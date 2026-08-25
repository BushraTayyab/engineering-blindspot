import ast
from pathlib import Path


def analyze_file(file_path):
    file_path = Path(file_path)

    source = file_path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    functions = []
    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    return {
        "file": file_path.name,
        "functions": functions,
        "imports": imports
    }
if __name__ == "__main__":
    result = analyze_file("sample_repo/hello.py")
    print(result)