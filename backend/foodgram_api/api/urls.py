from django.urls import include, path
from .views import (
    UserViewSet,
    RecipeViewSet,
    IngredientViewSet,
    TagViewSet,
)
from rest_framework.routers import DefaultRouter


router_api_v1 = DefaultRouter()
router_api_v1.register('users', UserViewSet, basename='users')
router_api_v1.register(r'recipes', RecipeViewSet)
router_api_v1.register(r'ingredients', IngredientViewSet)
router_api_v1.register(r'tags', TagViewSet)


urlpatterns = [
    path('', include(router_api_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
