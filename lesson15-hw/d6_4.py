# Implement a function json2csv() - the opposite of the previous exercise.
# This time the function gets the path of the json file
# (you can assume that the file is actually a list of not nested objects) and creates a corresponding csv file.
import os
import json
from csv import DictWriter


def json2csv(fp: str, csv_path: str):
    if not os.path.exists(fp) or not os.path.exists(csv_path):
        raise Exception('Invalid path provided')
    if os.path.splitext(fp)[1] != '.json':
        raise Exception('Non-JSON file provided')

    with open(fp, 'r') as j:
        file_list = json.load(j)
        fieldnames = list(file_list[0].keys())

    with open(os.path.join(csv_path, 'd6_4.csv'), 'w', newline='') as f:
        writer = DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(file_list)
        print('CSV file created')


if __name__ == '__main__':
    json2csv('./files/d6_3.json', './files')
