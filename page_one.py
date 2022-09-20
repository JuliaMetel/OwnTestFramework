from selenium.webdriver.common.by import By
from foundation_page import FoundationPage
from foundation_element import FoundationElement


class PageOne(FoundationPage):
    link = "https://webglsamples.org/collectibles/index.html"
    welcome_text = 'Welcome to Collectibles Painter'
    select_text = 'Select a model to begin'

    def __getattr__(self, attrname):
        if attrname == "element_doll_base_female":
            return self.element_doll_base_female()
        elif attrname == "element_doll_base_male":
            return self.element_doll_base_male()
        elif attrname == "element_loading_menu_welcome":
            return self.element_loading_menu_welcome()
        elif attrname == "element_loading_menu_select":
            return self.element_loading_menu_select()
        print(f'Атрибута {attrname} не существует!')
        raise AttributeError

    def element_doll_base_female(self):
        return FoundationElement((By.ID, 'dollbaseFemale'), self._driver)

    def element_doll_base_male(self):
        return FoundationElement((By.ID, 'dollbaseMale'), self._driver)

    def element_loading_menu_welcome(self):
        return FoundationElement((By.XPATH, "//*[@id='loadingMenu']/h4"), self._driver)

    def element_loading_menu_select(self):
        return FoundationElement((By.XPATH, "//*[@id='loadingMenu']/h2"), self._driver)
