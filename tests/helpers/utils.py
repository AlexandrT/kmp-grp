import i18n
import re
import os

class KmpTranslator:
    def __init__(self):
        self.locale = i18n.config.get('locale')
        i18n.resource_loader.load_directory(os.path.join(os.path.dirname(__file__), '../support/translations'), self.locale)

    def get_translation(self, key, fix_link):
        result = i18n.translations.container[self.locale][key]

        if fix_link == True:
            result = add_domain(result)

        return result

def get_int(string):
    num = float(re.search(r'\d+\.?\d.', string).group())
    return num

def buy_book(page, num):
    elements = page.get_books_blocks()

    i = 0
    total_price = 0

    while i < num:
        #block = elements[i]
        block = elements[0]
        page.click_buy_button(block)
        price = get_int(page.get_price(block).text)
        total_price += price
        i += 1

    return total_price
