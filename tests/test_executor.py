from utils.file_utils import TempWorkSpace
from execution.python_executor import PythonExecutor

content = """
print(111)
"""

workspace = TempWorkSpace()
path = workspace.write("tesy.py", content)
executor = PythonExecutor()
print(executor.run(path))