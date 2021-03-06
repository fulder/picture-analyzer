import logging
import ntpath
import re
from datetime import datetime
import os
from urllib import parse

import piexif
from PIL import Image

log = logging.getLogger("picture_analyzer")


class PictureAnalyzer:

    def __init__(self, config):
        self.config = config

    def get_pictures(self):
        pictures = {}
        for path in self.config.get_paths():
            for root, dirs, files in os.walk(path, topdown=False):
                for f in files:
                    img_path = os.path.join(root, f)
                    img_info = self._load_image(img_path)
                    if img_info is not None:
                        if img_info["date"] not in pictures:
                            pictures[img_info["date"]] = []
                        pictures[img_info["date"]].append(img_info)

        ret = {}
        for date in sorted(pictures):
            ret[date] = pictures[date]
        return pictures

    def _load_image(self, path):
        if re.search(r"\.jpg|\.jpeg|\.JPG|\.JPEG", path):
            img = Image.open(path)
            if 'exif' in img.info:
                exif_dict = piexif.load(img.info['exif'])
                exif_date = exif_dict["0th"][piexif.ImageIFD.DateTime].decode("utf-8")
                thumb_path = os.path.abspath(os.path.join(".thumbs", ntpath.basename(path)))
                if exif_dict["thumbnail"]:
                    if not os.path.isdir(".thumbs"):
                        os.mkdir(".thumbs")

                    thumbnail = exif_dict["thumbnail"]
                    with open(thumb_path, "wb+") as f:
                        f.write(thumbnail)
                return {"date": datetime.strptime(exif_date, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d"),
                        "path": "file:///" + path,
                        "thumb_path": "file:///" + thumb_path}
            else:
                return {"date": self._creation_date(path),
                        "path": "file:///" + path}
        else:
            log.warning("Couldn't load: {}".format(path))

    def _creation_date(self, path_to_file):
        c_time = os.path.getctime(path_to_file)
        m_time = os.path.getmtime(path_to_file)
        if m_time < c_time:
            return datetime.utcfromtimestamp(m_time).strftime("%Y-%m-%d")
        return datetime.utcfromtimestamp(c_time).strftime("%Y-%m-%d")
