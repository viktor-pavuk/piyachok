from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from .models import UserModel as User

UserModel: User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id', 'is_active', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at'
        )

        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
