from django.shortcuts import render
from rest_framework import generics
from recipes.models import Recipe
from .serializers import RecipeSerializer



class RecipeAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer