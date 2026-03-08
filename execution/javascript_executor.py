from .base import Executor
from .safe_subprocess import run

class JavaScriptExecutor(Executor):

    def run(self, path):
        return run(["node", str(path)])