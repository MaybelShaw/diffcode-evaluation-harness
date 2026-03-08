from .base import Executor
from .safe_subprocess import run
from executor_registry import register_executor


@register_executor("js")
class JavaScriptExecutor(Executor):
    suffix = ".js"

    def run(self, path):
        return run(["node", str(path)])
