from webium import BasePage, Find
from pages.locators import MainYandexPageLocators
from selenium.webdriver.common.keys import Keys


class YandexMainPage(BasePage):
    by, value = MainYandexPageLocators.SUGGEST
    suggest = Find(by=by, value=value)
    by, value = MainYandexPageLocators.SEARCH_FIELD
    search_field = Find(by=by, value=value)
    by, value = MainYandexPageLocators.IMAGES_LINK
    images_link = Find(by=by, value=value)

    def __init__(self, driver):
        super(YandexMainPage, self).__init__(url='https://yandex.ru/', driver=driver)

    def should_be_search_field(self):
        assert self.is_element_present('search_field', timeout=5), "There is no search field here"

    def enter_sample_text_to_search_field(self):
        self.search_field.send_keys("Тензор")

    def should_be_suggest(self):
        assert self.is_element_present('suggest', timeout=5), "There is no suggest here"

    def press_enter_button(self):
        self.search_field.send_keys(Keys.ENTER)

    def should_be_images_link(self):
        assert self.is_element_present('images_link', timeout=5), "There is no images link here"

    def click_on_images_link(self):
        self.images_link.click()
