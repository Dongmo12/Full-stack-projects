import json

json_file = 'file.json'

my_family = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)

a = my_family["children"][0]["favorite_color"]= ' blue'
b = my_family["children"][1]["favorite_color"]= 'red'
c = my_family["color"][3]= " for the first elememt tey tp "

with open(json_file, 'a') as file_obj1:
    json.dump(a, file_obj1, indent = 2, sort_keys=True)
    json.dump(b, file_obj1, indent=2, sort_keys=True)