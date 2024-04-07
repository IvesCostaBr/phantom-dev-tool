import subprocess
from main import ROOT_PATH


def exec(data):
    repo_dir = "{}/repositories/{}".format(ROOT_PATH,
                                           data.get("get_repo").get("data").get("name"))
    branch = data.get("get_repo").get("data").get("branch")

    add_key_agent = "eval $(ssh-agent) && ssh-add ~/.ssh/default"
    result = subprocess.run(f"{add_key_agent} && cd {repo_dir} && git checkout {branch} && git pull origin HEAD", shell=True,
                            capture_output=True, text=True)

    if result.returncode == 1:
        raise Exception("error in pull repository")
