def return_pipe(data):
    return [
        {
            "name": "list_repo",
            "provider": "list_repo",
            # "module": ""
        },
        # {
        #     "name": "save depository data"
        # },
        {
            "name": "response",
            "provider": "response",
            "module": "response_list_repo"
        }
    ]
