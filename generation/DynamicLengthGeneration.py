from .base import GenerationStrategy


class DynamicLengthGeneration(GenerationStrategy):
    def __init__(self, start=64, step=64, max_length=512):
        self.start = start
        self.step = step
        self.max_length = max_length

    def generate(self, model, prompt, exectuor):
        gen = ""
        length = self.start

        while length <= self.max_length:
            gen = model.generate(prompt=prompt, length=length, )

            if exectuor.syntax_check(gen):
                return gen

            length = length + self.step

        return gen
