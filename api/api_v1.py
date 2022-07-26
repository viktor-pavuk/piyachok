from django.urls import include, path

urlpatterns = [
    path('users/', include('apps.user.urls')),
    path('auth/', include('apps.auth.urls'))
]