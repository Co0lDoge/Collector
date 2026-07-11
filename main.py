import os
import time
import providers
from interface import get_provider
from pymongo import MongoClient
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)

class DataCollectorApp:
    def __init__(self, db_client, db_name, provider):
        # self.db = ...           # TODO MongoDB logic
        # self.collection = ...   # TODO MongoDB logic
        self.provider = provider

    def collect_data(self):
        data = self.provider.fetch_data()
        # TODO: Insert data into MongoDB collection (MongoDB logic)

if __name__ == "__main__":
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    client = MongoClient(MONGO_URI)
    
    PROVIDER_NAME = os.getenv("COLLECTOR_PROVIDER")
    try:
        provider = get_provider(PROVIDER_NAME)
    except Exception as e:
        logging.error(f"Error getting provider: {e}")
        exit(1)

    app = DataCollectorApp(client, MONGO_DB_NAME, provider)

    while True:
        logging.info("Collecting data...")
        app.collect_data()
        time.sleep(3600)