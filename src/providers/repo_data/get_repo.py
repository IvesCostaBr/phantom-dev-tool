from src.repository import code_repo


def exec(data):
    result = code_repo.filter_query(name=data.get("payload").get("repo_name"))
    if not result:
        return None
    return result[0]
