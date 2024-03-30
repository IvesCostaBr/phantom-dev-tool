def return_pipe(data):
    return [
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
