from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_BUTTON = (By.XPATH, '//input[@name="search"]/following-sibling::span')
    BOOK_BLOCK = (By.XPATH, '//div[@data-bookid]')
