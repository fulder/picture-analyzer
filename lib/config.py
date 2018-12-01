import pyyaml

class Config:

    def __init__(self):
        self.paths = []

    def add_path(self, path):
        self.paths.append(path)

