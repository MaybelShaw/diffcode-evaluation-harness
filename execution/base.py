from abc import ABC, abstractmethod


class Executor(ABC):
    suffix: str

    @abstractmethod
    def run(self, path):
        pass
