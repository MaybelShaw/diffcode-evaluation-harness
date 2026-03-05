from abc import ABC, abstractmethod

class Task(ABC):

    DATASET_PATH: str = None

    def __init__(self):
        pass

    @abstractmethod
    def get_dataset(self):
        return []

    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def get_reference(self):
        pass

    @abstractmethod
    def postprocess_generation(self):
        pass

    @abstractmethod
    def process_results(self):
        pass