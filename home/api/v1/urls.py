from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserSignupViewSets, LoginViewSet, BlogViewSet, CommentViewSet


router = DefaultRouter()
router.register('users', UserSignupViewSets, basename='users')
router.register('login', LoginViewSet, basename='login')
router.register('blogs', BlogViewSet, basename='blogs')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
