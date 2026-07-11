from typing import TypeVar, Generic, Type, Dict
from core.interfaces import DataProvider, DataStorage

T = TypeVar("T")

class Registry(Generic[T]):
    def __init__(self, kind: str):
        self.kind = kind
        self._entries: Dict[str, Type[T]] = {}

    def register(self, name: str):
        """Decorator to register a class"""
        def decorator(cls: Type[T]) -> Type[T]:
            self._entries[name] = cls
            return cls
        return decorator

    def get(self, name: str) -> T:
        """Retrieve an instance of the registered class by name"""
        cls = self._entries.get(name)
        if not cls:
            available = ", ".join(self._entries.keys())
            raise ValueError(f"Unknown {self.kind} '{name}'. Available: [{available}]")
        
        return cls()

providers = Registry[DataProvider]("Provider")
storages = Registry[DataStorage]("Storage")