from django.urls import path
from .views import BaseRegisterView

urlpatterns = [
    path('', BaseRegisterView.as_view()),
]