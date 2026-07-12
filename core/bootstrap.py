
import importlib
import logging
import pkgutil
from dotenv import load_dotenv
from settings import CollectorSettings

def _discover_modules(package_name: str):
    try:
        # Import the package to ensure it's available for discovery
        package = importlib.import_module(package_name)

        # Iterate through the modules in the package and import them
        for loader, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
            if not is_pkg:
                full_module_name = f"{package_name}.{module_name}"
                importlib.import_module(full_module_name)
                logging.debug(f"Module loaded: {full_module_name}")

    except Exception as e:
        logging.error(f"Error discovering modules in {package_name}: {e}")
    
def bootstrap_collector():
    load_dotenv(override=False)

    settings = CollectorSettings.from_env()
    
    logging.basicConfig(
        level=settings.log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    logging.info("Initializing collector's plugins...")
    _discover_modules("providers")
    _discover_modules("storages")

    return settings




    