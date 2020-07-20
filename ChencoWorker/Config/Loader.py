#! /usr/bin/env python3
# coding: utf-8

import json


class Loader:

    def __init__(self, path):
        try:
            with open(path, 'r') as fileReader:
                self.config = json.loads(fileReader.read())
        except FileNotFoundError:
            raise FileNotFoundError