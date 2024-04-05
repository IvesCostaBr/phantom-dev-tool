def return_pipe(data):
    return [
        {
            "name": "file_content",
            "provider": "command",
            "module": "get_public_key"
        },
        # {
        #     "name": "save depository data"
        # },
        {
            "name": "response",
            "provider": "response",
            "module": "response_public_key"
        }
    ]
