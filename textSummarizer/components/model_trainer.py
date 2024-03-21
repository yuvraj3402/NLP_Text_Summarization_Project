from textSummarizer.exception import ProjectException
from textSummarizer.logger import logging
from textSummarizer.entity.config_entity import ModelTrainerConfig
from textSummarizer.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
import os,sys
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from textSummarizer.utils import read_yaml_file
from textSummarizer.constants import *
from datasets import load_from_disk

class ModelTrainer:

    def __init__(self,data_transformation_artifact:DataTransformationArtifact,
                 model_trainer_config:ModelTrainerConfig) -> None:
         try:
              self.data_transformation_artifact=data_transformation_artifact
              self.model_trainer_config=model_trainer_config
              self.model_yaml_path=read_yaml_file(self.model_trainer_config.model_config_file_path)
         except Exception as e:
              raise ProjectException(e,sys) from e




    def update_property_of_class(self,instance_ref:object, property_data: dict):
        try:
          for key, value in property_data.items():
              setattr(instance_ref, key, value)
          return instance_ref
        except Exception as e:
            raise ProjectException(e, sys) from e
         


    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            os.makedirs(self.model_trainer_config.trained_model_dir,exist_ok=True)

            model_name=self.model_trainer_config.model_name

            model=AutoModelForSeq2SeqLM.from_pretrained(model_name)

            seq2seq_data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer,model=model)



            tokenizer=self.data_transformation_artifact.Tokenizer

            dataset_samsum_pt=load_from_disk(self.data_transformation_artifact.transformed_samsum_dataset_dir)




            model_args=self.model_yaml_path[PARAMS]



            training_arguments=self.update_property_of_class(instance_ref=TrainingArguments,
                                                            property_data=model_args)
                                                            


            
            trainer = Trainer(model=model , args=training_arguments,
                              tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                              train_dataset=dataset_samsum_pt["test"], 
                              eval_dataset=dataset_samsum_pt["validation"])


            trainer.train()




            samsum_model_path=self.model_trainer_config.saved_model_path

            tokenizer_file_path=self.model_trainer_config.Tokenizer_path

            model.save_pretrained(samsum_model_path)

     
            tokenizer.save_pretrained(tokenizer_file_path)






            model_trainer_artifact=ModelTrainerArtifact(samsum_model=samsum_model_path, 
                                                        Tokenizer=tokenizer_file_path)

            return model_trainer_artifact

            
            
        except Exception as e:
            raise ProjectException(e,sys) from e