from dataclasses import dataclass
import os

@dataclass
class CollectorSettings:
    mongo_uri: str
    mongo_db_name: str
    collector_provider: str
    collector_interval_seconds: int

    @classmethod
    def from_env(cls):
        return cls(
            mongo_uri=os.environ["MONGO_URI"],
            mongo_db_name=os.environ["MONGO_DB_NAME"],
            collector_provider=os.environ["COLLECTOR_PROVIDER"],
            collector_interval_seconds=int(os.environ["COLLECTOR_INTERVAL_SECONDS"])
        )