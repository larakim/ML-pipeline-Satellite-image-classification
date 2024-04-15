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

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/larakim/ML-pipeline-Satellite-image-classification.mlflow 

export MLFLOW_TRACKING_USERNAME=yyyyyyyy 

export MLFLOW_TRACKING_PASSWORD=XXXXXXXXXXXXXXXXXXXXXXXXX 
```

#  Open EC2 and Install docker in EC2 Machine:

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

# Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one


# Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app