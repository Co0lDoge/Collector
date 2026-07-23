from typing import Protocol

class DataProvider(Protocol):
    def fetch_data(self):
        """Fetch data from the provider."""
        pass

    def commit(self):
        """Called after storage succeeds"""
        pass

class DataStorage(Protocol):
    def store_data(self, data):
        """Store the provided data."""
        pass