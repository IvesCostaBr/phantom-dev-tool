from main import ROOT_PATH
import subprocess


def exec(data):
    repo_name = data.get("payload").get("repo_name")
    repo_data = data.get("get_repo").get("data")
    formated_dir = ROOT_PATH.replace(" ", "\ ")
    command = f'cd {formated_dir}/repositories/{repo_name} && git checkout {repo_data.get("branch")} && git revert HEAD'
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode == 1:
        raise Exception("error in revert file")
