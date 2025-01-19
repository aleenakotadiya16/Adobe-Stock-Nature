import os
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import pandas as pd


@dataclass
class DataIngestionConfig:
    train_data_path:str= os.path.join('artifacts','train.csv')
    test_data_path:str= os.path.join('artifacts','test.csv')
    Raw_data_path:str= os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("ingestion started")
        try:
            df= pd.read_csv(r"C:\Users\Aleena\Adobe stock pize\Data\data.csv")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.Raw_data_path,index=False,header=True)
            logging.info("Raw data saved")

            train_set,test_set= train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            logging.info("train data saved")
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("test data saved")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

        
