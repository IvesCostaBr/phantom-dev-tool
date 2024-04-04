from src.repository import code_repo


def exec(data):
    data = code_repo.filter_query(namme=data.get("payload").get("repo_name"))
    if not data:
        return None
    return data[0]
