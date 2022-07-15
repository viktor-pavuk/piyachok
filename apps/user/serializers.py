import os

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from utils.email_util import EmailUtils

from ..profile.models import ProfileModel
from ..profile.serializers import ProfileSerializer
from .models import UserModel as User

UserModel: User = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'profile', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
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

    @transaction.atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        print(os.environ.get('EMAIL_HOST'))
        print(os.environ.get('EMAIL_HOST_USER'))
        print(os.environ.get('EMAIL_HOST_PASSWORD'))
        EmailUtils.register_email(user.email, user.profile.name)
        return user
