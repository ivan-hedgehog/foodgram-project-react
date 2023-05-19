from django.urls import include, path
from .views import RecipeViewSet, IngredientViewSet, TagViewSet
from rest_framework.routers import SimpleRouter


router_api = SimpleRouter()
router_api.register(r'recipes', RecipeViewSet)
router_api.register(r'ingredients', IngredientViewSet)
router_api.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router_api.urls)),
]


# router_api_v1.register('posts', PostViewSet, basename='posts')
# router_api_v1.register('groups', GroupViewSet, basename='groups')
# router_api_v1.register(
#     r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
# )

# urlpatterns = [
#     path('v1/', include(router_api_v1.urls)),
#     path('v1/', include('djoser.urls')),
#     path('v1/', include('djoser.urls.jwt')),
#     path('v1/follow/', FollowList.as_view()),
# ]
