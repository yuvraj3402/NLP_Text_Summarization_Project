import os
from datetime import datetime




def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR=os.getcwd()
CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"
MODEL_FILE_NAME="model.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"




#training pipline constants
TRAINING_PIPELINE_CONFIG_KEY= "training_pipeline_config"
PIPELINE_NAME_KEY="pipeline_name"
ARTIFACT_DIR_KEY ="artifact_dir"



#data ingestion constants
DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATASET_DOWNLOAD_URL_KEY="dataset_download_url"
DATA_INGESTION_ARTIFACT_DIR="data_ingestion"
ZIP_DATA_DIR_KEY="zip_data_dir"
INGESTED_DIR_KEY="ingested_dir"


#dataset dir
SAMSUM_DATASET="samsum_dataset"


#data validation constants
DATA_VALIDATION_CONFIG_KEY="data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR="data_validation"
STATUS_FILE_KEY="status_file"
ALL_REQUIRED_FILES_KEY="all_required_files"


#data transformation constants
DATA_TRANSFORMATION_CONFIG_KEY="data_transformation_config"
DATA_TRANSFORMATION_ARTIFACT_DIR="data_transformation"
TOKENIZER_NAME_KEY="tokenizer_name"
TRANSFORMED_DIR_KEY="transformed_dir"



DIALOGUE="dialogue"
SUMMARY="summary"
INPUT_IDS="input_ids"
ATTENTION_MASK="attention_mask"
LABELS="labels"

#model trainer constants
MODEL_TRAINER_CONFIG_KEY="model_trainer_config"
TRAINED_MODEL_DIR="trained_model"
MODEL_NAME_KEY="model_name"

PARAMS="params"