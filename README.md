# Dockerized Data Collector Engine

Extendable data ingestion framework written in Python

This service acts as data collector for ETL pipelines. 
It is supposed to be used for data collection and storing processes,
isolating scheduling and configuration from business logic. 
Users simply need to mount their custom Data Providers and 
Data Storages into the Docker container at runtime.

# Features
* **Dynamic Plugin Architecture:** Add new data sources or database targets simply by mounting a Python file. 
* **Automatic Dependencies Retrieval:** The Docker entrypoint automatically detects and installs custom `requirements.txt` packages provided by mounted plugins before booting.
* **Execution Modes:** 
  * `ONCE`: Execution with zero idle resource consumption.
  * `DAEMON`: Built-in interval scheduler for standalone deployments.

# Quick Start with Docker Compose
When running the container, pass both the Core Framework variables and your Custom Plugin variables directly into the environment block.
```yaml
services:
  collector:
      image: collector:latest
      container_name: ${CONTAINER_PREFIX}_collector
      environment:
        # --- Core Framework Settings ---
        - COLLECTOR_PROVIDER=example_provider
        - COLLECTOR_STORAGE=example_storage
        - COLLECTOR_RUN_MODE=DAEMON
        - COLLECTOR_INTERVAL_SECONDS=3600
        - LOG_LEVEL=INFO
        
        # --- Plugin-Specific Settings ---
        # These are automatically picked up by your plugins via Pydantic
        - EXAMPLE_DATA_ENDPOINT=https://api.example.com/data
        - EXAMPLE_STORAGE_ENDPOINT=/app/data/output

      volumes:
      - ./collector/providers:/app/providers:ro
      - ./collector/storages:/app/storages:ro
```

# How to Write a Plugin
Plugins are dynamically loaded and configured using `pydantic-settings`.
## 1. To write Data Provider plugin, create a file in mounted `/providers` directory
```python
import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from core.interfaces import DataProvider
from core.registry import providers

class ExampleProviderSettings(BaseSettings):
    EXAMPLE_DATA_ENDPOINT: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@providers.register("example_provider")
class ExampleFileProvider(DataProvider):
    def __init__(self):
        self.config = ExampleProviderSettings()
    
    def fetch_data(self):
        endpoint = self.config.EXAMPLE_DATA_ENDPOINT
        logging.info(f"Retrieving data from files in {endpoint}...")  
        return [{"example": "data"}]
```

## 2. To write Data Storage plugin, create a file in mounted `/storages` directory
```python
import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from core.interfaces import DataStorage
from core.registry import storages

class ExampleFileStorageSettings(BaseSettings):
    EXAMPLE_STORAGE_ENDPOINT: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@storages.register("example_storage")
class ExampleFileStorage(DataStorage):
    def __init__(self):
        self.config = ExampleFileStorageSettings()
    
    def store_data(self, data):
        storage = self.config.EXAMPLE_STORAGE_ENDPOINT
        logging.info(f"Storing data in local files in {storage}...")  
        pass
```


