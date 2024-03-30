import json


def parse_data(value):
    try:
        if type(value) == dict:
            return json.dumps(value)
        return str(value)
    except Exception as ex:
        print(ex)
        raise Exception("error in parser data")
