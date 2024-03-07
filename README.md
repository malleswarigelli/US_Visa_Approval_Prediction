# US_Visa_Approval_Prediction

# Git commands
- git add .

- git commit -m "Updated"

- git push origin main

# How to run?
- conda create -n visa python=3.8 -y
- conda activate visa
- pip install -r requirements.txt

# Workflow
1. constant
2. config_entity
3. artifact_entity
4. component
5. pipeline
6. app.py

### Export the environment variable since I don't want to add URL_KEY as public

os.getenv(MONGODB_URL_KEY)

```run this command in gitbash to set MONGODB_URL

export MONGODB_URL= "mongodb+srv://username:password@cluster0.ppivwau.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

```if using CMD, add it to environment variable``` 
  (PC -> edit environment variable -> Environment variables ->New -> Variable Name: AWS_ACCESS_KEY_ID_ENV_KEY,
                                                                      Variable Value: -------get value from AWS downloaded csv file---
                                                                      OK, repeat the process for AWS_SECRET_ACCESS_KEY_ENV_KEY
                                                                      
                                                            do the same for MongoDB_URL_KEY)

 ```                                                           

# data transformation steps

1. loading train,test data from data_ingestion artifact
2. calculate age column
3. apply preprocessing/ transformation (imputation, one hot encoding, ordinal encoding, scaling, handle imbalance data)
4. drop columns
5. mapping target feature values (convert categories to numbers)
6. save preprocessing object (preprocessing.pkl)
7. save transformed train, test data as np array (train.npy, test.npy)


# AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS console.
## 2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
- Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## 6. Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one

## 7. Setup github secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO