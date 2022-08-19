from utils import check_text_equal
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

    def test_loading_menu_header_welcome(self, driver):
        page_one = PageOne(driver)
        page_one.open_page()
        check_text_equal(page_one.element_loading_menu_welcome().get_text(), page_one.welcome_text)

    def test_loading_menu_header_select(self, driver):
        page_one = PageOne(driver)
        page_one.open_page()
        check_text_equal(page_one.element_loading_menu_select().get_text(), page_one.select_text)



