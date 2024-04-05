from src.repository import code_repo


def exec(data):
    payload = {
        "name": data.get("payload").get("repo_name"),
        "key":  data.get("download_repository").get("data").get("path_key"),
        "repo_dir": data.get("download_repository").get("data").get("path_repo"),
        "branch":  data.get("payload").get("branch"),
    }
    return code_repo.create(**payload)
