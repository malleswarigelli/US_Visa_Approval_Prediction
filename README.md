# US_Visa_Approval_Prediction

🔍 Build End to End ML pipeline to train, predict US Visa Approval and deploy to AWS EC2 by integrating Docker, CI/CD tool: GitHub Actions

- The US Visa Approval Prediction project aims to develop a machine learning model that can accurately predict the approval or rejection of US visa applications. This project adopts a modular coding approach, leveraging various technologies to build an end-to-end solution.
- This project aims to provide valuable insights to applicants, immigration authorities, and legal professionals, enabling informed decision-making and optimizing the visa application process.

# Techstack
- Python: The programming language used to build the model.
- Python libraries: pandas, numpy, matplotlib, plotly, seaborn, scipy, scikit-learn etc
- Jupyter notebook: EDA, experiment with different algorithms, and fine-tune the model parameters.
- MongoDB: a noSQL database, to store and manage data
- AWS: Cloud computing platform 
- AWS S3: Stores the model and dataset
- AWS ECR (Elastic Container Registry): To host our containerized application
- AWS EC2 (Elastic Compute Cloud): For scalable and reliable virtual servers
- GitHub: Our code repository for version control and collaboration
- GitHub Actions (CI/CD tool): To automate deployment workflows
- Visual Studio Code: Our integrated development environment (IDE) for writing modular and scalable code 
- FastAPI: A modern, fast (high-performance) web framework for building APIs.
- Ubuntu: provides a reliable and stable operating system environment for hosting your project's infrastructure, such as EC2 instances or GitHub Action Runners.
By combining these technologies, the US Visa Approval Prediction project aims to develop a reliable and efficient machine learning model that can assist in predicting the outcome of US visa applications, streamlining the visa approval process, and improving decision-making.

# Workflow
1) Training pipeline is made to ingest data from MongoDB, validate using Evidently, transform data for feature engineering, train and evaluate multiple ML classification models, fine tune and select the model giving best metrics, stored the final best trained mdoel into AWS S3 bucket for making predictions
2) Prediction pipeline is made to ingest new or unseen data from user or from MongoDB, transform new data with preprocessing.pkl from training pipeline and make predictions with the best trainined model saved in AWS S3. 
3) Deployment: containerize the application using Docker, store docker image in AWS ECR repository for easy deployment and scalability
- Set up AWS EC2 instance to host our deployed application
- Leveraged GitHub Actions to automate our deployment workflow. With each code push, the model is retrained, the Docker image is built, test, push to AWS ECR, pull image to EC2 and the application runs in EC2 instance.
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

export MONGODB_URL="mongodb+srv://username:password@cluster0.ppivwau.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

```                                                         

# AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS console.
## 2. Create IAM user for deployment

# with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


# Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

# Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
- Save the URI: 637423357032.dkr.ecr.us-east-1.amazonaws.com/usvisa_ecr

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
