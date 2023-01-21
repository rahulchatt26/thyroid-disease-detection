import sys, os
from datetime import datetime
from thyroid.logger import logging
from thyroid.exception import ThyroidException


FILE_NAME = "thyroid.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.arfifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")

        except Exception as e:
            raise ThyroidException(e, sys)


class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name = "HealthCare"
            self.collection_name = "Thyroid"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.arfifact_dir,"data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2

        except Exception as e:
            raise ThyroidException(e, sys)


    def to_dict(self,)->dict:
        """
        To convert and return the output as dict : data_ingestion_config
        """ 
        try:
            return self.__dict__

        except Exception as e:
            raise ThyroidException(e, sys)


class DataValidationConfig:...

class DataTransformation:...

class ModelTrainerConfig:...

class ModelEvaluationConfig:...

class ModelPusherConfig:...