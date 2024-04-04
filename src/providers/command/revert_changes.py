from main import ROOT_PATH
import subprocess


def exec(data):
    repo_name = data.get("payload").get("repo_name")
    formated_dir = ROOT_PATH.replace(" ", "\ ")
    repo_data = data.get("get_repo")
    extra_command = ''
    if repo_data.get('key'):
        extra_command = "GIT_SSH_COMMAND='ssh -i {}'&&".format(
            repo_data.get('key'))
    command = f'{extra_command} cd {formated_dir}/repositories/{repo_name} && git reset --hard'
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode == 1:
        raise Exception("error in revert file")
