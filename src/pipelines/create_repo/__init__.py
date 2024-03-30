def return_pipe(data):
    return [
        {
            "name": "download_repository",
            "provider": "command",
            "module": "download_repo"
        },
        {
            "name": "save_repo",
            "provider": "create_repo",
            # "module": ""
        },
        {
            "name": "response",
            "provider": "response",
            "module": "response_create_repo"
        }
    ]
