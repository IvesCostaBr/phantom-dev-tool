def exec(data):
    file_dir = data.get("payload").get("file_dir")
    start_line = data.get("payload").get("start")
    end_line = data.get("payload").get("end")
    new_code = data.get("payload").get("code")

    old_code = data.get("file_content").get("data")

    new_code_list = []
    for each in new_code:
        new_code_list.append(each)

    sub_count = 0
    if not start_line and end_line:
        for i, line in enumerate(old_code, start=0):
            if i >= start_line and i <= end_line:
                old_code[i] = f'{i}: {new_code_list[sub_count]}'
                sub_count += 1
        formated_code = [line.split(
            ": ", 1)[1] if ": " in line else line for line in old_code]
        return formated_code
    else:
        old_code = new_code_list
        return old_code
