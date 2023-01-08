# Implement a function that receives a directory path (str) as an argument, iterates the given directory,
# and creates a nested dictionary that corresponds to the structure of the directory and the files in it.

import os
import json
from pprint import pprint


def dir2dict(dp: str, jp: str = None):
    if not os.path.exists(dp):
        raise FileNotFoundError(f"Dir {dp} not found")

    directory_dict = {}

    root, dirs, files = next(os.walk(dp))
    dir_dict = {'files': files, 'dirs': [dir2dict(os.path.join(root, d)) for d in dirs]}
    directory_dict[os.path.basename(root)] = dir_dict

    # for root, dirs, files in os.walk(dp):
    #     dir_dict = {'files': files, 'dirs': [dir2dict(os.path.join(root, d)) for d in dirs]}
    #     directory_dict[os.path.basename(root)] = dir_dict
    #     break

    if jp:
        with open(jp, 'w') as f:
            json.dump(directory_dict, f)
            print('JSON file created')

    return directory_dict


pprint(dir2dict('dir_ex', './files/d6_5.json'))
print('\n')
pprint(dir2dict('dir_ex'))
