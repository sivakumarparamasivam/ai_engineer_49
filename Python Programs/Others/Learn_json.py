# data ={
#     'name': 'sivakumar',
#     'age': 25,
#     'city': 'chennai',
#     'value': None  ,
#     'is_nothing': True,
#     'hobbies': ('coding', 'reading', 'sports')
# }

# print(type(data))
# import json
# json_data = json.dumps(data, indent=4)
# print(type(json_data))
# print(json_data)

# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)

# python_obj = json.loads(json_data)
# print(type(python_obj))
# print(python_obj)
import json
with open('data.json', 'r') as file1:
    data_new = json.load(file1)
    # data_new=json.loads(data_new)
print(data_new)