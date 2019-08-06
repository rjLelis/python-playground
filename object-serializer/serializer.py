import json

def serialize(object):

    ''' Serializes a class object into json '''
    attribute_list = [attr for attr in dir(object) if not attr.startswith('__')]
    attributes_dict = {}

    for attribute in attribute_list:
        attributes_dict[attribute] = getattr(object, attribute)

    return json.dumps(attributes_dict, indent=2)


def deserialize(content ,class_to_deserialize):
    json_content = json.loads(content)
    if type(json_content) == list:
        pass