from textSummarizer.exception import ProjectException
from textSummarizer.logger import logging
from textSummarizer.entity.config_entity import DataValidationConfig
from textSummarizer.entity.artifact_entity import DataIngestionArtifact
import os,sys


class DataValidation:


    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact) -> None:
        try:
            logging.info(f"{'>>'*20} data validation started {'<<'*20}")

            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise ProjectException(e,sys) from e
        


    def initiate_data_validaion(self):
        try:
            validaion_status=None
            dataset_dir=self.data_ingestion_artifact.samsum_dataset_dir

            status_file=self.data_validation_config.status_file_path

            required_files=self.data_validation_config.required_files


            for files in required_files:
                if files not in os.listdir(dataset_dir):
                    validaion_status=False
                    with open(status_file,'w') as f:
                        f.write(f"{files} not found validation stastus is validaion status {validaion_status}")

                else:
                    validaion_status=True
                    with open(status_file,'w') as f:
                        f.write(f"all files present validaion status {validaion_status}")

            logging.info(f"validation status is {validaion_status}")



            logging.info(f"{'>>'*20} data validation complete {'<<'*20}")
            

            return validaion_status
                
        except Exception as e:
            raise ProjectException(e,sys) from e