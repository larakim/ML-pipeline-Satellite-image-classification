# ML-pipeline-Satellite-image-classification
Satellite Image Classification (link: https://www.kaggle.com/datasets/mahmoudreda55/satellite-image-classification?resource=download)

## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


## MLflow
MLFLOW_TRACKING_URI=https://dagshub.com/larakim/ML-pipeline-Satellite-image-classification.mlflow \
MLFLOW_TRACKING_USERNAME=larakim \
MLFLOW_TRACKING_PASSWORD=6f0caff147881a6dd8d7169da2dc21273f023c6c \
python script.py

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/larakim/ML-pipeline-Satellite-image-classification.mlflow 

export MLFLOW_TRACKING_USERNAME=larakim 

export MLFLOW_TRACKING_PASSWORD=6f0caff147881a6dd8d7169da2dc21273f023c6c 
```