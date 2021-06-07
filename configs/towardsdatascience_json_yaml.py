# https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

import json
from pprint import pprint

import yaml


def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def read_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


assert read_json('sample.json') == read_yaml('sample.yaml')

print('json')
pprint(read_json('sample.json'))
print('yaml')
pprint(read_yaml('sample.yaml'))
