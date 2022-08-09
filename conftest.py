import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    # Browser settings
    chrome_options = webdriver.ChromeOptions()

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.maximize_window()
        driver.implicitly_wait(10)

        yield driver

        driver.save_screenshot(request.node.name + '.png')