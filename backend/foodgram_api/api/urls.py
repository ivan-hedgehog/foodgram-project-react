from django.urls import path
from .views import RecipeAPIView

urlpatterns = [
    path('v1/recipelist/', RecipeAPIView.as_view()),
]