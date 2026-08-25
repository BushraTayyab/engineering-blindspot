from pathlib import Path
from git import Repo

repo_path = Path(__file__).resolve().parent.parent / "sample_repo"
repo = Repo(repo_path)

head = repo.head
commit = head.commit
parent = commit.parents[0]
diff = commit.diff(parent)

print(commit.hexsha)
print(commit.message)
print(parent)
print(type(diff))

for file_diff in diff:
    print("Old:", file_diff.a_path)
    print("New:", file_diff.b_path)