import os

from main import ROOT_PATH


def exec(data):
    file_name = data.get("payload").get("file_dir")

    file_dir = '{}/repositories/{}'.format(ROOT_PATH, file_name)

    with open(file_dir, 'r') as file:
        content = file.read()

        lines = content.strip().split('\n')
        code = []
        for i, linha in enumerate(lines, start=0):
            code.append(f"{i}: {linha}")
        return code
