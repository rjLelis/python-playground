import json

def serialize(obj):

    ''' Serializes a class object into json '''
    attribute_list = [attr for attr in dir(obj) if not attr.startswith('__')]
    attributes_dict = {}

    for attribute in attribute_list:
        attributes_dict[attribute] = getattr(obj, attribute)

    return json.dumps(attributes_dict, indent=2)


def deserialize(content, klass):
    json_content = json.loads(content)
    if type(json_content) == list:
        for content in json:
            pass
        return

    c = klass()
    for key, value in json_content.items():
        setattr(c, key, value)
    return c



class Pessoa:

    def __init__(self):
        self.nome = 'Renato'
        self.idade = 23
