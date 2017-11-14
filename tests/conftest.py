import sys
import os
import i18n
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

i18n.load_path.append(os.path.join(os.path.dirname(__file__), '../support/translations'))
i18n.set('locale', 'ru')

pytest_plugins = ['common_fixtures']
