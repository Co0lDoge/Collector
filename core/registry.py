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

STORAGES = {}

def register_storage(name):
    """Decorator to register a collector's storage class"""
    def wrapper(cls):
        STORAGES[name] = cls
        return cls
    return wrapper

def get_storage(name):
    storage_class = STORAGES.get(name)
    if not storage_class:
        available = list(STORAGES.keys())
        raise ValueError(f"Storage '{name}' not found. Available: {available}")
    return storage_class()