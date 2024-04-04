from datetime import datetime
from main import ROOT_PATH
import uuid
import subprocess


def exec(data):
    repo_name = data.get("payload").get("repo_name")
    repo_data = data.get("get_repo")

    commit_msg = f"{uuid.uuid4()}-{datetime.now()}"
    formated_dir = ROOT_PATH.replace(" ", "\ ")

    extra_command = ''
    if repo_data.get('key'):
        extra_command = "GIT_SSH_COMMAND='ssh -i {}'&&".format(
            repo_data.get('key'))

    command = f'{extra_command} cd {formated_dir}/repositories/{repo_name} && git add . && git commit -m "{commit_msg}" && git push origin HEAD'

    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode == 1:
        raise Exception("error in format file.")
    return {"commit_msg": commit_msg}
