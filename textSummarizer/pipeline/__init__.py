from textSummarizer.exception import ProjectException 
from textSummarizer.logger import logging
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.components.model_trainer import ModelTrainer
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

              
              return data_validation_artifact
         except Exception as e:
              raise ProjectException(e,sys) from e
         

     
    def start_data_transformation(self,data_ingestion_artifact):
         try:
          data_transformation_config=self.config.get_data_transformation_config()
          data_transformation_obj=DataTransformation(data_transformer_config=data_transformation_config,
                                                     data_ingestion_artifact=data_ingestion_artifact)
          
          data_transformation_artifact=data_transformation_obj.initiate_data_transformation()

          return data_transformation_artifact
         except Exception as e:
             raise ProjectException(e,sys) from e
         

    def start_model_training(self,data_transformation_artifact):
         try:

          model_trainer_config=self.config.get_model_trainer_config()
          model_trainer_obj=ModelTrainer(data_transformation_artifact=data_transformation_artifact,
                                         model_trainer_config=model_trainer_config)
          
          model_trainer_artifact=model_trainer_obj.initiate_model_trainer()

          return model_trainer_artifact
         except Exception as e:
              raise ProjectException(e,sys) from e
     
         



    def run_pipeline(self):
         try:
              data_ingestion_artifact=self.start_data_ingestion()

              dat_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)


              data_transformation_artifact=self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact)

              model_trainer_artifact=self.start_model_training(data_transformation_artifact=data_transformation_artifact)
              
         except Exception as e:
              raise ProjectException(e,sys) from e