def return_pipe(data):
    return [
        {
            "name": "process_tree_repository",
            "provider": "list_dir_tree",
            # "module": ""
        },
        # {
        #     "name": "save depository data"
        # },
        {
            "name": "response",
            "provider": "response",
            "module": "response_list_tree_repo"
        }
    ]
