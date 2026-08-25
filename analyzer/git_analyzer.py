from git import Repo


def analyze_commit(repo_path):
    repo = Repo(repo_path)

    head = repo.head
    commit = head.commit

    if not commit.parents:
        raise ValueError("Cannot analyze root commit")

    parent = commit.parents[0]

    diffs = commit.diff(parent)

    changed_files = []

    for diff in diffs:
        if diff.change_type == "D":
            changed_files.append(diff.a_path)
        else:
            changed_files.append(diff.b_path)

    return {
        "commit": commit.hexsha,
        "message": commit.message.strip(),
        "changed_files": changed_files
    }