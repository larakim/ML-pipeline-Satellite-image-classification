from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
  source_url: str
  root_dir: Path
  zip_file: Path

  