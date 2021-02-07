from webium import BasePage, Find
from pages.locators import ImagesMainPageLocators


class ImagesMainPage(BasePage):
    driver = None
    by, value = ImagesMainPageLocators.FIRST_POPULAR_ITEM
    first_popular_item = Find(by=by, value=value)
    by, value = ImagesMainPageLocators.FIRST_POPULAR_ITEM_NAME
    first_popular_item_name = Find(by=by, value=value)

    def __init__(self, driver):
        super(ImagesMainPage, self).__init__(driver=driver)
        self.driver = driver

    def should_be_correct_url(self):
        assert "https://yandex.ru/images/" in self.driver.current_url, "There is wrong url"

    def click_on_first_popular_item(self):
        assert self.is_element_present('first_popular_item', timeout=5), "there is no popular items here"
        self.first_popular_item.click()
        return self.first_popular_item_name.text