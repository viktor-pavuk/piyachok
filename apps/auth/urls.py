from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import ActivateUserByEmailView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_tokens'),
    path('activate/<str:token>/', ActivateUserByEmailView.as_view(), name='auth_activate_user' )

]