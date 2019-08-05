import json

def serialize(object):

    attribute_list = [attr for attr in dir(object) if not attr.startswith('__')]
    attributes_dict = {}

    for attribute in attribute_list:
        attributes_dict[attribute] = object.__getattribute__(attribute)

    return json.dumps(attributes_dict, indent=2)