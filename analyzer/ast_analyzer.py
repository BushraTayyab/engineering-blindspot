import ast
from pathlib import Path

sample_file = Path(__file__).resolve().parent.parent / "sample_repo" / "hello.py"
source = sample_file.read_text()
tree = ast.parse(source)
for node in ast.walk(tree):
    if isinstance(node, ast.ImportFrom):
        print(node.module)