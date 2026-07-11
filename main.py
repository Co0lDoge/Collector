import os
import time
from pymongo import MongoClient
import providers
from interface import get_provider

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
        print(f"Error getting provider: {e}") # TODO: Use logging instead of print
        exit(1)

    app = DataCollectorApp(client, MONGO_DB_NAME, provider)

    while True:
        print(f"Collecting data...") # TODO: Use logging instead of print
        app.collect_data()
        time.sleep(3600)