import os
import uuid
from datetime import datetime
from git import Repo
import subprocess
from main import ROOT_PATH


def exec(data):
    dirs = data.get("save_file").get("data")

    repo = Repo(
        f"{ROOT_PATH}/repositories/{data.get('payload').get('repo_name')}")
    branch = data.get("get_repo").get("data")
    repo.git.checkout(branch.get("branch"))

    # subprocess.call()

    if not data.get("validate_file").get("status"):
        os.remove(dirs.get("temp_dir"))

    os.rename(dirs.get("temp_dir"), dirs.get("original_dir"))

    commit_msg = f"{uuid.uuid4()}-{datetime.now()}"

    repo.git.add(dirs.get("original_dir"))
    repo.git.commit(m=commit_msg)

    return {"commit_msg": commit_msg}
