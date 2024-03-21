from textSummarizer.config import configuration
from textSummarizer.exception import ProjectException
from transformers import pipeline,AutoTokenizer
import os,sys


class PredictionPipeline:


    def __init__(self,configuration=configuration()) -> None:
        try:
            self.configuration=configuration
        except Exception as e:
            raise ProjectException(e,sys) from e


    def predict(self,text):
        try:
            model_config=self.configuration.get_model_trainer_config()

            tokenizer=AutoTokenizer.from_pretrained(model_config.Tokenizer_path)

            model=model_config.saved_model_path


            gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

            pipe = pipeline("summarization", model=model,tokenizer=tokenizer)

            print("Dialogue:")
            print(text)

            output = pipe(text, **gen_kwargs)[0]["summary_text"]
            print("\nModel Summary:")
            print(output)

            return output


        except Exception as e:
            raise ProjectException(e,sys) from e