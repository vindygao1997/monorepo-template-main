import jsonapi
import json

def test_complex():
    assert jsonapi.loads(jsonapi.dumps(1 + 2j)) == 1 + 2j
    
def test_range():
    assert jsonapi.loads(jsonapi.dumps(range(0, 100, 10))) == range(0, 100, 10)