from locator import MainPageLocator

from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"


class Basepage(object):

    def __init__(self, driver):
        self.driver = driver


class Mainpage(Basepage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocator.GO_BUTTON)
        element.click()


class SearchResultPage(Basepage):

    def is_result_found(self):
        return "No results found." not in self.driver.page_source


# *(1,2)
# This means unpack the object
# 1 , 2
#Can pass it as an argument
