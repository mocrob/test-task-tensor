from webium import BasePage, Find, Finds
from pages.locators import MainYandexPageLocators
from selenium.webdriver.common.keys import Keys


class YandexMainPage(BasePage):
    by, value = MainYandexPageLocators.SUGGEST
    suggest = Find(by=by, value=value)
    by, value = MainYandexPageLocators.SEARCH_FIELD
    search_field = Find(by=by, value=value)

    def __init__(self, driver):
        super(YandexMainPage, self).__init__(url='https://yandex.ru/', driver=driver)

    def should_be_search_field(self):
        assert self.is_element_present('search_field', timeout=5), "Here is no search field"

    def enter_sample_text_to_search_field(self):
        self.search_field.send_keys("Тензор")

    def should_be_suggest(self):
        assert self.is_element_present('suggest', timeout=5), "Here is no suggest"

    def press_enter_button(self):
        self.search_field.send_keys(Keys.ENTER)
