from copy import deepcopy


def exec(data: dict):
    if data.get("errors"):
        response = deepcopy(data.get("errors"))
        return {"errors": response}
    return {"detail": True}
