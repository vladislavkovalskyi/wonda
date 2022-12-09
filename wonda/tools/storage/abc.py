from abc import ABC, abstractmethod
from typing import Optional

from wonda.tools.storage.types import Key, Value, TTL, NO_KEY


class ABCBaseStorage(ABC):
    @abstractmethod
    def get(self, key: Key, default: Optional[Value] = NO_KEY) -> Value:
        pass

    @abstractmethod
    def delete(self, key: Key) -> None:
        pass

    @abstractmethod
    def contains(self, key: Key) -> bool:
        pass


class ABCStorage(ABCBaseStorage):
    @abstractmethod
    async def put(self, key: Key, value: Value) -> None:
        pass


class ABCExpiringStorage(ABCStorage):
    @abstractmethod
    async def put(self, key: Key, value: Value, ttl: TTL) -> None:
        pass
