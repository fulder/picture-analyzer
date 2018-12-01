from datetime import datetime
import os
import piexif
from PIL import Image


def creation_date(path_to_file):
    c_time = os.path.getctime(path_to_file)
    m_time = os.path.getmtime(path_to_file)
    if m_time < c_time:
        return m_time
    return c_time

def load_image(path):
    img = Image.open(path)
    print(img.info)
    if 'exif' in img.info:
        exif_dict = piexif.load(img.info['exif'])
        print(exif_dict)
    else:
        print(datetime.utcfromtimestamp(creation_date(image_path_2)))


image_path = "\\\\freenas.local\\pictures\\Mama\\9 ROK 2018\\9. Wrzesien\\20180908_205414.jpg"
load_image(image_path)

print("--------------------------")

image_path_2 = "\\\\freenas.local\pictures\Mama\\1 Zdjecia dawne 2000-2004\\08.2000\\33.jpg"
load_image(image_path_2)
