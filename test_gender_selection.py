from page_one import PageOne
from page_two import PageTwo

# Test run
class TestClass:

    def test_gender_selection_female(self, driver):
        page_one = PageOne(driver)
        page_one.open_page()
        page_one.element_doll_base_female().click_element()
        page_two = PageTwo(driver)
        page_two.wait_page_stable()

    def test_gender_selection_male(self, driver):
        page_one = PageOne(driver)
        page_one.open_page()
        page_one.element_doll_base_male().click_element()
        page_two = PageTwo(driver)
        page_two.wait_page_stable()