from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from .serializers import UserSerializer

UserModel = get_user_model()

class UserListCreateAPIView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer