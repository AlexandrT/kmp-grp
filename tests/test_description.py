import pytest
import logging
import time

from config import settings
from fixtures import test_data
from utils import *
from support.assertions import *
import page

logger = logging.getLogger('public_api')

REQUEST_PATH = '/www/index.php'

class TestDescription:
    """Test description"""

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
        """of book"""
        selenium.get(f"{settings.MAIN_URL}{REQUEST_PATH}")

        main_page = page.MainPage(selenium)
        main_page.click_first_book()

        book_info = {}
        book_info = main_page.collect_book_info()

        expected = { 'name': test_data.NAME, 'author': test_data.AUTHOR, 'isbn':
                test_data.ISBN, 'pages_count': test_data.PAGES_COUNT,
                'provider_id': test_data.PROVIDER_ID, 'price': test_data.PRICE,
                'description': test_data.DESCRIPTION }

        assert_dict_equals(expected, book_info)
