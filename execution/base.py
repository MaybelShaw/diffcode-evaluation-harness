from abc import ABC, abstractmethod


class Executor(ABC):
    @abstractmethod
    def run(self, **kwargs):
        pass
