import os
from datetime import datetime




def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR=os.getcwd()
CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"




#training pipline constants
TRAINING_PIPELINE_CONFIG_KEY= "training_pipeline_config"
PIPELINE_NAME_KEY="pipeline_name"
ARTIFACT_DIR_KEY ="artifact_dir"



DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATASET_DOWNLOAD_URL_KEY="dataset_download_url"
DATA_INGESTION_ARTIFACT_DIR="data_ingestion"
ZIP_DATA_DIR_KEY="zip_data_dir"
INGESTED_DIR_KEY="ingested_dir"


#dataset dir
SAMSUM_DATASET="samsum_dataset"