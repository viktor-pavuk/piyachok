from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from utils.jwt_util import JwtUtils


class ActivateUserByEmailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtUtils.validate_token(token)
        user.is_active = True
        user.save()
        return Response('activated', status=status.HTTP_200_OK)