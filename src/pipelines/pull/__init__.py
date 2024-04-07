def return_pipe(data):
    return [
        {
            "name": "get_repo",
            "provider": "repo_data",
            "module": "get_repo",
        },
        {
            "name": "pull",
            "provider": "command",
            "module": "pull",
        },
        {
            "name": "response",
            "provider": "response",
            "module": "response_complete"
        }
    ]
