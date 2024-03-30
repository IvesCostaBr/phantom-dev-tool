from src.repository import code_repo


def exec(data):
    payload = {
        "name": data.get("payload").get("name"),
        "key": data.get("payload").get("key"),
        "repo_dir": data.get("download_repository").get("data"),
        "branch":  data.get("payload").get("branch"),
    }
    return code_repo.create(**payload)
