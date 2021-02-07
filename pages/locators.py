from selenium.webdriver.common.by import By


class MainYandexPageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible")


class SearchYandexPageLocators():
    SEARCH_RESULTS = (By.CSS_SELECTOR, "#search-result")
    LINK_RESULT = (By.CSS_SELECTOR, ".serp-item .organic .organic__subtitle .path .link")