from abc import ABC, abstractmethod

class DataProvider(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

PROVIDERS = {}

def register_provider(name):
    """Decorator to register a collector's provider class"""
    def wrapper(cls):
        PROVIDERS[name] = cls
        return cls
    return wrapper

def get_provider(name):
    provider_class = PROVIDERS.get(name)
    if not provider_class:
        available = list(PROVIDERS.keys())
        raise ValueError(f"Provider '{name}' not found. Available: {available}")
    return provider_class()
    