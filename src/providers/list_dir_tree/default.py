import os
from main import ROOT_PATH


def exec(data):
    root_dir = '{}/repositories/{}'.format(ROOT_PATH,
                                           data.get("payload").get("repo_name"))

    arquivos = []
    for pasta_raiz, _, arquivos_na_pasta in os.walk(root_dir):
        for arquivo in arquivos_na_pasta:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            arquivos.append(caminho_completo)
    return arquivos
