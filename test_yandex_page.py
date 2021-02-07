import pytest
from pages.main_ya_page import YandexMainPage
from pages.search_result_page import YandexSearchPage
from pages.images_main_page import ImagesMainPage
from pages.images_search_result_page import ImagesSearchResultPage
from pages.full_image_page import FullImagePage


@pytest.mark.search
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


@pytest.mark.images
def test_user_can_use_image_function(browser):
    page = YandexMainPage(driver=browser)
    page.open()
    page.should_be_images_link()
    page.click_on_images_link()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    page = ImagesMainPage(driver=browser)
    page.should_be_correct_url()
    text = page.click_on_first_popular_item()
    page = ImagesSearchResultPage(driver=browser, search_text=text)
    page.should_equals_search_texts()
    page.click_on_first_image()
    page = FullImagePage(driver=browser)
    page.should_open_full_image()
    page.click_on_next_button()
    page.should_change_image()
    page.click_on_prev_button()
    page.should_change_image_to_first()