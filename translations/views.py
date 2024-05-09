from django.shortcuts import render
from django.views.generic import View

from services.translations import TranslationService


class TranslationsView(View):
    @staticmethod
    def get(request):
        return render(request, 'base.html')

    @staticmethod
    def post(request):
        input_text = request.POST.get('input-text', '')
        translation_service = TranslationService()
        translated_text = translation_service.translate_text(input_text)
        return render(request, 'base.html', {'translated_text': translated_text})
