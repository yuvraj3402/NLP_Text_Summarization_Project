from collections import namedtuple



TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])



DataIngestionConfig=namedtuple("DataIngestionConfig",
                               ["dataset_download_url",
                                "zip_data_dir",
                                "ingested_data_dir"])



DataValidationConfig=namedtuple("DataValidationConfig",
                               ["status_file_path",
                                "required_files"])


DataTransformationConfig=namedtuple("DataTransformationConfig",
                               ["Tokenizer",
                                "transformed_data_dir"])



ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_dir",
                                                       "model_config_file_path",
                                                       "model_name",
                                                       "Tokenizer_path",
                                                       "saved_model_path"])