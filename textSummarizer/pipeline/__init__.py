from textSummarizer.exception import ProjectException 
from textSummarizer.logger import logging
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.components.data_validation import DataValidation

from textSummarizer.config import configuration
import os,sys



class Pipeline:


    def __init__(self,configuration=configuration()) -> None:
         try:
              self.config=configuration
         except Exception as e:
              raise ProjectException(e,sys) from e
         


    def start_data_ingestion(self):
         try:
              
              data_ingestion_config=self.config.get_data_ingestion_config()
              data_ingestion_obj=DataIngestion(data_ingestion_config=data_ingestion_config)

              data_ingestion_artifact=data_ingestion_obj.initiate_data_ingestion()

              return data_ingestion_artifact
         except Exception as e:
              raise ProjectException(e,sys) from e
         


    def start_data_validation(self,data_ingestion_artifact):
         try:
              data_validation_config=self.config.get_data_validation_config()
              
              data_val_obj=DataValidation(data_validation_config=data_validation_config,
                                          data_ingestion_artifact=data_ingestion_artifact)
              
              data_validation_artifact=data_val_obj.initiate_data_validaion()
         except Exception as e:
          raise ProjectException(e,sys) from e
     



    def run_pipeline(self):
         try:
              data_ingestion_artifact=self.start_data_ingestion()

              dat_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
         except Exception as e:
              raise ProjectException(e,sys) from e