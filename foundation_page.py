import time
from utils import is_images_equal

class FoundationPage():
    def wait_page_stable(self, driver):
        image_1 = driver.get_screenshot_as_png()
        for x in range(5):
            image_2 = driver.get_screenshot_as_png()
            if is_images_equal(image_1, image_2):
                break
            time.sleep(0.01)
            image_1 = driver.get_screenshot_as_png()

    def open_page(self, driver, link):
        driver.get(link)