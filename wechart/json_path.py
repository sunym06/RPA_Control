d = {
    'ads': [
        {
            'id': 1,
            'name': 'tom'
        },
        {
            'id': 2,
            'name': 'lucy'
        }
    ]
}

import jsonpath

ids = jsonpath.jsonpath(d, '$..id')
print(ids)