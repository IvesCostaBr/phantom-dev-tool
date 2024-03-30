import os


def exec(data):
    file_dir = data.get("payload").get("file_dir")

    with open(file_dir, 'r') as file:
        content = file.read()

        lines = content.strip().split('\n')
        code = []
        for i, linha in enumerate(lines, start=0):
            code.append(f"{i}: {linha}")
        return code
