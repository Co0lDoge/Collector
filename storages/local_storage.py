import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from core.interfaces import DataStorage
from core.registry import storages

class LocalFileStorageSettings(BaseSettings):
    COLLECTOR_LOCAL_DATA_DIRECTORY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@storages.register("local_storage")
class LocalFileStorage(DataStorage):
    def __init__(self):
        self.config = LocalFileStorageSettings()
    
    def store_data(self, data):
        directory = self.config.COLLECTOR_LOCAL_DATA_DIRECTORY
        logging.info(f"Storing data in local files in some directory...")  
        pass