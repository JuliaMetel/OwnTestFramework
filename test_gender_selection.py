import time
import io
import pytest
from PIL import Image, ImageChops
from selenium import webdriver


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


@pytest.fixture
def driver(request):
    # Browser settings
    chrome_options = webdriver.ChromeOptions()

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.maximize_window()
        driver.implicitly_wait(10)

        yield driver

        driver.save_screenshot(request.node.name + '.png')


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
