from textSummarizer.exception import ProjectException 
from textSummarizer.constants import *
from textSummarizer.utils import read_yaml_file
from textSummarizer.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig
import os,sys


class configuration:


    def __init__(self):
        try:
            self.config_info=read_yaml_file(file_path=CONFIG_FILE_PATH)
            self.pipeline_config=self.get_pipline_config()
            self.time_stamp=CURRENT_TIME_STAMP
        except Exception as e:
            raise ProjectException(e,sys) from e
        


    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            data_ingestion_info=self.config_info[DATA_INGESTION_CONFIG_KEY]

            artifact_dir=self.pipeline_config.artifact_dir

            dataset_download_url=data_ingestion_info[DATASET_DOWNLOAD_URL_KEY]

            data_ingestion_artifact_dir=os.path.join(artifact_dir,
                                                     DATA_INGESTION_ARTIFACT_DIR,
                                                     self.time_stamp)
            

            zip_data_dir=os.path.join(data_ingestion_artifact_dir,
                                      data_ingestion_info[ZIP_DATA_DIR_KEY])
            

            ingested_data_dir=os.path.join(data_ingestion_artifact_dir,
                                           data_ingestion_info[INGESTED_DIR_KEY])

            data_ingestion_config=DataIngestionConfig(dataset_download_url=dataset_download_url, 
                                                      zip_data_dir=zip_data_dir, 
                                                      ingested_data_dir=ingested_data_dir)
            
            return data_ingestion_config
        except Exception as e:
            raise ProjectException(e,sys) from e
        




    def get_data_validation_config(self)->DataValidationConfig:
        try:

            data_validation_info=self.config_info[DATA_VALIDATION_CONFIG_KEY]

            artifact_dir=self.pipeline_config.artifact_dir


            data_validation_dir=os.path.join(artifact_dir,
                                             DATA_VALIDATION_ARTIFACT_DIR,
                                             self.time_stamp)
            
            os.makedirs(data_validation_dir,exist_ok=True)


            status_file_path=os.path.join(data_validation_dir,
                                          data_validation_info[STATUS_FILE_KEY])
            

            required_files=data_validation_info[ALL_REQUIRED_FILES_KEY]
            

            data_validation_config=DataValidationConfig(status_file_path=status_file_path,
                                                        required_files=required_files)
            

            return data_validation_config
        
        except Exception as e:
            raise ProjectException(e,sys) from e

        



    def get_pipline_config(self)->TrainingPipelineConfig:
        try:

            pipeline_info=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]

            artifact_dir=os.path.join(ROOT_DIR, 
                                      pipeline_info[PIPELINE_NAME_KEY],
                                      pipeline_info[ARTIFACT_DIR_KEY])
            
            training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)

            return training_pipeline_config
        except Exception as e:
            raise ProjectException(e,sys) from e
        
