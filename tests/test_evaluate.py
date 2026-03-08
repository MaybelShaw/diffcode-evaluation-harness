from models.StableDiffCoder import StableDiffCoder
from tasks.santacoder_fim import SantaCoderFim
from metrics.passk import PassK
from execution.executor_registry import get_executor
from utils.file_utils import TempWorkSpace

def test_evaluate():
    model = StableDiffCoder("/nvme3n1/XiaoMBworks/models/Stable-DiffCoder-8B-Base")
    task = SantaCoderFim()
    dataset = task.get_dataset()
    dataset = dataset[:10]
    for data in dataset:
        mid = model.generate(model.build_prompt(task.get_input(data)))
        code = data['prompt']+mid+data['suffix']+'\n'+data['test']
        executor = get_executor(data['language'])
        workspace = TempWorkSpace()
        path = workspace.write("test.js", code)