# Implement a function that receives a directory path (str) as an argument, iterates the given directory,
# and creates a nested dictionary that corresponds to the structure of the directory and the files in it.

import os
from pprint import pprint


def dir2dict(dp: str):
    directory_dict = {}

    for root, dirs, files in os.walk(dp):
        dir_dict = {'files': files, 'dirs': [dir2dict(os.path.join(root, d)) for d in dirs]}
        directory_dict[os.path.basename(root)] = dir_dict
        break

    return directory_dict


pprint(dir2dict('dir_ex'))
