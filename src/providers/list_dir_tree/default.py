import os
from main import ROOT_PATH


def exec(data):
    root_dir = '{}/repositories/{}'.format(ROOT_PATH,
                                           data.get("payload").get("repo_name"))

    arquivos = []
    for root_path, _, files_folder in os.walk(root_dir):
        for arquivo in files_folder:
            full_path = os.path.join(root_path, arquivo)
            path_splited = full_path.split(
                f"{os.environ.get('PROJECT_NAME')}/repositories")
            for each in [".git/"]:
                if not each in path_splited[1]:
                    arquivos.append(path_splited[1])
    return arquivos
