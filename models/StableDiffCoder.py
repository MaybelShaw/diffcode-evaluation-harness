from base import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class StableDiffCoder(BaseModel):
    def __init__(self, model_path=None, device='cpu'):
        super().__init__()
        self.device = device
        self.model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True,
                                                          torch_dtype=torch.bfloat16).to(self.device).eval()
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

    def build_prompt(self, input):
        return '<[fim-suffix]>' + input['suffix'] + '<[fim-prefix]>' + input['prefix'] + '<[fim-middle]>'

    def generate(self, prompt, steps=64, gen_length=64, block_length=4, temperature=0.,
                 remasking='low_confidence', shift=False, threshold=None,
                 ):
        input_ids = self.tokenizer(prompt)['input_ids']
        input_ids = torch.tensor(input_ids).to(self.device).unsqueeze(0)

        out = self.model.generate(input_ids, steps=steps, gen_length=gen_length, block_length=block_length,
                                  temperature=temperature, remasking=remasking, tokenizer=self.tokenizer, shift=False,
                                  threshold=None, eos_id=self.tokenizer.eos_token_id)

        return self.tokenizer.decode(out[0][input_ids.shape[1]:], skip_special_tokens=True)


if __name__ == '__main__':
    stable_diff_coder = StableDiffCoder('/nvme3n1/XiaoMBworks/models/Stable-DiffCoder-8B-Base', device='cuda')

    prefix = "def add_numbers(a, b):\n    "
    suffix = "\n    return result"

    prompt = stable_diff_coder.build_prompt({'prefix': prefix, 'suffix': suffix})

    print(stable_diff_coder.generate(prompt))
