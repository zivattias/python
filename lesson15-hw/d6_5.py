# Implement a function that receives a directory path (str) as an argument, iterates the given directory,
# and creates a nested dictionary that corresponds to the structure of the directory and the files in it.

import os
from pprint import pprint

def dir2dict(dp: str):
    ret_val = dict()
    for root, dirs, files in os.walk(dp, topdown=True):
        if len(root.split('/')) == 1:
            ret_val[root] = {'dirs': [], 'files': []}
            continue
        inner_dir = root.split('/')[1]
        outer_dir = root.split('/')[0]
        ret_val[outer_dir]['dirs'].append([inner_dir])
        print(ret_val)
    # dir = os.walk(dp, topdown=True)
    # print(next(dir))
    # print(next(dir))
    # print(next(dir))

dir2dict('dir_ex')
