#! /usr/bin/env python3
# coding: utf-8

from .Config.Loader import Loader as ConfigLoader

class WorkerConfigLoader(ConfigLoader):
    token: str
    
    def __init__(self, path):
        super().__init__(path)

        if "token" not in self.config:
            raise Exception("No token given in the configuration file !")
        else:
            self.token: str = self.config["token"]

