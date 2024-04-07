import os

from main import ROOT_PATH
import subprocess


def exec(data):
    repo_data = data.get("get_repo").get("data")
    new_code = data.get("change_file").get("data")
    file_dir = data.get("payload").get("file_dir")
    dir_splited = file_dir.split(".")
    extension = None
    if len(dir_splited) == 1:
        temp_dir = dir_splited[0] + '_temp'
    else:
        temp_dir = file_dir + '_temp'
        extension = dir_splited[-1:][0]

    temp_dir = '{}/repositories/{}'.format(ROOT_PATH, temp_dir)
    original_dir = '{}/repositories/{}'.format(ROOT_PATH, file_dir)

    repo_dir = '{}/repositories/{}'.format(ROOT_PATH, repo_data.get('name'))
    subprocess.run(f"cd {repo_dir} && git checkout {repo_data.get('branch')}",
                   shell=True, capture_output=True, text=True)

    with open(temp_dir, "w") as file:
        file.write('\n'.join(new_code))

    return {
        "temp_dir": temp_dir,
        "original_dir": original_dir,
        "extension": extension
    }
