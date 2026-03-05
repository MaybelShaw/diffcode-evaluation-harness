from abc import ABC, abstractmethod

class BaseModel(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def build_prompt(self,input):
        pass

    @abstractmethod
    def generate(self,prompt,**kwargs):
        pass