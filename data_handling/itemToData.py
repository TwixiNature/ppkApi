import json


def objectToJson(object, type):

    return json.dumps(vars(object))
