# https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

import json

import pytest

from configs.towardsdatascience_json_yaml import read_json, read_yaml


def test_validation_json():
    with pytest.raises(FileNotFoundError):
        read_json(file_path="sample_error.json")

    with pytest.raises(json.decoder.JSONDecodeError):
        # only show the first error
        # read_json(file_path="sample.json")
        read_json(file_path="sample.yaml")


def test_validation_yaml():
    with pytest.raises(FileNotFoundError):
        read_yaml(file_path="sample_error.yaml")
