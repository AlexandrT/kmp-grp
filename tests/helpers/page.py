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

    def click_first_book(self):
        books = self.get_books_blocks()
        books[0].click()

    def collect_book_info(self):
        name = self.get_name()
        author = self.get_author()
        isbn = self.get_isbn()
        pages_count = self.get_pages_count()
        provider_id = self.get_provider_id()
        price = self.get_price().split(':')[1]
        description = self.get_description()

        return { 'name': name, 'author': author, 'isbn': isbn, 'pages_count': pages_count,
                'provider_id': provider_id, 'price': price, 'description': description }

    def get_name(self):
        element = self.driver.find_element(*MainPageLocators.BOOK_NAME)
        return element.text

    def get_author(self):
        elements = self.driver.find_elements(*MainPageLocators.INFO_BLOCKS)
        author = select_element("Автор:", elements)

        return author

    def get_isbn(self):
        elements = self.driver.find_elements(*MainPageLocators.INFO_BLOCKS)
        isbn = select_element("ISBN:", elements)

        return isbn

    def get_pages_count(self):
        elements = self.driver.find_elements(*MainPageLocators.INFO_BLOCKS)
        pages_count = select_element("Кол-во страниц:", elements)
        return pages_count

    def get_provider_id(self):
        elements = self.driver.find_elements(*MainPageLocators.INFO_BLOCKS)
        provider_id = select_element("ID поставщика:", elements)

        return provider_id

    def get_price(self):
        element = self.driver.find_element(*MainPageLocators.PRICE)
        return element.text

    def get_description(self):
        element = self.driver.find_element(*MainPageLocators.DESCRIPTION)
        return element.text

def select_element(substring, arr):
    for elem in arr:
        if substring in elem.text:

            text = clear_text(elem.text)
            return text

def clear_text(text):
    substr = text.split(':')[1]
    substr = substr.rstrip().lstrip()
    return substr
