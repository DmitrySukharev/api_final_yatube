from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowListCreate, GroupViewSet, PostViewSet

router_1 = DefaultRouter()
router_1.register('v1/posts', PostViewSet)
router_1.register('v1/groups', GroupViewSet)
router_1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router_1.urls)),
    path('v1/follow/', FollowListCreate.as_view(), name='follow'),
    path('v1/', include('djoser.urls.jwt')),
]
