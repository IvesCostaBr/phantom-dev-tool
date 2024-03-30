import os


def exec(data):
    new_code = data.get("change_file").get("data")
    file_dir = data.get("payload").get("file_dir")
    dir_splited = file_dir.split(".")
    extension = None
    if len(dir_splited) == 1:
        temp_dir = dir_splited[0] + '_temp'
    else:
        temp_dir = dir_splited[0] + '_temp.' + dir_splited[1]
        extension = dir_splited[1]

    with open(temp_dir, "w") as file:
        file.write('\n'.join(new_code))

    return {
        "temp_dir": temp_dir,
        "original_dir": file_dir,
        "extension": extension
    }