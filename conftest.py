import pytest
from selenium import webdriver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_run_test_make_report(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def driver(request):
    # Browser settings
    chrome_options = webdriver.ChromeOptions()

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.maximize_window()
        driver.implicitly_wait(10)

        yield driver

        if request.node.rep_call.failed:
            driver.save_screenshot(request.node.name + '.png')