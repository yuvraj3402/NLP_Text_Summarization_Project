from collections import namedtuple



DataIngestionArtifact=namedtuple("DataIngestionArtifact",
                               ["samsum_dataset_dir"])


DataTransformationArtifact=namedtuple("DataTransformationArtifact",
                               ["transformed_samsum_dataset_dir",
                                "Tokenizer"])

ModelTrainerArtifact=namedtuple("ModelTrainerArtifact",
                               ["samsum_model",
                                "Tokenizer"])