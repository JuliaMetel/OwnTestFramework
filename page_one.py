from selenium.webdriver.common.by import By
from foundation_page import FoundationPage
from foundation_element import FoundationElement


class PageOne(FoundationPage):
    link = "https://webglsamples.org/collectibles/index.html"
    welcome_text = 'Welcome to Collectibles Painter'
    select_text = 'Select a model to begin'

    @property
    def element_doll_base_female(self):
        return FoundationElement((By.ID, 'dollbaseFemale'), self._driver)

    @property
    def element_doll_base_male(self):
        return FoundationElement((By.ID, 'dollbaseMale'), self._driver)

    @property
    def element_loading_menu_welcome(self):
        return FoundationElement((By.XPATH, "//*[@id='loadingMenu']/h4"), self._driver)

    @property
    def element_loading_menu_select(self):
        return FoundationElement((By.XPATH, "//*[@id='loadingMenu']/h2"), self._driver)
