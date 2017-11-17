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

class TestOrder:
    """Test order"""

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

    @pytest.mark.parametrize("num", [
        (1),
        (4),
        ])
    def test_without_sale(self, selenium, num):
        """without sale"""
        selenium.get(f"{settings.MAIN_URL}{REQUEST_PATH}")

        main_page = page.MainPage(selenium)
        num = 1

        expected_price = buy_book(main_page, num)
        item_count = int(main_page.get_item_count().text)

        assert num == item_count

        main_page.click_bucket()

        bucket_page = page.BucketPage(selenium)
        price = get_int(bucket_page.get_price().text)

        assert expected_price == price

    @pytest.mark.parametrize("num", [
        (5),
        (6),
        ])
    def test_sale(self, selenium, num):
        """with sale"""
        selenium.get(f"{settings.MAIN_URL}{REQUEST_PATH}")

        main_page = page.MainPage(selenium)

        expected_price = buy_book(main_page, num)
        item_count = int(main_page.get_item_count().text)

        assert num == item_count

        main_page.click_bucket()

        bucket_page = page.BucketPage(selenium)
        price = get_int(bucket_page.get_price().text)
        expected_price *= 0.9

        assert expected_price == price
