import subprocess


def exec(data):
    dirs = data.get("save_file").get("data")

    if dirs.get("extension") == "py":
        command = f"black --check {dirs.get('temp_dir')}"
        dir = dirs.get('temp_dir').replace(" ", "\ ")
        command_format = f"autopep8 --in-place --aggressive --aggressive {dir}"

        result = subprocess.run(command_format, shell=True,
                                capture_output=True, text=True)

        if result.returncode == 1:
            raise Exception("error in format file.")

    else:
        command = "echo ''"

    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)

    if result.returncode == 1:
        raise Exception("file not valid")
