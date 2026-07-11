import providers
import storages
import time
import logging
from dotenv import load_dotenv
from settings import CollectorSettings
from core.interfaces import DataProvider, DataStorage
from core.registry import get_provider, get_storage

logging.basicConfig(level=logging.INFO)
load_dotenv(override=False)

class DataCollectorApp:
    def __init__(self, provider: DataProvider, storage: DataStorage):
        self.provider = provider
        self.storage = storage

    def ingest(self):
        data = self.provider.fetch_data()
        self.storage.store_data(data) # TODO: is that good?

if __name__ == "__main__":
    settings = CollectorSettings.from_env()

    # TODO: refactor two trys?
    try:
        provider = get_provider(settings.collector_provider)
    except Exception as e:
        logging.error(f"Error getting provider: {e}")
        exit(1)

    try:
        storage = get_storage(settings.collector_storage)
    except Exception as e:
        logging.error(f"Error getting storage: {e}")
        exit(1)

    app = DataCollectorApp(provider, storage)

    while True:
        # TODO: Better scheduling?
        logging.info("Collecting data...")
        app.ingest()
        time.sleep(settings.collector_interval_seconds)