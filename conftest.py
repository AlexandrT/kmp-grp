import sys
import os
import pytest
import logging

sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from config import set_env

LOG_NAME = 'test.log'

logging.basicConfig(filename=LOG_NAME,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filemode='w')

logger = logging.getLogger('public_api')

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

# def pytest_addoption(parser):
    # parser.addoption("--skip-mock", action="store_true",  default=False, help="skip mock-tests")

# def pytest_collection_modifyitems(config, items):
    # if not config.getoption("--skip-mock"):
        # return

    # skip_mock = pytest.mark.skip(reason="get rid --skip-mock option to run")

    # for item in items:
        # if "skip_mock" in item.keywords:
            # item.add_marker(skip_mock)

logger.info(f"Tests runs on the {set_env()} environment")
