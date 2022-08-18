from foundation_page import FoundationPage
from foundation_element import FoundationElement


class PageOne(FoundationPage):
    link = "https://webglsamples.org/collectibles/index.html"
    def element_doll_base_female(self):
        return FoundationElement(('id', 'dollbaseFemale'), self._driver)
    def element_doll_base_male(self):
        return FoundationElement(('id', 'dollbaseMale'), self._driver)
