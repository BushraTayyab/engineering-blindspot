import ast
from pathlib import Path


def find_related_tests(repo_path, changed_file):
    repo_path = Path(repo_path)
    changed_file = Path(changed_file)

    changed_module = changed_file.stem
    related_tests = []

    for file_path in repo_path.rglob("*.py"):

        if not (
            file_path.name.startswith("test_")
            or file_path.name.endswith("_test.py")
        ):
            continue

        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == changed_module:
                        if file_path.name not in related_tests:
                            related_tests.append(file_path.name)

            elif isinstance(node, ast.ImportFrom):
                if node.module == changed_module:
                    if file_path.name not in related_tests:
                        related_tests.append(file_path.name)

    return related_tests

if __name__ == "__main__":
    result = find_related_tests(
        "sample_repo",
        "hello.py"
    )
    print(result)