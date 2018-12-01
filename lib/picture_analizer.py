from datetime import datetime
import os
import piexif
from PIL import Image

class PictureAnalyzer:

    def creation_date(self, path_to_file):
        c_time = os.path.getctime(path_to_file)
        m_time = os.path.getmtime(path_to_file)
        if m_time < c_time:
            return m_time
        return c_time

    def load_image(self, path):
        img = Image.open(path)
        print(img.info)
        if 'exif' in img.info:
            exif_dict = piexif.load(img.info['exif'])
            print(exif_dict)
        else:
            print(datetime.utcfromtimestamp(self.creation_date(path)))
