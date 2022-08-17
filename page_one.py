from foundation_page import FoundationPage
from foundation_element import FoundationElement


class PageOne(FoundationPage):
    link = "https://webglsamples.org/collectibles/index.html"
    def element_doll_base_female(self, driver):
        return FoundationElement(('id', 'dollbaseFemale'), driver)
    def element_doll_base_male(self, driver):
        return FoundationElement(('id', 'dollbaseMale'), driver)
