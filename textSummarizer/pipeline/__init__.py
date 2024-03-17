from textSummarizer.exception import ProjectException 
from textSummarizer.logger import logging
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.config.configuration import configuration
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
         



    def run_pipeline(self):
         try:
              data_ingestion_artifact=self.start_data_ingestion()
         except Exception as e:
              raise ProjectException(e,sys) from e