from webium import BasePage, Find
from pages.locators import ImagesSearchResultLocators


class ImagesSearchResultPage(BasePage):
    search_text = None
    driver = None

    by, value = ImagesSearchResultLocators.SEARCH_FIELD_TEXT
    search_field_text = Find(by=by, value=value)
    by, value = ImagesSearchResultLocators.FIRST_IMAGE
    first_image = Find(by=by, value=value)

    def __init__(self, driver, search_text):
        super(ImagesSearchResultPage, self).__init__(driver=driver)
        self.search_text = search_text
        self.driver = driver

    def should_equals_search_texts(self):
        assert self.is_element_present('search_field_text', timeout=5), "There is no search field here"
        assert self.search_text == self.search_field_text.get_attribute("value"), "Wrong text in search field"

    def click_on_first_image(self):
        assert self.is_element_present('first_image', timeout=5), "There is no images here"
        self.first_image.click()
