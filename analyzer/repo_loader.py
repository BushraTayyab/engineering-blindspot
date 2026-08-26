import shutil
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from git import Repo


def clone_repository(repo_url):
    parsed = urlparse(repo_url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("Please provide a valid GitHub repository URL.")

    temp_dir = tempfile.mkdtemp(prefix="blindspot_")

    try:
        Repo.clone_from(repo_url, temp_dir)
        return Path(temp_dir)

    except Exception:
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise


def cleanup_repository(repo_path):
    shutil.rmtree(repo_path, ignore_errors=True)