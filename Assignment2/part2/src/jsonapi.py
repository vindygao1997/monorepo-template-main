import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, complex):
            return {
                '_custom_type_': 'complex',
                'real': o.real,
                'imag': o.imag
            }
        elif isinstance(o, range):
            return {
                '_custom_type_': 'range',
                'start': o.start,
                'stop': o.stop,
                'step': o.step
            }
        
        return super().default(o)

def dumps(o):
    return json.dumps(o, cls=CustomJSONEncoder)

class CustomJSONDecoder(json.JSONDecoder):
    def object_hook(self, d):
        if '_custom_type_' in d:
            type_name = d['_custom_type_']
            if type_name == 'complex':
                return complex(d['real'], d['imag'])
            elif type_name == 'range':
                return range(d['start'], d['stop'], d['step'])
            
        return d
    
def loads(s):
    return json.loads(s, cls=CustomJSONDecoder)