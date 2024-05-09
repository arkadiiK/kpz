from django.urls import path
from .views import TranslationsView

urlpatterns = [
    path('', TranslationsView.as_view(), name='translations')
]
