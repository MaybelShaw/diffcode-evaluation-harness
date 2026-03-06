from .base import Task
from datasets import load_dataset


class SantaCoderFim(Task):
    DATASET_PATH = '/nvme3n1/XiaoMBworks/datasets/santacoder-fim-task/'

    def __init__(self):
        super().__init__()
        self.dataset = load_dataset(self.DATASET_PATH)

    def get_dataset(self):
        return self.dataset['train']

    def get_input(self, doc):
        return {
            'prefix': doc['prompt'],
            'suffix': doc['suffix'],
        }

    def get_reference(self, doc):
        return doc['canonical_solution']

    def postprocess_generation(self,generation):
        return generation

    def process_results(self):
        pass

if __name__ == "__main__":
    task = SantaCoderFim()
    dataset = task.get_dataset()
    sample = dataset[0]
    from pprint import  pprint

    pprint(task.get_reference(sample))
    pprint(task.get_input(sample))