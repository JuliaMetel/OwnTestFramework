class FoundationElement():
    def __init__(self, locator, driver):
        self.__element = driver.find_element(*locator)

    def click_element(self):
        self.__element.click()