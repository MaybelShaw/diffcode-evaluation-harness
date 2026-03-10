from .base import GenerationStrategy


class SimpleGeneration(GenerationStrategy):
    def generate(self, model, prompt, **kwargs):
        return model.generate(prompt=prompt, **kwargs)