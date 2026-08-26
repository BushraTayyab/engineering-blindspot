from pathlib import Path

from analyzer.git_analyzer import analyze_commit
from analyzer.ast_analyzer import analyze_file
from analyzer.dependency_analyzer import find_dependents
from analyzer.test_analyzer import find_related_tests


def analyze_impact(repo_path):
    git_result = analyze_commit(repo_path)

    changes = []

    for changed_file in git_result["changed_files"]:
        file_path = Path(repo_path) / changed_file

        code_result = analyze_file(file_path)

        dependents = find_dependents(
            repo_path,
            changed_file
        )

        related_tests = find_related_tests(
            repo_path,
            changed_file
        )

        # Separate production dependents from test files
        production_dependents = [
            file for file in dependents
            if not (
                file.startswith("test_")
                or file.endswith("_test.py")
            )
        ]

        changes.append({
            "file": changed_file,
            "code": code_result,
            "dependents": production_dependents,
            "related_tests": related_tests
        })

    return {
        "commit": {
            "hash": git_result["commit"],
            "message": git_result["message"]
        },
        "changes": changes
    }


if __name__ == "__main__":
    result = analyze_impact("sample_repo")
    print(result)