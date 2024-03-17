from textSummarizer.exception import ProjectException
from textSummarizer.logger import logging
from textSummarizer.entity.config_entity import DataIngestionConfig
from textSummarizer.entity.artifact_entity import DataIngestionArtifact
import urllib,zipfile
import os,sys
from textSummarizer.constants import *


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig) -> None:
        try:
            logging.info(f"{'>>'*20} data ingestion started {'<<'*20}")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise ProjectException(e,sys) from e
        


    def download_url(self):
        try:
            download_url=self.data_ingestion_config.dataset_download_url

            zip_folder=self.data_ingestion_config.zip_data_dir

            file_name="data.zip"

            
            logging.info(f"making dir {zip_folder}")
            os.makedirs(zip_folder,exist_ok=True)

            folder_path=os.path.join(zip_folder,file_name)

            urllib.request.urlretrieve(download_url,folder_path)

            return folder_path


        except Exception as e:
            raise ProjectException(e,sys) from e
        


    def extract_files(self):
        try:
            zip_file=self.download_url()

            ingested_dir=self.data_ingestion_config.ingested_data_dir

            with zipfile.ZipFile(zip_file) as f:
                f.extractall(ingested_dir)


            return ingested_dir

        except Exception as e:
            raise ProjectException(e,sys) from e
        


    def initiate_data_ingestion(self):
        try:
           ingested_dir=self.extract_files()


           samsum_dataset_dir=os.path.join(ingested_dir,SAMSUM_DATASET)

           data_ingestion_artifact=DataIngestionArtifact(samsum_dataset_dir=samsum_dataset_dir)

           return data_ingestion_artifact
        
        except Exception as e:
            raise ProjectException(e,sys) from e