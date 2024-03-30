def return_pipe(data):
    return [
        {
            "name": "file_content",
            "provider": "file_content",
            # "module": ""
        },
        {
            "name": "change_file",
            "provider": "file_content",
            "module": "analize_file",
        },
        {
            "name": "save_file",
            "provider": "file_content",
            "module": "save_file"
        },
        {
            "name": "validate_file",
            "provider": "command",
            "module": "validate_file"
        },
        {
            "name": "replace_file",
            "provider": "file_content",
            "module": "replace_file",
        },
        {
            "name": "response",
            "provider": "response",
            "module": "response_complete"
        }
    ]
