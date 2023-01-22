import pandas as pd
import numpy as np
import os, sys
from thyroid.exception import ThyroidException
from thyroid.logger import logging
from thyroid.config import mongo_client
import yaml
import dill    # To store python object as a file like pkl

def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df

    except Exception as e:
        raise ThyroidException(e, sys)

def write_yaml_file(file_path,data:dict):
    """
    Creating yaml report for validation status of each column
    """
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise ThyroidException(e, sys)

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    """
    Converting column to float type except target column
    """
    try:
        obj_cols = df.columns[df.dtypes.eq('O')]
        obj_cols = df[obj_cols]
        for column in obj_cols.columns:
            if column not in exclude_columns:
                #df[column]=df[column].astype('float')
                #df[column] = df[column].apply(pd.to_numeric, errors='coerce') 
                df[column] = pd.to_numeric(column, errors='coerce') # ignore errors
        return df
    except Exception as e:
        raise ThyroidException(e, sys)


def save_object(file_path: str, obj: object) -> None:
    """
    Saving object 
    """
    try:
        logging.info("Entered the save_object method of utils")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise ThyroidException(e, sys) from e


def load_object(file_path: str, ) -> object:
    """
    Loading object
    """
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise ThyroidException(e, sys) from e


def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise ThyroidException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise ThyroidException(e, sys) from e
