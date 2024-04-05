import subprocess
from main import ROOT_PATH


def exec(data):
    exists_repo = data.get("get_repo").get("data")
    if exists_repo:
        raise Exception("repository already exists")
    path_key = None
    path_repo = "{}/repositories/{}".format(ROOT_PATH,
                                            data.get('payload').get('repo_name'))

    branch = data.get("payload").get("branch")
    add_key_agent = "eval $(ssh-agent) && ssh-add ~/.ssh/default"
    clone_command = f'{add_key_agent} && git clone {data.get("payload").get("repo_url")} "{path_repo}"'

    result = subprocess.run(clone_command, shell=True,
                            capture_output=True, text=True)
    if result.returncode in [1, 128]:
        raise Exception("error in clone repo")

    result = subprocess.run('git config --global user.email "ivespauiniam@gmail.com" && git config --global user.name "Ives Costa"', shell=True,
                            capture_output=True, text=True)

    if branch:
        command = f"cd {path_repo} && git checkout {branch}"
        subprocess.run(
            command, shell=True, capture_output=True, text=True)

        if result.returncode in [1, 128]:
            raise Exception("error in checkout branch")

    return {"path_repo": path_repo, "path_key": path_key}
