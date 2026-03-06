from abc import ABC, abstractmethod

class Task(ABC):

    DATASET_PATH: str = None

    def __init__(self):
        pass

    @abstractmethod
    def get_dataset(self):
        return []

    @abstractmethod
    def get_input(self,doc):
        pass

    @abstractmethod
    def get_reference(self,doc):
        pass

    @abstractmethod
    def postprocess_generation(self,generation):
        pass

    @abstractmethod
    def process_results(self):
        pass