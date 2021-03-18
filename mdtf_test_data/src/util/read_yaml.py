#!/usr/bin/python
""" mdtf_test_data yaml parsing utiltities """

import yaml
import pprint

def read_yaml():
    """ A function to read YAML file"""
    with open('config.yml') as f:
        config = yaml.safe_load(f)

    return config
