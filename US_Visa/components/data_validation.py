import json
import sys

import pandas as pd
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection

from pandas import DataFrame

from US_Visa.exception import USvisaException
from US_Visa.logger import logging
from US_Visa.utils.main_utils import read_yaml_file, write_yaml_file
from US_Visa.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from US_Visa.entity.config_entity import DataValidationConfig
from US_Visa.constant import SCHEMA_FILE_PATH


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        """
        :param data_ingestion_artifact: Output reference of data ingestion artifact stage
        :param data_validation_config: configuration for data validation
        """
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config =read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise USvisaException(e,sys)

    def validate_number_of_columns(self, df: DataFrame) -> bool:
        """
        Method Name :   validate_number_of_columns
        Description :   This method validates the number of columns
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info(f"Entering validate_number_of_columns method of DataValidation")
        
        try:
            status = len(df.columns) == len(self._schema_config["columns"])
            logging.info(f"Is required column present: [{status}]")
            logging.info(f"Exiting validate_number_of_columns method of DataValidation")
            return status
        except Exception as e:
            raise USvisaException(e, sys)

    def is_column_exist(self, df: DataFrame) -> bool:
        """
        Method Name :   is_column_exist
        Description :   This method validates the existence of a numerical and categorical columns
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info(f"Entering validate_number_of_columns method of DataValidation")
        try:
            dataframe_columns = df.columns
            missing_numerical_columns = []
            missing_categorical_columns = []
            for column in self._schema_config["numerical_columns"]:
                if column not in dataframe_columns:
                    missing_numerical_columns.append(column)

            if len(missing_numerical_columns)>0:
                logging.info(f"Missing numerical column: {missing_numerical_columns}")


            for column in self._schema_config["categorical_columns"]:
                if column not in dataframe_columns:
                    missing_categorical_columns.append(column)

            if len(missing_categorical_columns)>0:
                logging.info(f"Missing categorical column: {missing_categorical_columns}")
                
            logging.info(f"Exiting validate_number_of_columns method of DataValidation")
            
            return False if len(missing_categorical_columns)>0 or len(missing_numerical_columns)>0 else True
        except Exception as e:
            raise USvisaException(e, sys) from e

    @staticmethod
    # static method allows to call the method directly (class.method()) instead of requiring to create object/instance
    def read_data(file_path) -> pd.DataFrame:
        """
        Method Name :   read_data
        Description :   This method reads csv file
        
        Output      :   Returns dataframe
        On Failure  :   Write an exception log and then raise an exception
       
        """
        logging.info(f"Entering read_data method of DataValidation")
        try:
            logging.info(f"Exiting read_data method of DataValidation")
            
            return pd.read_csv(file_path)
        
        except Exception as e:
            raise USvisaException(e, sys)

    def detect_dataset_drift(self, reference_df: DataFrame, current_df: DataFrame, ) -> bool:
        """
        Method Name :   detect_dataset_drift
        Description :   This method validates if drift between two files is detected 
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info(f"Entering detect_dataset_drift method of DataValidation")
        try:
            data_drift_profile = Profile(sections=[DataDriftProfileSection()])

            data_drift_profile.calculate(reference_df, current_df)
            
            logging.info(f"converting {data_drift_profile} into json format")
            report = data_drift_profile.json()
            
            logging.info(f"loading {report} and converting as yaml file")
            json_report = json.loads(report)
            write_yaml_file(file_path=self.data_validation_config.drift_report_file_path, content=json_report)

            n_features = json_report["data_drift"]["data"]["metrics"]["n_features"]
            n_drifted_features = json_report["data_drift"]["data"]["metrics"]["n_drifted_features"]

            logging.info(f"{n_drifted_features}/{n_features} drift detected.")
            drift_status = json_report["data_drift"]["data"]["metrics"]["dataset_drift"]
            logging.info(f"Exiting detect_dataset_drift method of DataValidation")
            
            return drift_status
        
        except Exception as e:
            raise USvisaException(e, sys) from e

    def initiate_data_validation(self) -> DataValidationArtifact:
        """
        Method Name :   initiate_data_validation
        Description :   This method initiates the data validation component for the pipeline
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered initiate_data_validation method of data validation")
        try:
            validation_error_msg = ""
            logging.info("Starting data validation")
            
            # import train.csv and test.csv as dataframes
            train_df, test_df = (DataValidation.read_data(file_path=self.data_ingestion_artifact.trained_file_path), # since read_data is static method, called directly as class.method()
                                 DataValidation.read_data(file_path=self.data_ingestion_artifact.test_file_path))
            
            # checking if required number of columns exist
            status = self.validate_number_of_columns(df=train_df)
            logging.info(f"All required columns present in training dataframe: {status}")
            if not status:
                validation_error_msg += f"Columns are missing in training dataframe."
                
            status = self.validate_number_of_columns(df=test_df)
            logging.info(f"All required columns present in testing dataframe: {status}")
            if not status:
                validation_error_msg += f"Columns are missing in test dataframe."

            # checking if numerical and categorical columns match with schema.yaml
            status = self.is_column_exist(df=train_df)
            logging.info(f"All required numerical, categorical columns present in training dataframe: {status}")
            if not status:
                validation_error_msg += f"Numerical or Categorical columns are missing in training dataframe."
            
            
            status = self.is_column_exist(df=test_df)
            logging.info(f"All required numerical, categorical columns present in test dataframe: {status}")
            if not status:
                validation_error_msg += f"Numerical or Categorical columns are missing in test dataframe."

            validation_status = len(validation_error_msg) == 0

            if validation_status:
                drift_status = self.detect_dataset_drift(train_df, test_df)
                if drift_status:
                    logging.info(f"Drift detected.")
                    validation_error_msg = "Drift detected"
                else:
                    validation_error_msg = "Drift not detected"
            else:
                logging.info(f"Validation_error: {validation_error_msg}")
                

            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status,
                message=validation_error_msg,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )

            logging.info(f"Data validation artifact: {data_validation_artifact}")
            logging.info("Exited data validation")
            
            return data_validation_artifact
        
        except Exception as e:
            raise USvisaException(e, sys) from e