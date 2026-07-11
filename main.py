import time
import logging
from core.bootstrap import bootstrap_collector
from core.interfaces import DataProvider, DataStorage
from core.registry import providers, storages

class DataCollectorApp:
    def __init__(self, provider: DataProvider, storage: DataStorage):
        self.provider = provider
        self.storage = storage

    def ingest(self):
        data = self.provider.fetch_data()
        self.storage.store_data(data) # TODO: is that good?

if __name__ == "__main__":
    settings = bootstrap_collector()

    try:
        provider = providers.get(settings.collector_provider)
        storage = storages.get(settings.collector_storage)
        app = DataCollectorApp(provider, storage)
    except Exception as e:
        logging.error(f"Failed to initialize application: {e}")
        exit(1)

    while True:
        # TODO: Better scheduling?
        logging.info("Collecting data...")
        app.ingest()
        time.sleep(settings.collector_interval_seconds)