# -*- coding: utf-8 -*-
"""
@author: nurguiana.gavrileva
"""
ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12
    }, {
        "name": "petja",
        "age": 10
    }]
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21
    }, {
        "name": "pavel",
        "age": 15
    }]
}

def older_than(people, age):
    result = []
    for person in people:
        for child in person['children']:
            if child['age'] >= age:
                result.append(person)
                break
    return result

if __name__ == '__main__':
    arr = [ivan, darja]
    print(*[i['name'] for i in older_than(arr, 18)])