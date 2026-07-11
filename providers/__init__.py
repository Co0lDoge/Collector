import os
import importlib
import pkgutil

for module in pkgutil.iter_modules([os.path.dirname(__file__)]):
    if module.name != "__init__":
        importlib.import_module(f"{__package__}.{module.name}")