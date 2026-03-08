from .base import Executor
from .safe_subprocess import run

class JavaExecutor(Executor):

    def run(self, path):
        return run(["javac", str(path)])