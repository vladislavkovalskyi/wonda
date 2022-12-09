from os import getenv
from typing import Optional


class Token(str):
    @classmethod
    def from_env(cls, variable_name: Optional[str] = "WONDA_TOKEN") -> "Token":
        return cls(getenv(variable_name))
