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
    dataset = dataset.select(range(50))
    results = []
    for data in tqdm(dataset):
        if data['language'] != 'py':
            continue
        mid = model.generate(model.build_prompt(task.get_input(data)),gen_length=64)
        if data['language'] == "java":
            s = data['tests']
            s = s[s.find('\n') + 1:]
            # print(data['suffix'][:-1])
            code = data['prompt'] + data['canonical_solution']+data['suffix'][:-4] + data['tests'][1:]
        else:
            code = data['prompt'] + mid + data['suffix'] + data['tests']
        pprint({"prefix": data['prompt'], "mid": mid, "suffix": data['suffix'], "tests": data['tests'],"c":data['canonical_solution']})
        # print(code)
        # # exit(0)
        # code = "\n".join([
        #     data["prompt"],
        #     mid,
        #     data["suffix"],
        #     data["tests"]
        # ])
        # print(code)
        # exit(0)
        executor = get_executor(data['language'])
        workspace = TempWorkSpace()
        file = "Problem" + executor.suffix
        path = workspace.write(file, code)
        result = executor.run(path)
        results.append(result)
        workspace.cleanup()
        # if result.returncode == 1:
            # print(code)
            # print(result)
            # exit(0)
    pprint(results)
    results = [r.returncode == 0 for r in results]
    pass_k = PassK(1)
    print(pass_k.evaluate(results))


if __name__ == '__main__':
    test_evaluate()
