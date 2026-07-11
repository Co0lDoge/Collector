from typing import Protocol

# TODO: define interface typing
class DataProvider(Protocol):
    def fetch_data(self):
        """Fetch data from the provider."""
        pass

# TODO: define interface typing
class DataStorage(Protocol):
    def store_data(self, data):
        """Store the provided data."""
        pass