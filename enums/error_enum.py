from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = ('Token is invalid or expired', status.HTTP_400_BAD_REQUEST)

    def __int__(self, msg, code= status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.code = code