import time
import os
import pytest
from PIL import Image, ImageChops
from selenium import webdriver


def is_images_equal(img1, img2):
    image_1 = Image.open(img1).convert('RGB')
    image_2 = Image.open(img2).convert('RGB')
    result = ImageChops.difference(image_1, image_2).getbbox()
    if result is None:
        return True
    return False

@pytest.fixture
def driver():
    # Browser settings
    chrome_options = webdriver.ChromeOptions()

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.maximize_window()
        driver.implicitly_wait(10)

        yield driver


# Test run
class TestClass:

    def test_gender_selection_female(self, driver):
        driver.get("https://webglsamples.org/collectibles/index.html")
        driver.find_element('id', 'dollbaseFemale').click()
        test_path = 'test_gender_selection_female_test.png'
        driver.save_screenshot(test_path)
        for x in range(10):
            time.sleep(0.1)
            path = 'test_gender_selection_female.png'
            driver.save_screenshot(path)
            if is_images_equal(test_path, path):
                break
            driver.save_screenshot(test_path)
        os.remove(test_path)

    def test_gender_selection_male(self, driver):
        driver.get("https://webglsamples.org/collectibles/index.html")
        driver.find_element('id', 'dollbaseMale').click()
        test_path = 'test_gender_selection_male_test.png'
        driver.save_screenshot(test_path)
        for x in range(10):
            time.sleep(0.1)
            path = 'test_gender_selection_male.png'
            driver.save_screenshot(path)
            if is_images_equal(test_path, path):
                break
            driver.save_screenshot(test_path)
        os.remove(test_path)

