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
    
    
def get_commit_diff(repo_path):
    repo = Repo(repo_path)

    commit = repo.head.commit

    if not commit.parents:
        raise ValueError("Cannot analyze root commit")

    parent = commit.parents[0]

    diffs = parent.diff(commit, create_patch=True)

    changes = []

    for diff in diffs:
        if diff.change_type == "D":
            continue

        patch = diff.diff.decode("utf-8", errors="replace")

        changes.append({
            "file": diff.b_path,
            "change_type": diff.change_type,
            "diff": patch
        })

    return changes

if __name__ == "__main__":
    result = get_commit_diff("../blindspot-demo-orders")

    for change in result:
        print(change["file"])
        print(change["diff"])