from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, NoReturn, Union

if TYPE_CHECKING:
    from wonda.api import ABCAPI, API


class ABCResponseValidator(ABC):
    @abstractmethod
    async def validate(
        self, method: str, data: dict, response: Any, ctx_api: Union["ABCAPI", "API"]
    ) -> Union[Any, NoReturn]:
        pass
