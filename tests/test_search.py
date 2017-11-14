import pytest
import logging
import time

from config import settings
from utils import *
import page

logger = logging.getLogger('public_api')

REQUEST_PATH = '/www/index.php'

class TestSearch:
    """Test search"""

    def setup_class(cls):
        cls.translator = KmpTranslator()
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_by_name(self, selenium):
        """by name should be result"""
        selenium.get(f"{settings.MAIN_URL}{REQUEST_PATH}")

        main_page = page.MainPage(selenium)
        main_page.search_book_element = "Король лис"
        main_page.click_search_button()

        time.sleep(2)

        books = main_page.get_books_count()

        assert books == 1
