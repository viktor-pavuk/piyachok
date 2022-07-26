from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_error_handler(exc: Exception, content) -> Response:
    handlers = {
        'JwtException': _jwt_validate_error
    }
    response = exception_handler(exc, content)
    exc_class = exc.__class__.__name__

    if exc_class in handlers:
        function = handlers[exc_class]
        return function(exc, content)
    return response


def _jwt_validate_error(exc: Exception, content: dict) -> Response:
    return Response('Token is invalid or expired', status.HTTP_400_BAD_REQUEST)