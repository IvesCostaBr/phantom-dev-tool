import subprocess
import os


def exec(data):
    file_dir = '/home/appuser/.ssh/default.pub'
    exists_key = os.path.isfile(file_dir)
    if not exists_key:
        command_generate_ssh_key = 'ssh-keygen -t rsa -b 4096 -C "$1" -f "$HOME/.ssh/default" -N ""'

        start_agent_ssh = "eval $(ssh-agent)"

        add_key_agent = "ssh-add  ~/.ssh/default"

        result = subprocess.run(f"{command_generate_ssh_key} && {start_agent_ssh} && {add_key_agent}", shell=True,
                                capture_output=True, text=True)

        if result.returncode == 1:
            raise Exception("error in get ssh key")

    with open(file_dir, 'r') as file:
        content = file.read()
        return content
