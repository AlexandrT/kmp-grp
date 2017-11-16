import os
import importlib

class TestData():
    def __init__(self):
        self.MODULE = 'test_data'

        mod = importlib.import_module(self.MODULE)

        self._explicit_items = set()
        for item in dir(mod):
            if item.isupper():
                item_value = getattr(mod, item)

                setattr(self, item, item_value)
                self._explicit_items.add(item)

    def __repr__(self):
        return '<%(cls)s>' % {
            'cls': self.__class__.__name__,
        }

test_data = TestData()
