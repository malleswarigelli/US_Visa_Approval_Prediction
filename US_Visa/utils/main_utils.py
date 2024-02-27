import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from US_Visa.exception import USvisaException
from US_Visa.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    read yaml file from file
    file_path: str location of file to load
    return: dict returns dictionary
    """
    logging.info("Entered the read_yaml_file method of utils")
    try:
        with open(file_path, "rb") as yaml_file:
            dict= yaml.safe_load(yaml_file)
        logging.info("Exited the read_yaml_file method of utils")
        return dict

    except Exception as e:
        raise USvisaException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Write yaml file to file
    file_path: str location of file to save
    obj: object yaml object to save
    return: None
    """
    logging.info("Entered the write_yaml_file method of utils") 
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
        logging.info("Exited the write_yaml_file method of utils")
        
    except Exception as e:
        raise USvisaException(e, sys)

def save_object(file_path: str, obj: object) -> None:
    """
    Save pickled object to file
    file_path: str location of file to save
    obj: object pickled object to save
    return: None
    """
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise USvisaException(e, sys) from e

def load_object(file_path: str) -> object:
    """
    load pickled object from file
    file_path: str location of file to load
    return: object pickled object loaded
    """
    logging.info("Entered the load_object method of utils")

    try:

        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise USvisaException(e, sys) from e

def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    return: None 
    """
    logging.info("Entered save_numpy_array_data method of utils")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
        logging.info("Exited the save_numpy_array_data method of utils")
            
    except Exception as e:
        raise USvisaException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    logging.info("Entered load_numpy_array_data method of utils")
    try:
        with open(file_path, 'rb') as file_obj:
            array = np.load(file_obj)            
        logging.info("Exited the load_numpy_array_data method of utils")
        return array
            
    except Exception as e:
        raise USvisaException(e, sys) from e
    

def drop_columns(df: DataFrame, cols: list)-> DataFrame:

    """
    drop the columns form a pandas DataFrame
    df: pandas DataFrame
    cols: list of columns to be dropped
    returns: DataFrame
    """
    logging.info("Entered drop_columns method of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise USvisaException(e, sys) from e