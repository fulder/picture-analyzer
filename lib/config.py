import logging
import os

import yaml

log = logging.getLogger("config")

class Config:

    def __init__(self):
        self.config_path = "config.yaml"
        self.config = {}
        self._load_config()

    def add_path(self, path):
        log.debug("Adding path: {}".format(path))
        if "paths" not in self.config:
            self.config["paths"] = []
        self.config["paths"].append(path)
        self._save_config()

    def get_paths(self):
        if "paths" in self.config:
            return self.config["paths"]
        return []

    def _save_config(self):
        with open(self.config_path, 'w') as config_file:
            yaml.dump(self.config, config_file, default_flow_style=False)

    def _load_config(self):
        if os.path.isfile(self.config_path):
            with open(self.config_path, 'r') as config_file:
                self.config = yaml.load(config_file)
