from copy import deepcopy


def exec(data):
    if data.get("errors"):
        response = deepcopy(data.get("errors"))
        return {"errors": response}
    return {"clone": data.get("download_repository").get("data")}
