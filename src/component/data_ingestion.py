# read the data from the data source 

import os 
import sys # custom exception
from src.exception import CustomException 
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass 
class DataIngestionConfig: 
    # these are the inputs that i am giving to my data ingestion component 
    # and now data ingestion component knows where to save the train path , test path ,and data path 

    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # this ingestion_config consist of these 3 values
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try :
            df =pd.read_csv('Notebook/data/stud.csv')
            logging.info('reading the dataset as a dataframe- df')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index = False, header = True)
            logging.info("Train Test split intiated")

            train_set, test_set = train_test_split(df, test_size =0.2,random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False, header = True)

            test_set.to_csv(self.ingestion_config.test_data_path,index = False, header = True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
        
            )

            
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__== "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


    
