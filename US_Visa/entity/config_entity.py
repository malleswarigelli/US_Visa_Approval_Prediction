import os
from US_Visa.constant import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass # if use this, you can declare class variables without self keyword; no need to say self.pipeline_name. 
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME) # creates data_ingestion folder 
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME) # data_ingestion/feature_store/usvisa.csv
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME) # data_ingestion/ingested/train.csv
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)  # data_ingestion/ingested/test.csv
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO # 0.2
    collection_name:str = DATA_INGESTION_COLLECTION_NAME # visa_data (collection name in MongoDB)



@dataclass
class DataValidationConfig:
    data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir,DATA_VALIDATION_DIR_NAME)
    drift_report_file_path:str = os.path.join(data_validation_dir, 
                                              DATA_VALIDATION_DRIFT_REPORT_DIR,
                                              DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)