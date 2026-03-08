from .base import Executor
from .safe_subprocess import run


class PythonExecutor(Executor):
    def run(self, path):
        return run(["python3", str(path)])
