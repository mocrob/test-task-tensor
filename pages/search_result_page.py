from webium import BasePage, Find, Finds
from pages.locators import SearchYandexPageLocators


class YandexSearchPage(BasePage):
    by, value = SearchYandexPageLocators.SEARCH_RESULTS
    search_results = Find(by=by, value=value)
    by, value = SearchYandexPageLocators.LINK_RESULT
    links_results = Finds(by=by, value=value)

    def __init__(self, driver):
        super(YandexSearchPage, self).__init__(driver=driver)

    def should_be_search_results(self):
        assert self.is_element_present('search_results', timeout=5), "Here is no search results"

    def should_be_correct_link_in_five_first_results(self):
        result = False
        for i in range(6):
            if ("tensor.ru" in self.links_results[i].get_attribute("href")):
                result = True
                break
        assert result, "In first results no correct link"
