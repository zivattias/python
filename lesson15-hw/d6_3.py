# Implement a function csv2json().
# The function receives a file_path of csv file and file_path of a new json file that will be created by a function.
# The function should read x§the original csv file, convert the data in it into json,
# and store the contents of the csv file as a json file that contains a list of objects.

import os
import json
from csv import DictReader


def csv2json(fp: str, json_path: str):
    if not os.path.exists(fp) or not os.path.exists(json_path):
        raise Exception('Invalid path provided')
    if os.path.splitext(fp)[1] != '.csv':
        raise Exception('Non-CSV file given')
    with open(fp, 'r') as f:
        file_list = list(DictReader(f))
        with open(os.path.join(json_path, 'd6_3.json'), 'w') as j:
            json.dump(file_list, j)
            print('File created')


if __name__ == '__main__':
    csv2json('./files/d6_3.csv', './files')
