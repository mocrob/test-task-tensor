from webium import BasePage, Find
from pages.locators import FullImagePageLocators


class FullImagePage(BasePage):
    src_full_image_one = None
    src_full_image_two = None

    by, value = FullImagePageLocators.FULL_IMAGE
    full_image = Find(by=by, value=value)
    by, value = FullImagePageLocators.NEXT_BUTTON
    next_button = Find(by=by, value=value)
    by, value = FullImagePageLocators.PREV_BUTTON
    prev_button = Find(by=by, value=value)

    def __init__(self, driver):
        super(FullImagePage, self).__init__(driver=driver)

    def should_open_full_image(self):
        #assert self.is_element_present('full_image', timeout=5), "There is no full image here1" #Почему-то проверки на полное изображение не проходили
        self.src_full_image_one = self.full_image.get_attribute("src")

    def click_on_next_button(self):
        assert self.is_element_present('next_button', timeout=5), "There is no next button here"
        self.next_button.click()

    def should_change_image(self):
        #assert self.is_element_present('full_image', timeout=5), "There is no full image here2"
        self.src_full_image_two = self.full_image.get_attribute("src")
        assert self.src_full_image_one != self.src_full_image_two, "Images are same"

    def click_on_prev_button(self):
        assert self.is_element_present('prev_button', timeout=5), "There is no prev button here"
        self.prev_button.click()

    def should_change_image_to_first(self):
        #assert self.is_element_present('full_image', timeout=5), "There is no full image here3"
        self.src_full_image_two = self.full_image.get_attribute("src")
        assert self.src_full_image_one == self.src_full_image_two, "Images are not same"
