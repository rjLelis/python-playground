import json

def serialize(obj):

    ''' Serializes a class object into json '''
    attribute_list = [attr for attr in dir(obj) if not attr.startswith('__')]
    attributes_dict = {}

    for attribute in attribute_list:
        attributes_dict[attribute] = getattr(obj, attribute)

    return json.dumps(attributes_dict, indent=2)


def deserialize(content, klass, many=False):
    json_content = json.loads(content)
    if many:
        class_list = []
        for content in json_content:
            c = klass()
            for key, value in content.items():
                if hasattr(c, key):
                    setattr(c, key, value)
                    class_list.append(c)
        return class_list

    c = klass()
    for key, value in json_content.items():
        if hasattr(c, key):
            setattr(c, key, value)
    return c
