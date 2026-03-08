from .base import Executor
from .safe_subprocess import run
from .executor_registry import register_executor


@register_executor("java")
class JavaExecutor(Executor):

    suffix = ".java"

    def run(self, path):
        compile_result = run(["javac", str(path)])

        if compile_result['returncode'] != 0:
            return compile_result

        classname = path.stem

        return run(["java", "-cp", str(path.parent), classname])
