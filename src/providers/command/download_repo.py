import subprocess
from main import ROOT_PATH


def exec(data):
    path_key = None
    path_repo = "{}/repositories/{}".format(ROOT_PATH,
                                            data.get('payload').get('name'))

    branch = data.get("payload").get("branch")
    key = data.get('payload').get('key')
    if key:
        path_key = f"{ROOT_PATH}/keys/{data.get('payload').get('name')}"
        with open(path_key, "w") as file:
            file.write('\n'.join(key))

    ssh_comand = "GIT_SSH_COMMAND='ssh -i {}'".format(
        path_key) if key else ''

    clone_command = f'{ssh_comand} git clone {data.get("payload").get("repo_url")} "{path_repo}"'

    result = subprocess.run(clone_command, shell=True,
                            capture_output=True, text=True)
    if result.returncode in [1, 128]:
        raise Exception("error in clone repo")

    if branch:
        command = f"cd {path_repo} && git checkout {branch}"
        subprocess.run(
            command, shell=True, capture_output=True, text=True)

        if result.returncode in [1, 128]:
            raise Exception("error in checkout branch")

    return {"path_repo": path_repo, "path_key": path_key}
