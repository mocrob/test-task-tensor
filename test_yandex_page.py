import pytest
from pages.main_ya_page import YandexMainPage
from pages.search_result_page import YandexSearchPage


def test_user_can_use_search_function(browser):
    page = YandexMainPage(driver=browser)
    page.open()
    page.should_be_search_field()
    page.enter_sample_text_to_search_field()
    page.should_be_suggest()
    page.press_enter_button()
    page = YandexSearchPage(driver=browser)
    page.should_be_search_results()
    page.should_be_correct_link_in_five_first_results()