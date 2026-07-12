import logging
from core.bootstrap import bootstrap_collector
from core.registry import providers, storages
from app import DataCollectorApp

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