# django
from django.urls import path

# Views
from .views import CardValidation

app_name = 'card_validation'

urlpatterns = [
    path('card_validation', CardValidation, name='card_validation')
]