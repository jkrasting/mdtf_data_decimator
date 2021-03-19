#!/usr/bin/python
""" mdtf_test_data yaml parsing utiltities """

import yaml
import pprint

def read_yaml(file_name):
    """ A function to read YAML file"""
    with open(file_name) as f:
        config = yaml.safe_load(f)
    return config
