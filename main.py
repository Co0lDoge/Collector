import logging
import schedule
import time
from core.bootstrap import bootstrap_collector
from core.interfaces import DataProvider, DataStorage
from core.registry import providers, storages
from settings import CollectorSettings

class DataCollectorApp:
    def __init__(self, provider: DataProvider, storage: DataStorage, settings: CollectorSettings):
        self.provider = provider
        self.storage = storage
        self.run_mode = settings.collector_run_mode
        self.run_interval = settings.collector_interval_seconds

    def ingest(self):
        logging.info("Starting ingestion cycle...")
        try:
            data = self.provider.fetch_data()
            self.storage.store_data(data)
            logging.info("Ingestion completed successfully.")
        except Exception as e:
            logging.error(f"Ingestion failed: {e}")

    def run(self):
        # TODO: enums for run modes
        if self.run_mode == "ONCE":
            logging.info("Running in ONCE mode")
            self.ingest()

        elif self.run_mode == "DAEMON":
            if self.run_interval is None:
                raise ValueError('No "COLLECTOR_INTERVAL_SECONDS" was provided for running app in DAEMON mode')
            
            logging.info(f"Running in DAEMON mode (Interval: {self.run_interval}s).")
            
            self.ingest()
            schedule.every(self.run_interval).seconds.do(self.ingest)
            
            while True:
                schedule.run_pending()
                time.sleep(1)
        
        else:
            raise ValueError(f"Unknown run mode: {self.run_mode}")

if __name__ == "__main__":
    settings = bootstrap_collector()

    try:
        provider = providers.get(settings.collector_provider)
        storage = storages.get(settings.collector_storage)
        app = DataCollectorApp(provider, storage, settings)
    except Exception as e:
        logging.error(f"Failed to initialize application: {e}")
        exit(1)

    app.run()