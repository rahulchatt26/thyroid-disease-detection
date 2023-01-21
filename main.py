from thyroid.components.data_ingestion import DataIngestion
from thyroid.exception import ThyroidException
import os, sys
from thyroid.pipeline import training_pipeline
from thyroid.entity import config_entity



if __name__ == "__main__":
        try:
                training_pipeline_config = config_entity.TrainingPipelineConfig()

                #data ingestion
                data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
                print(data_ingestion_config.to_dict)
                data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
                data_ingestion_arfifact = data_ingestion.initiate_data_ingestion()

        except Exception as e:
                raise ThyroidException(e,sys)