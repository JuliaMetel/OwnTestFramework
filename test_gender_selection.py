from page_one import PageOne
from page_two import PageTwo

# Test run
class TestClass:

    def test_gender_selection_female(self, driver):
        page_one = PageOne()
        page_one.open_page(driver, page_one.link)
        page_one.element_doll_base_female(driver).click_element()
        page_two = PageTwo()
        page_two.wait_page_stable(driver)

    def test_gender_selection_male(self, driver):
        page_one = PageOne()
        page_one.open_page(driver, page_one.link)
        page_one.element_doll_base_male(driver).click_element()
        page_two = PageTwo()
        page_two.wait_page_stable(driver)
