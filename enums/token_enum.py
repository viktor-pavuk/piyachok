from datetime import timedelta
from enum import Enum


class TokenEnum(Enum):
    ACTIVATION = ('activation', timedelta(days=1))
    RECOVERY = ('recovery', timedelta(hours=1))

    def __init__(self, token_type, exp_time):
        self.token_type = token_type
        self.exp_time = exp_time
