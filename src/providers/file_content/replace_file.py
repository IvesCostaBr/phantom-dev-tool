import os


def exec(data):
    dirs = data.get("save_file").get("data")

    if not data.get("validate_file").get("status"):
        os.remove(dirs.get("temp_dir"))

    os.rename(dirs.get("temp_dir"), dirs.get("original_dir"))
