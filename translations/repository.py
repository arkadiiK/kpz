from .models import Translation


class TranslationRepository(Translation):
    @staticmethod
    def save_translations(original_text, translated_text):
        translation = Translation.objects.create(
            original_text=original_text,
            translated_text=translated_text,
        )
        return translation

    @staticmethod
    def get_translations_by_original(original_text):
        try:
            translations = Translation.objects.get(original_text=original_text)
            return translations
        except Translation.DoesNotExist:
            return None
