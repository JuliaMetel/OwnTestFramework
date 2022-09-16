class FoundationElement():
    def __init__(self, locator, driver):
        self.__element = driver.find_element(*locator)

    def click_element(self):
        self.__element.click()

    def get_text(self):
        return self.__element.text

    def get_rect(self):
        # Multiply by 2 with testing on Mac
        element_rect = self.__element.rect
        element_rect['x'] = element_rect['x'] * 2
        element_rect['y'] = element_rect['y'] * 2
        element_rect['width'] = element_rect['width'] * 2
        element_rect['height'] = element_rect['height'] * 2
        return element_rect

