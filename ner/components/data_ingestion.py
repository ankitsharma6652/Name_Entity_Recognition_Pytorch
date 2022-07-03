from linecache import cache
from datasets import load_dataset
from ner.exception.exception import CustomException
from ner.entity.config_entity import DataIngestionConfig
from ner.config.configurations import Configuration
import logging
import sys
import pandas as pd
from ner.constants import ARTIFACTS_KEY,DATA_STORE_KEY
import os

logger = logging.getLogger(__name__)
# print(__name__)


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        logger.info(" Data Ingestion Log Started ")
        self.data_ingestion_config = data_ingestion_config

    def get_data(self):
        try:
            """
            This is class is responsible for data collection from official hugging face library.
            Cross-lingual Transfer Evaluation of Multilingual Encoders (XTREME) benchmark called WikiANN or PAN-X.
            Returns: Dict of train test validation data 
            """
            # Task Implement save data to artifacts/data_store , write check if data already exists there
            # if not then only fetch from load_dataset
            logger.info(f"Loading Data from Hugging face ")
            print(os.path.join(ARTIFACTS_KEY,DATA_STORE_KEY))
            pan_en_data = load_dataset(self.data_ingestion_config.dataset_name,
                                       name=self.data_ingestion_config.subset_name,cache_dir=os.path.join(ARTIFACTS_KEY,DATA_STORE_KEY))
            logger.info(f"Dataset Info : {pan_en_data}")
            print(pan_en_data['train'])

            return pan_en_data

        except Exception as e:
            message = CustomException(e, sys)
            logger.error(message.error_message)


if __name__ == "__main__":
    project_config = Configuration()
    ingestion = DataIngestion(project_config.get_data_ingestion_config())
    print(ingestion)
    ingestion.get_data()
