import os
import subprocess
from main import ROOT_PATH


def exec(data):
    path_key = None
    path_repo = "{}/repositories/{}".format(ROOT_PATH,
                                            data.get('payload').get('name'))

    branch = data.get("payload").get("branch")
    if data.get('payload').get('key'):
        path_key = "{}/keys/{}".format(ROOT_PATH,
                                       data.get('payload').get('name'))
        with open(path_key, "w") as file:
            file.write(data.get('payload').get('key'))

    ssh_comand = "GIT_SSH_COMMAND='ssh -i {}'".format(
        path_key) if path_key else ''

    result = subprocess.run(
        f'{ssh_comand} git clone {data.get("payload").get("repo_url")} "{path_repo}"', shell=True, capture_output=True, text=True)
    if result.returncode == 1:
        raise Exception("error in clone repo")

    if branch:
        subprocess.run(
            command, shell=True, capture_output=True, text=True)
        command = f"cd {path_repo} && git checkout {branch}"
        if result.returncode == 1:
            raise Exception("error in checkout branch")

    return path_repo
