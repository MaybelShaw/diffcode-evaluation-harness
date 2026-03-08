from .base import Executor
from .safe_subprocess import run
from executor_registry import register_executor


@register_executor("python")
class PythonExecutor(Executor):
    suffix = ".py"

    def run(self, path):
        return run(["python3", str(path)])
