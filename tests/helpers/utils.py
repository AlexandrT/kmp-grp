import i18n
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
