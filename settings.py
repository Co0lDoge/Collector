from dataclasses import dataclass
import os

@dataclass
class CollectorSettings:
    collector_provider: str
    collector_storage: str
    collector_interval_seconds: int

    @classmethod
    def from_env(cls):
        return cls(
            collector_provider=os.environ["COLLECTOR_PROVIDER"],
            collector_storage=os.environ["COLLECTOR_STORAGE"],
            collector_interval_seconds=int(os.environ["COLLECTOR_INTERVAL_SECONDS"])
        )