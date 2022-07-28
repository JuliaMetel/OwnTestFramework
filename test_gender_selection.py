import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture
def driver():
    # Browser settings
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--auto-open-devtools-for-tabs')

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.maximize_window()
        driver.implicitly_wait(3)

        yield driver


# Test run
class TestClass:
    def test_gender_selection_female(self, driver):
        driver.get("https://webglsamples.org/collectibles/index.html")
        elem = driver.find_element('id', 'dollbaseFemale')
        elem.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(('id', 'canvas')))


    def test_gender_selection_male(self, driver):
        driver.get("https://webglsamples.org/collectibles/index.html")
        elem = driver.find_element('id', 'dollbaseMale')
        elem.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(('id', 'canvas')))