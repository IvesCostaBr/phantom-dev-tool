def return_pipe(data):
    return [
        {
            "name": "get_repo",
            "provider": "repo_data",
            "module": "get_repo",
        },
        {
            "name": "commit_and_push",
            "provider": "command",
            "module": "commit",
        },

        {
            "name": "response",
            "provider": "response",
            "module": "response_complete"
        }
    ]
