import json

with open('example_2.json') as fh:
    ret_val = json.load(fh)

print(type(ret_val))
print(ret_val)
print(len(ret_val))
print(ret_val["quiz"]["sport"])