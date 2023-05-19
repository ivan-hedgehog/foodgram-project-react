from django.shortcuts import render
from rest_framework import generics
from recipes.models import Recipe
from .serializers import RecipeSerializer, IngredientSerializer, TagSerializer
from rest_framework import permissions, status, mixins, viewsets, filters
from .mixins import ListRetrieveViewSet
from recipes.models import Ingredient, Tag, Recipe  # , Title


class IngredientViewSet(ListRetrieveViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(ListRetrieveViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RecipeViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
