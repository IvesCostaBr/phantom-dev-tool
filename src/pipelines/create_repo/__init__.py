def return_pipe(data):
    return [
        {
            "name": "get_repo",
                    "provider": "repo_data",
                    "module": "get_repo",
        },
        {
            "name": "download_repository",
            "provider": "command",
            "module": "download_repo"
           
        },
        {
            "name": "save_repo",
            "provider": "repo_data",
            "condition": {
                "step": "download_repository",
                "value": True
            }
            # "module": ""
        },
        {
            "name": "response",
            "provider": "response",
            "module": "response_create_repo"
        }
    ]
