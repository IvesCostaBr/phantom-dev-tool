import os
from git import Repo
from main import ROOT_PATH
import subprocess


def exec(data):
    repo_data = data.get("get_repo").get("data")
    file_name = data.get("payload").get("file_dir")
    repo_dir = '{}/repositories/{}'.format(ROOT_PATH,
                                           data.get("payload").get("repo_name"))

    file_dir = '{}/repositories{}'.format(ROOT_PATH, file_name)

    try:

        subprocess.run(f"cd {repo_dir} && git checkout {repo_data.get('branch')}",
                       shell=True, capture_output=True, text=True)

        try:
            with open(file_dir, 'r') as file:
                content = file.read()
                lines = content.strip().split('\n')
                code = []
                for i, linha in enumerate(lines, start=0):
                    code.append(f"{i}: {linha}")
                return code
        except FileNotFoundError:
            # Arquivo não encontrado, criar um arquivo vazio
            with open(file_dir, 'w') as file:
                file.write('')
            return []
    except:
        raise Exception("file not found")
