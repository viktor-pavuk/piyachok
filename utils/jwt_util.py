from datetime import timedelta

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import Token, BlacklistMixin

from enums.token_enum import TokenEnum
from exceptions.jwt_exception import JwtException

UserModel = get_user_model()


class ActionToken(BlacklistMixin, Token):
    token_type = TokenEnum.ACTIVATION.token_type
    lifetime = TokenEnum.ACTIVATION.exp_time


class JwtUtils:
    @staticmethod
    def create_token(user):
        return ActionToken.for_user(user)

    @staticmethod
    def validate_token(token: str):
        try:
            action_token = ActionToken(token)
            action_token.check_blacklist()
        except Exception:
            raise JwtException
        action_token.blacklist()
        user_id = action_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
