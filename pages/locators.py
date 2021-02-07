from selenium.webdriver.common.by import By


class MainYandexPageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible")
    IMAGES_LINK = (By.CSS_SELECTOR, '[data-id="images"]')


class SearchYandexPageLocators():
    SEARCH_RESULTS = (By.CSS_SELECTOR, "#search-result")
    LINK_RESULT = (By.CSS_SELECTOR, ".serp-item .organic .organic__subtitle .path .link")


class ImagesMainPageLocators():
    FIRST_POPULAR_ITEM = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")
    FIRST_POPULAR_ITEM_NAME = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 .PopularRequestList-SearchText")


class ImagesSearchResultLocators():
    SEARCH_FIELD_TEXT = (By.CSS_SELECTOR, ".input__box .input__control")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item_pos_0")


class FullImagePageLocators():
    FULL_IMAGE = (By.CSS_SELECTOR, "img.MMImage-Origin")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")
    PREV_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")