from datetime import datetime
from main import ROOT_PATH
import uuid
import subprocess


def exec(data):
    repo_name = data.get("payload").get("repo_name")
    repo_data = data.get("get_repo").get("data")

    formated_dir = ROOT_PATH.replace(" ", "\ ")
    add_key_agent = "eval $(ssh-agent) && ssh-add  ~/.ssh/default"

    command = f'cd {formated_dir}/repositories/{repo_name} && git checkout {repo_data.get("branch")} && {add_key_agent} && git push origin HEAD'

    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode == 1:
        raise Exception("error in format file.")
