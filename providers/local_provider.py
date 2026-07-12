import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from core.interfaces import DataProvider
from core.registry import providers

class LocalFileProviderSettings(BaseSettings):
    COLLECTOR_LOCAL_DATA_DIRECTORY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@providers.register("local_provider")
class LocalFileProvider(DataProvider):
    def __init__(self):
        self.config = LocalFileProviderSettings()
    
    def fetch_data(self):
        directory = self.config.COLLECTOR_LOCAL_DATA_DIRECTORY
        logging.info(f"Fetching data from local files in some directory")  
        pass