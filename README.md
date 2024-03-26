# US_Visa_Approval_Prediction

- The US Visa Approval Prediction project utilizes ML to forecast the probability of visa approval for individuals seeking entry into the United States. This model predicts the likelihood of a US visa application being approved based on various factors including demographics, employment history, education, finances, and travel purpose.
- This project aims to provide valuable insights to applicants, immigration authorities, and legal professionals, enabling informed decision-making and optimizing the visa application process.

# Techstack
- AWS: Cloud computing platform 
- AWS S3: Stores the model and dataset
- AWS ECR (Elastic Container Registry): To host our containerized application
- AWS EC2 (Elastic Compute Cloud): For scalable and reliable virtual servers
- GitHub: Our code repository for version control and collaboration
- GitHub Actions (CI/CD tool): To automate deployment workflows
- Visual Studio Code: Our integrated development environment (IDE)
- Python: The programming language used to build the model.
- FastAPI: A modern, fast (high-performance) web framework for building APIs.

# Workflow
1) Training pipeline is made to train, evaluate multiple ML classification models, fine tune and select the model giving best metrics, stored the final training mdoel into AWS S3 bucket for making predictions
2) Prediction pipeline is made to make predictions on new or unseen data user provided/ingest from MongoDB
3) Deployment: containerize the application using Docker, store docker image in AWS ECR repository for easy deployment and scalability
- Set up AWS EC3 instance to host our deployed application
- Leveraged GitHub Actions to automate our deployment workflow. With each code push, the model is retrained, the Docker image is built, stored in ECR and the application is deployed to the EC2 instance.
4) Built web app with FASTAPI that expose model's prediction functionality.



# Git commands
- git add .

- git commit -m "Updated"

- git push origin main

# How to run?
- conda create -n visa python=3.8 -y
- conda activate visa
- pip install -r requirements.txt

# Files to fill for each component workflow
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

# AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS console.
## 2. Create IAM user for deployment

# with specific access

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
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO