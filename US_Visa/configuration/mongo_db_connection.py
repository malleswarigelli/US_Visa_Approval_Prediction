import sys

from US_Visa.exception import USvisaException
from US_Visa.logger import logging

import os
from US_Visa.constant import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where() # takes care of timeout error

class MongoDBClient:
    """
    Class Name :   MongoDBClient
    Description :   This method provides connection to MongoDB client; contains database_name 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connected successfully")
        except Exception as e:
            raise USvisaException(e,sys)