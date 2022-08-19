import time
from utils import is_images_equal
from exception import PageWithoutLinkException


class FoundationPage():

    def __init__(self, driver):
        self._driver = driver

    def wait_page_stable(self):
        image_1 = self._driver.get_screenshot_as_png()
        for x in range(5):
            image_2 = self._driver.get_screenshot_as_png()
            if is_images_equal(image_1, image_2):
                break
            time.sleep(0.01)
            image_1 = self._driver.get_screenshot_as_png()

    def open_page(self):
        if hasattr(self, 'link'):
            self._driver.get(self.link)
        else:
            raise PageWithoutLinkException('Class PageOne do not have attribute \'link\'')