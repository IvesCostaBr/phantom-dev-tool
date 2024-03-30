import json

def format_data_receiver(value):
    try:
        formated_value = int(value)
        return formated_value
    except ValueError:
        pass

    try:
        formated_value = float(value)
        return formated_value
    except ValueError:
        pass

    try:
        formated_value = json.loads(value)
        return formated_value
    except ValueError:
        pass

    if value.lower() == "True":
        return True
    elif value.lower() == "False":
        return False

    return None