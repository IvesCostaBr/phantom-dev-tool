def return_pipe(data):
    return [
        {
            "name": "get_repo",
            "provider": "repo_data",
            "module": "get_repo",
        },
        {
            "name": "file_content",
            "provider": "file_content",
            # "module": ""
        },
        # {
        #     "name": "save depository data"
        # },
        {
            "name": "response",
            "provider": "response",
            "module": "response_file_content"
        }
    ]
