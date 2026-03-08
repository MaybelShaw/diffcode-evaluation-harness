from .base import Executor
from .safe_subprocess import run, Result
from .executor_registry import register_executor


@register_executor("java")
class JavaExecutor(Executor):
    suffix = ".java"

    def run(self, path):
        compile_result = run(["javac", str(path)])

        if compile_result.returncode != 0:
            return Result(status="CompileError", returncode=compile_result.returncode, stdout=compile_result.stdout,
                          stderr=compile_result.stderr,
                          timeout=False)

        classname = path.stem

        return run(["java", "-cp", str(path.parent), classname])
