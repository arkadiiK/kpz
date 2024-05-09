from .api import TranslateAPI


class TranslationService:
    @staticmethod
    def translate_text(text):
        api_instance = TranslateAPI()
        result = api_instance.translate_to_minion(text)
        return result
