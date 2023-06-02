from api.views import (CustomUserViewSet, IngredientViewSet, RecipeViewSet,
                       TagViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_api_v1 = DefaultRouter()
router_api_v1.register('users', CustomUserViewSet, basename='users')
router_api_v1.register(r'recipes', RecipeViewSet)
router_api_v1.register(r'ingredients', IngredientViewSet)
router_api_v1.register(r'tags', TagViewSet)


urlpatterns = [
    path('', include(router_api_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
