from models.StableDiffCoder import StableDiffCoder
from tasks.santacoder_fim import SantaCoderFim

def test_generate():
    model = StableDiffCoder('/nvme3n1/XiaoMBworks/models/Stable-DiffCoder-8B-Base', device='cuda')
    task = SantaCoderFim()

    dataset = task.get_dataset()
    sample = dataset[0]
    prompt = model.build_prompt(task.get_input(sample))
    generation = model.generate(prompt)
    print(task.postprocess_generation(generation))

if __name__ == "__main__":
    test_generate()