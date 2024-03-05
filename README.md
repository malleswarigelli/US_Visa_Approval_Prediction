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