from textSummarizer.entity.config_entity import DataTransformationConfig
from textSummarizer.entity.artifact_entity import DataIngestionArtifact
from textSummarizer.entity.artifact_entity import DataTransformationArtifact
from datasets import load_from_disk
from transformers import AutoTokenizer
import os,sys
from textSummarizer.exception import ProjectException
from textSummarizer.logger import logging


class DataTransformation:


    def __init__(self,data_transformer_config:DataTransformationConfig,
                 data_ingestion_artifact:DataIngestionArtifact) -> None:
            try:
                self.data_transformer_config=data_transformer_config
                self.data_ingestion_artifact=data_ingestion_artifact
                self.tokenizer=AutoTokenizer.from_pretrained(self.data_transformer_config.Tokenizer)
            except Exception as e:
                raise ProjectException(e,sys) from e



    def map_words_to_features(self,batch_summary):
         try:
              input_encoding=self.tokenizer(batch_summary["dialogue"],max_length = 1024, truncation = True)

              with self.tokenizer.as_target_tokenizer():
                   target_encoding=self.tokenizer(batch_summary["summary"],max_length = 128, truncation = True)
                   
              return {'input_ids' : input_encoding['input_ids'],
                'attention_mask': input_encoding['attention_mask'],
                'labels': target_encoding['input_ids']
            }
         except Exception as e:
              raise ProjectException(e,sys) from e
        

        
    

    def initiate_data_transformation(self)->DataTransformationArtifact:
         try:
            dataset=self.data_ingestion_artifact.samsum_dataset_dir

            dataset_tr=load_from_disk(dataset_path=dataset)

            dataset_map=dataset_tr.map(self.map_words_to_features,batched=True)


            os.makedirs(self.data_transformer_config.transformed_data_dir,exist_ok=True)

            transformed_data_path=os.path.join(self.data_transformer_config.transformed_data_dir,"samsum_dataset")

            dataset_map.save_to_disk(transformed_data_path)

            data_transformation_artifact=DataTransformationArtifact(transformed_samsum_dataset_dir=transformed_data_path)

            return data_transformation_artifact
         
         except Exception as e:
              raise ProjectException(e,sys) from e