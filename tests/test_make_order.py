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

class TestMakeOrder:
    """Test"""

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
        ])
    def test_make_one(self, selenium, num):
        """make one order"""
        selenium.get(f"{settings.MAIN_URL}{REQUEST_PATH}")

        main_page = page.MainPage(selenium)
        num = 1

        expected_price = buy_book(main_page, num)
        main_page.click_bucket()

        bucket_page = page.BucketPage(selenium)
        bucket_page.click_make_order_button()

        order_number = get_int(bucket_page.get_order_info_block().text)

        assert order_number == num

        main_page.click_bucket()

        number_from_history = int(bucket_page.get_order_from_history().get_attribute('data-orderid'))

        assert num == number_from_history
