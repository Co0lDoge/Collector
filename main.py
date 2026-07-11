import os
import time
import providers
from interface import get_provider
from pymongo import MongoClient
from dotenv import load_dotenv
import logging

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
    MONGO_URI = os.environ["MONGO_URI"]
    MONGO_DB_NAME = os.environ["MONGO_DB_NAME"]
    PROVIDER_NAME = os.environ["COLLECTOR_PROVIDER"]
    COLLECTOR_INTERVAL_SECONDS = int(os.environ["COLLECTOR_INTERVAL_SECONDS"])

    client = MongoClient(MONGO_URI)

    try:
        provider = get_provider(PROVIDER_NAME)
    except Exception as e:
        logging.error(f"Error getting provider: {e}")
        exit(1)

    app = DataCollectorApp(client, MONGO_DB_NAME, provider)

    while True:
        # TODO: Better scheduling?
        logging.info("Collecting data...")
        app.collect_data()
        time.sleep(COLLECTOR_INTERVAL_SECONDS)