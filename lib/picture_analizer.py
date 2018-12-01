import re
from datetime import datetime
import os
import piexif
from PIL import Image


class PictureAnalyzer:

    def __init__(self, config):
        self.config = config

    def get_pictures(self):
        pictures = {}
        for path in self.config.get_paths():
            for root, dirs, files in os.walk(path, topdown=False):
                for f in files:
                    self._load_image(os.path.join(root, f))
        return pictures

    def _creation_date(self, path_to_file):
        c_time = os.path.getctime(path_to_file)
        m_time = os.path.getmtime(path_to_file)
        if m_time < c_time:
            return m_time
        return c_time

    def _load_image(self, path):
        if re.search(r"\.jpg|\.jpeg|\.JPG|\.JPEG", path):
            img = Image.open(path)
            print(img.info)
            if 'exif' in img.info:
                exif_dict = piexif.load(img.info['exif'])
                print(exif_dict)
            else:
                print(datetime.utcfromtimestamp(self._creation_date(path)))
