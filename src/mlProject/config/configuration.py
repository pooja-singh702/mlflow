# calling script constants that contain path to yaml file
from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import (DataIngestionConfig, DataValidationConfig)



## creating class configuration manager which will 
## initialise constants all 3 yaml file path, then it will initialise 3 var as self.config, ... for all 3 yaml files after reading it usin 
#funct read_yaml
# use create dir function from common to crearte artifact dir

class ConfigurationManager:
    def __init__(self,config_filepath= CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH,schema_filepath= SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion  # config.yml page data ingestion containg  var path

        create_directories([config.root_dir])  # now config is var containg contents of config.yaml 
                                               # and getting root dir from dataingestion written inside it

        


        ## configuring data ingestion files path using dataingestionconfig class
        # passing data to dataingetsionconfig to get paths of 4 var
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir= config.unzip_dir)

        return data_ingestion_config   #returning all 4 paths of root dir, source, zip , unzip

    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            unzip_data_dir= config.unzip_data_dir,
            all_schema= schema,

        )

        return data_validation_config
