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
        name = self.get_name_info()
        author = self.get_author_info()
        isbn = self.get_isbn_info()
        pages_count = self.get_pages_count_info()
        provider_id = self.get_provider_id_info()
        price = self.get_price_info().split(':')[1]
        description = self.get_description_info()

        return { 'name': name, 'author': author, 'isbn': isbn, 'pages_count': pages_count,
                'provider_id': provider_id, 'price': price, 'description': description }

    def get_name_info(self):
        element = self.driver.find_element(*MainPageLocators.BOOK_NAME)
        return element.text

    def get_author_info(self):
        elements = self.driver.find_elements(*MainPageLocators.INFO_BLOCKS)
        author = select_element("Автор:", elements)

        return author

    def get_isbn_info(self):
        elements = self.driver.find_elements(*MainPageLocators.INFO_BLOCKS)
        isbn = select_element("ISBN:", elements)

        return isbn

    def get_pages_count_info(self):
        elements = self.driver.find_elements(*MainPageLocators.INFO_BLOCKS)
        pages_count = select_element("Кол-во страниц:", elements)
        return pages_count

    def get_provider_id_info(self):
        elements = self.driver.find_elements(*MainPageLocators.INFO_BLOCKS)
        provider_id = select_element("ID поставщика:", elements)

        return provider_id

    def get_price_info(self):
        element = self.driver.find_element(*MainPageLocators.PRICE)
        return element.text

    def get_description_info(self):
        element = self.driver.find_element(*MainPageLocators.DESCRIPTION)
        return element.text

    def click_buy_button(self, parent):
        element = parent.find_element(*MainPageLocators.BUY_BUTTON)
        element.click()

    def get_price(self, parent):
        element = parent.find_element(*MainPageLocators.PRICE_BLOCK)
        return element

    def click_bucket(self):
        element = self.driver.find_element(*MainPageLocators.BUCKET)
        element.click()

    def get_item_count(self):
        element = self.driver.find_element(*MainPageLocators.ITEM_COUNT)
        return element

class BucketPage(BasePage):
    def get_price(self):
        element = self.driver.find_element(*BucketPageLocators.PRICE_BLOCK)
        return element

    def click_make_order_button(self):
        element = self.driver.find_element(*BucketPageLocators.MAKE_ORDER_BUTTON)
        element.click()

    def get_order_info_block(self):
        element = self.driver.find_element(*BucketPageLocators.ORDER_INFO_BLOCK)
        return  element

def select_element(substring, arr):
    for elem in arr:
        if substring in elem.text:

            text = clear_text(elem.text)
            return text

def clear_text(text):
    substr = text.split(':')[1]
    substr = substr.rstrip().lstrip()
    return substr
