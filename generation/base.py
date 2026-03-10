from abc import ABC, abstractmethod


class GenerationStrategy(ABC):
    @abstractmethod
    def generate(self, model, prompt, **kwargs):
        pass
