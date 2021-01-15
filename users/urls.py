from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import AuthPost, UserViewSet

router = DefaultRouter()

urlpatterns = [
    path('v1/auth/email/', AuthPost.as_view(), name='email_confirmation'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router.register(
    r'users',
    UserViewSet,
    basename='users'
)
urlpatterns += [
    path('v1/', include(router.urls)),
]