from dataclasses import dataclass
from typing import Optional
import os

@dataclass
class CollectorSettings:
    collector_provider: str
    collector_storage: str
    collector_run_mode: str # "ONCE" or "DAEMON"
    collector_interval_seconds: Optional[int] # required for "DAEMON" mode
    log_level: str

    @classmethod
    def from_env(cls):
        return cls(
            collector_provider=os.environ["COLLECTOR_PROVIDER"],
            collector_storage=os.environ["COLLECTOR_STORAGE"],
            collector_run_mode=os.environ["COLLECTOR_RUN_MODE"],
            collector_interval_seconds=int(os.environ.get("COLLECTOR_INTERVAL_SECONDS")),
            log_level=os.environ.get("LOG_LEVEL", "INFO").upper()
        )