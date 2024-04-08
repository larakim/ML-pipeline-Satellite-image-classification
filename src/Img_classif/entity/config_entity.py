from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
  source_url: str
  root_dir: Path
  zip_file: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
  root_dir: Path
  base_model_path: Path
  params_img_size: tuple
  params_lr: float
  params_classes: int

@dataclass(frozen=True)
class Model_trainer_config:
    root_dir: Path
    base_model_path: Path
    updated_model_path: Path
    data_path: Path
    epoch: int
    batch_size: int
    img_size: tuple

@dataclass(frozen=True)
class Modelevaluationconfig():
    model_path: Path
    data_path: Path
    batch_size: int
    img_size: tuple
    eval_path:Path
    root_dir:Path
    param_all: dict
    mlflow_uri: str
    