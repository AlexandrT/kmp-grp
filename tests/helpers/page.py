from locators import *
from elements import *

class SearchBookElement(BasePageElement):
    locator = 'search'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    search_book_element = SearchBookElement()

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

    def get_books_blocks(self):
        elements = self.driver.find_elements(*MainPageLocators.BOOK_BLOCK)
        return elements

    def get_books_count(self):
        books = self.get_books_blocks()
        return len(books)
