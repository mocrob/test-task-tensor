from webium import BasePage, Find, Finds
from pages.locators import SearchYandexPageLocators
from selenium.webdriver.remote.webelement import WebElement


class Link(WebElement):
    def is_contain_correct_link(self):
        return self.get_attribute('href').find('tensor.ru') != -1


class YandexSearchPage(BasePage):
    by, value = SearchYandexPageLocators.SEARCH_RESULTS
    search_results = Find(by=by, value=value)
    by, value = SearchYandexPageLocators.LINK_RESULT
    links_results = Finds(Link, by=by, value=value)

    def __init__(self, driver):
        super(YandexSearchPage, self).__init__(driver=driver)

    def should_be_search_results(self):
        assert self.is_element_present('search_results', timeout=5), "There is no search results here"

    def should_be_correct_link_in_five_first_results(self):
        results = list(filter(lambda link: link.is_contain_correct_link(), self.links_results[0:5]))
        assert len(results) > 0, "In first results no correct link"

