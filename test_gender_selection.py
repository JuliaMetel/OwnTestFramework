import time
import io
from PIL import Image, ImageChops

def is_images_equal(img1, img2):
    image_1 = Image.open(io.BytesIO(img1)).convert('RGB')
    image_2 = Image.open(io.BytesIO(img2)).convert('RGB')
    result = ImageChops.difference(image_1, image_2).getbbox()
    if result is None:
        return True
    return False


def wait_page_stable(driver):
    image_1 = driver.get_screenshot_as_png()
    for x in range(5):
        image_2 = driver.get_screenshot_as_png()
        if is_images_equal(image_1, image_2):
            break
        time.sleep(0.01)
        image_1 = driver.get_screenshot_as_png()


# Test run
class TestClass:

    def test_gender_selection_female(self, driver):
        driver.get("https://webglsamples.org/collectibles/index.html")
        driver.find_element('id', 'dollbaseFemale').click()
        wait_page_stable(driver)

    def test_gender_selection_male(self, driver):
        driver.get("https://webglsamples.org/collectibles/index.html")
        driver.find_element('id', 'dollbaseMale').click()
        wait_page_stable(driver)
