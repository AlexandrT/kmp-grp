from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_BUTTON = (By.XPATH, '//input[@name="search"]/following-sibling::span')
    BOOK_BLOCK = (By.XPATH, '//div[@data-bookid]')

    BOOK_NAME = (By.XPATH, '//h2')
    INFO_BLOCKS = (By.XPATH, '//p[b]')
    PRICE = (By.XPATH, '//p[@class="price"]')
    DESCRIPTION = (By.XPATH, '//p[@class="price"]/following-sibling::p')

    BUY_BUTTON = (By.XPATH, './/button[@class="buy"]')
    PRICE_BLOCK = (By.XPATH, './/div[@class="price"]')

    BUCKET = (By.XPATH, '//i[@class="fi fi-cart"]')
    ITEM_COUNT = (By.XPATH, '//sup[@class="itemcount"]')

class BucketPageLocators(object):
    PRICE_BLOCK = (By.XPATH, '//div[@class="total"]')
    MAKE_ORDER_BUTTON = (By.XPATH, '//div[@class="makeorder"]/button')
