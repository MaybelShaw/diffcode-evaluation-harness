from models.StableDiffCoder import StableDiffCoder
from tasks.santacoder_fim import SantaCoderFim
from metrics.passk import PassK
from execution.executor_registry import get_executor
from utils.file_utils import TempWorkSpace
from tqdm import tqdm
import execution
from pprint import pprint


def test_evaluate():
    model = StableDiffCoder("/nvme3n1/XiaoMBworks/models/Stable-DiffCoder-8B-Base", "cuda")
    task = SantaCoderFim()
    dataset = task.get_dataset()
    dataset = dataset.select(range(10))
    results = []
    for data in tqdm(dataset):
        mid = model.generate(model.build_prompt(task.get_input(data)))
        code = data['prompt'] + mid + data['suffix'] + '\n' + data['tests']
        executor = get_executor(data['language'])
        workspace = TempWorkSpace()
        file = "test" + executor.suffix
        path = workspace.write(file, code)
        results.append(executor.run(path))
        workspace.cleanup()
    pprint(results)
    results = [r.returncode == 0 for r in results]
    pass_k = PassK(1)
    print(pass_k.evaluate(results))


if __name__ == '__main__':
    test_evaluate()
