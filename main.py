import time
import providers
import logging
from interface import get_provider
from pymongo import MongoClient
from dotenv import load_dotenv
from settings import CollectorSettings

logging.basicConfig(level=logging.INFO)
load_dotenv(override=False)

class DataCollectorApp:
    def __init__(self, db_client, db_name, provider):
        # self.db = ...           # TODO MongoDB logic
        # self.collection = ...   # TODO MongoDB logic
        self.provider = provider

    def collect_data(self):
        data = self.provider.fetch_data()
        # TODO: Insert data into MongoDB collection (MongoDB logic)

if __name__ == "__main__":
    settings = CollectorSettings.from_env()
    client = MongoClient(settings.mongo_uri)

    try:
        provider = get_provider(settings.collector_provider)
    except Exception as e:
        logging.error(f"Error getting provider: {e}")
        exit(1)

    app = DataCollectorApp(client, settings.mongo_db_name, provider)

    while True:
        # TODO: Better scheduling?
        logging.info("Collecting data...")
        app.collect_data()
        time.sleep(settings.collector_interval_seconds)