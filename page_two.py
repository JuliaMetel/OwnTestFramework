import time
from PIL import Image
from utils import is_images_equal
from foundation_page import FoundationPage
from selenium.webdriver.common.by import By
from foundation_element import FoundationElement


class PageTwo(FoundationPage):
    def element_canvas(self):
        return FoundationElement((By.ID, 'canvas'), self._driver)

    def element_eye(self):
        return FoundationElement((By.ID, 'eye'), self._driver)

    def element_head_1(self):
        return FoundationElement((By.ID, 'head_1'), self._driver)

    def is_canvas_equal(self, link):
        canvas_rect = self.element_canvas().get_rect()
        for x in range(5):
            image_1 = self.create_screenshot_by_coordinates(canvas_rect)
            if is_images_equal(image_1, Image.open(link)):
                return True
            time.sleep(0.01)
        else:
            return False




