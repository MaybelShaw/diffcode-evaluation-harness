from utils.file_utils import TempWorkSpace
from execution.python_executor import PythonExecutor
from execution.java_executor import JavaExecutor
from execution.javascript_executor import JavaScriptExecutor


def test_python():
    content = """
print(111)
"""
    workspace = TempWorkSpace()
    path = workspace.write("test.py", content)

    executor = PythonExecutor()
    print(executor.run(path))


def test_java():
    content = """
public class Hello {
    public static void main(String[] args) {
        System.out.println(111);
    }
}
"""
    workspace = TempWorkSpace()
    path = workspace.write("Hello.java", content)

    executor = JavaExecutor()
    print(executor.run(path))


def test_js():
    content = """
console.log(111)
"""
    workspace = TempWorkSpace()
    path = workspace.write("test.js", content)

    executor = JavaScriptExecutor()
    print(executor.run(path))


if __name__ == "__main__":
    test_python()
    test_java()
    test_js()