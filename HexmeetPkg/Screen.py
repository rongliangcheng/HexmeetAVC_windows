from time import sleep
from PIL import ImageGrab
import allure
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class CaptureScreen:

    @staticmethod
    def capture_screen(pic_name, _bbox=(645, 316, 1918, 1072)):
        im = ImageGrab.grab(bbox=_bbox)
        im.save(pic_name, "jpeg")

    @staticmethod
    def attach_pic(pic_name, description):
        with open(pic_name, mode='rb') as f:
            file = f.read()
            allure.attach(file, description, allure.attachment_type.PNG)

    @staticmethod
    def capture_attach_pic(pic_name, description, _bbox=(645, 316, 1918, 1072)):
        im = ImageGrab.grab(bbox=_bbox)
        im.save(pic_name, "png")
        sleep(1)
        with open(pic_name, mode='rb') as f:
            file = f.read()
            allure.attach(file, description, allure.attachment_type.PNG)


if __name__ == '__main__':
    sleep(3)
    bbox = (0, 0, 2560, 1440)
    CaptureScreen().capture_screen("../pics/test.png")
    CaptureScreen().capture_screen("test1.png", bbox)
