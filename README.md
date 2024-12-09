# End to End MLOP Project

```
Steps:
1. initialing Git hub
2. create virtual env "venv" using commnad: conda create -p venv python=3.8 -y and activate using "conda activate D:\MLOP_Project_new\venv. 
3. Create file structure: create template.py and create file structure. on runnning, all files subfolders wete created along with log info.
4. Add libraries on requirements.txt
5. Create setup.py to create modules of ur project. 
6. For that create src folder with __inint__ which is recognised by setup.py and will conatin all files and structure of our project.
7. Connect requirements.txt to setup.py using "-e ." such that whenever requirements is run, set up script runs
8. Run Requirements.txt to install all libraries using commnad "pip install -r requirements.txt"
9. create utils and custom logger
10. create custom log inside src __init__.py.
    10: a: Create log config inside __init__.py of src folder instead creating seperate logger.py file inside src folder. It helps in easy acees like in import without mentioning src in import.
    10:b:Logging in __init__.py
           Setup:
           Configure logging in the __init__.py file of your src folder using logging.getLogger("mlprojectlogger").Usage:
           In your main scripts (e.g., main.py), simply import the logger and use functions like logger.info() or logger.error().
           Benefits:
           Package-Level Configuration: Shared logging setup across multiple modules.
           Ease of Access: Access the logger directly from the package without needing a separate import.
    10:c: Inside __init__.py of src folder, use get logger():
            Logging in Our Project
                Advantages of Using getLogger(__name__)
                    1. Module-Specific Logging: Each module can have its own logger, allowing for tailored logging configurations.
                    2. Independent Configurations: You can set different logging levels for each module. For example, one module can log detailed DEBUG information, while another can log only WARNING messages.
                    3. Controlled Propagation: Log messages can be managed hierarchically. For instance, a child logger can log at a lower level, while a parent logger only captures higher-level messages.4. 
                    
                    4. Traceability: Using __name__ in the logger name automatically includes the module's name, making it easier to identify where log messages are coming from.
                    5. Flexible Logging: You can create distinct loggers for various parts of your application, giving you precise control over what gets logged where.

                What Happens If You Don’t Use getLogger(__name__)
                    Uniform Logging Level: If the same logger is used across all modules, every script will log at the same level. This limits the ability to differentiate between log messages in different contexts.

                    Lack of Diversity: Without unique loggers, you can't have distinct configurations for different parts of your application, complicating log management.

                    Centralized Configuration: You may end up with a single logging setup for the entire application, which can lead to either too much information or not enough in critical areas.

                Setting Up Logging in __init__.py
                    In the __init__.py file of our project, we set up the logging configuration. This includes creating a directory for log files and setting up handlers for console output. This centralized setup allows different modules to use their own loggers while still maintaining a cohesive logging strategy.

```
```
step 02: Data Validation:
1. check Data before training
2. We checked for schema(features/ columns in data should be in schema.yaml)
3. For this, created schema.yaml file such that it contains all columns of data withtheir data type. (used data.info to get all information). Since data is clean and has no missing values, so didnot include in it. You can include check data types in ur file.
4. First, tried the data validation process on a notebook (data_validation.ipynb) 
        a. created Config.yaml file under config which contains yaml structure with data validation containing 3 variables path.(root dir for creating data_validation folder under artifacts , wine data unzip, status_file as status.txt file created inside data_validation which gives status of validation as true or false if data col matches schema columns  )

        b. then, created class for datavalidationconfig, containg  4 var types used in thos process. root_dir: Path , STATUS_FILE: str, unzip_data_dir: Path, all_schema: dict

5. Created configurationmanager.py inside configuration, it contains:
         a. read all yaml data: config, schema. create directoriers artifacts, data_validation
         b. def getdataconfiguration, will return all var as datavalidationconfig
         c. after reading , def getconfig, will initialise self.config as config file and get alll variables defined under it for datavalidation to get paths.
         d. also initialised self.schema after reading schema yaml file to get all colunns as dict.
         e. return all 4 var in datavalidation config as path
6. created "class datavalidation" inside src/componemts in which we will check all columns and creats status.txt file and returns status txt file created inside data_validation folder as yes or no.

7. then created pipeline as DataValidationTrainingPipeline:, under which created stage 02 data validation, which contains sequence in which these scripts are called. it contain main.py under which steps  are defined as config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
8. created main.py, which calls datavalidationpipeline.

```
```
Problems encountered
1. Requirements.txt: installing rust, cargo:
My virtual env did not recognise env path set for rustc, cargo
Solution:
Set the path inside my virtual env venv by using command: set PATH=%USERPROFILE%\.cargo\bin;%PATH%

```
########################################
STEP 1: TEMPLAYE.PY: STRUCTURING FILES AND CREATING EMPTY FILES AND FOLDERS and prints logging 
IMPORT LIBRARIES(OS, PATHLIB, LOGGING) 
ININTIALISE LOOGING USING BASIC CONFIG WITH LEVEL AS LOGING AND DAT FORMAT
THEN PROJECT NAME: "MLPROJECT"
LIST OF FILES: ALL FOLDERS OR FILES U NEED TO CREATE.STRUCTURING THE PROJECT FILES.EG : f"src/{project_name}/__init__.py. till prokect name is folder then file
ALL  UNDER GITHUB THEN WORKFLOW FOLDER. UNDER PATH(FILELINK, ), EXTRACT FILEDIR, FILENAME FROM LINK IN LIST IF FILES


stepb: requirements.txt(list of lib) and add - e .
stepc: setup.py: for ur project local package installation . meaning project changed to package


stepc: created logging under src constructor file: __init__.py instaed crating seperating folder. used logging filehandler and stramhandler

stepc: when u use constructor for lohhher fike, u can call it directly .instead src.mlproject.logger.py
u can write mlproject.logger.py.helps in seeing error

stepd: utils.py(under src- mlprokject):
purpose: those code which is all time used like read write. using @ensure_annotations as decorator , dir create funct, save, load, get size all basic ones. used config box for getting dict items using .
ALSO USED DECOATOR, WHICH CHEKS THE DATA TYPE LIKE EG WHILE IPOUT U GAVE WRONG DATA TYPE, THEN ERROR, SO ENSURE ANNOTATIONS, HELPS TP RESOLVE THIS AND IT CHECKS . @ENSURE_ANNNOTATION: PARAMETER TYPE CHECKS, OVER ANY METHOD U CAN MENTION IT.


STEPE: UPDATE CONFIG.YAML FILE : contains path to data folder and path to it local folder.
CREATE ARTIFACTS FOLDER CONATING ALL FOLDERS: DATASET
FOR DATA INGESTION PROCESS, CREATED VAR WITH LINK AS THEIR VALUE
VAR ARE : ROOT DIR: LINK TO IT , SOURCE URL: LINK FOR DATSET, LOCAL DATAFILE: ARTIFACTS/DATA_INGESTION/DATA.ZIP, UNZIP_DIR: artifacts/data_ingetsion. data u get is zip, unzipped file is then put under unzip dir.
STEPH: UPDATE THE ENITITY FOLDER : DEFINING CLASS DATAINGESTIONCONFIG: DEFINES Data TYPE OF VAR IN CONFIG 
used dataclass and pathlib. here dataclass is used as decoratir and is not python. in ython as we need to define var as self. var .. using dataclass, it get initialised on its own no need to write. used wen its not  gonna change like here u r just passing type of data var(root dir, source url, localdatafile, unzip dir) all those var defined in config. here return type of var and function is defined like root dir is path type, souurce url is str an dthese are return type of function 

NOTE: PATH CLASS: PATH(ARTIFACT/DATA) HELPS TO PEVENT ERROR FROM / WEN U PROVIDE PATH. SO GOOD TO USE

STEP I : UPDATE CONSTANTS.PY : IN OUR PROJECT WE HAVE 3 YAML FILES. THIS CONSTANTS.PY FILE CONTAINS PATH OF THESE FILES.HERE WE USE PATHLIB AND ITS  PATH TO DEFINE YAML FILES PATH. THERE ARE 3 YAML FILES DFEINED: CONFIG.YAML, PARAMS.YAML, SCHEMA.YAML. WE ARE DEFINING PATH OF THESE YAML FILES. THIS IS IMPORTED DUTING DATA INGETSION.

STEP: COMMON.PY: IT HAS ALL COMMON FUMCTIONS DEFINED: READYAML(PATH TO YAML), CREATE_DIRECTORIES(PATH)....

STEP: CONFIG FOLDER:(DIFF FROM YAML FILE): IT HAS CONFIGURation.py file: here 
1. u will read all 3 files. for that u will use common.py to use readyaml() to read yaml files.(config, schema, )

STEP F: UPDATE SCHEMA.YAML: used in validation


STEPG: UPDATE PARAMS.YAML
STEPH: UPDATE THE ENITITY folder: 
THIS FOLDER has "config_entity.py" file
it has all 4 var with their data tyoe defined. remember no path yet just data type
STEPI: UPDATE THE CONFIGURATION MANAGER IN SRC CONFIG
STEPJ: UPDATE THE COMPAONENTS
STEPK: UPDATE THE PUPELINE
STEPL: UPDATE THE MAIN.PY
STEPK: UPDATE THE DVC.YAML
UPDATE APP.PY

FOR DATA TO BE STORED AT DIFF TIMES:
FIRTS AT DATA INGESTION 
DATA VALIDATION
DATA 

NOW TO STORE THEM, WE ARE CREATING ARTIFACTS FOLDER, INSUDE IT 
WE WILL CREATE 3 DIFF FOLDERS BY NAME OF COMPONENTS:
DATA INGETSION
DATA VALIDATION
---

INSIDE THESE, AT DIFF LEVELS DATA WILL BE STORED.
DATA INGESTION: U GET DATA FROM SOURCE AND STORE IT IN DATA INGETION FOLDER UNDER ARTIFACTS

SLY, DATA VALIDATION: VALIDATED DATA GOES UNDER BY CREATIN DATA VALIDATION FOLDER AND INSIDE DATA I SSTORED

HOW DATA WILL BE CALLED AND HOW PATH WILL BEDEFINED:
1. AT DATA INGETION STAGE: DATA FROM SOURCE IS CALLED, ITS IN ZIP FILE FORMAT, SO IT IS UNZIPED HERE AND UNZIPED FILE IS STORED UNDER ARTIFCATS/ DATA INGETSION FOLDERS. 

2. HERE FOR THESE PURPOSES:
A. CONFIG.YAML IS CREATED UNDER CONFIG FOLDER
B. CONFIG FOLDER IS CREATED WHICH CONTAINS CONFIGURATION.PY FILE

CONFIG.YAML: IT HAS 4 SECTIONS AND EACH SECTIONS HAS PATH DEFINED FRO THEIR RESPECTIVE DATA, FOLDER, DIR PATH TO BE CREATED LOCALLY
SECTION 1: PATH OF ARTIFACTS FOLDER
SECTION2: DATA INEGSTION PATHS: ROOT DIR, SOURCE, ZIP, UNZIP: UNZIP IS FINALLY STORED AT ARTIFACTS/DATAINGESTION FOLDER, DATAINGESTION IS FOLDER.

SECTION3: DATA VALIDATION
SECTION 4: DATA TRANSFORMATION


PROCESS OF DATA INGETSION:
1. class DataIngestionConfig: GET DATA TYPE OF ALL 4 VAR: ROOT DIR, SOURCE, ZIP, UNZIP USING ENTITY CONFIG_ENTITY. First we will define data datype of var being usd.

2.  # Initialize the ConfigurationManager
    config = ConfigurationManager() : this class is defined under configurayion.py under config. it reads all 3 yaml files: config,yaml, schena.yaml, ....
    For this:
    1.first it will use configuration.py class named as ConfigurationManager()
    which first reads all yaml file.
    2. to read the file here, it uses commons.py functions(readyaml(path to yaml))
    3. now path to yaml file is given using all paths defined at constant.py
    which all 3 files path defined.
    4. u provide this path to readyaml() and this is stored as self.config = , self.schema,
    5. to remember, our config.yaml file contains path defined for all folders and files requird at data ingestion an ddata validation , data validation.
    6. for data ingetsion, it has 4 var defined: root dir, source url, zip, unzip dir
    and main dir artifacts where all these folders and files go.
    7. for data ingestion stage, under artifacts, data ingestion folder is created, then unzip data is stored ata that location ie : artifacts/ data ingetsion.
    8. so once u get these files content, inside configurayion.py and under this class configurationmanager(), we define method : class getdataingestionconfig() -> dataingestionconfig class. this class is defined under config)entity.py under entity which coantins path to these variables. so return type of getdataingstionconfig is that class dataingestionconfig so all 4 var is returend from this class method.

    9: in this method or class: we will initialise config var by "dataingestion"
    which is a class defined at config.yaml files. it has path to these var. as these method alsready read config.yaml file content and initialised as config, using that we can get datingestion, and all that 4 var 

    10. also before this, dir artifact is created using common.py method create dir([list of path])

    11. final :  def get_data_ingestion_config(self) -> DataIngestionConfig: this return all 4 var withtheir paths defined

    12. Then we call class data ingestion() and its methods defined at data ingetsion.py. 
    13. this file has 3 methods: first u get all 4 var paths
    14. it has 2 methods: download file, extract file : which is then called to get data and finally unzip data is stored at artifacts/ dataingetsion as data.zip and winequality.csv

    14 update pipeline: sequence u did data ingestion(): like all sequence with mainand logger(), raise exception

    #########################################################################

data validatation stage: schema validate
1. stage1: updat config.yaml file by adding data validation and paths of each var , which is used in data cofigurationmanager() getdatavalidation() method where u inilise the var to this class to get all their paths and also define this method return as dataingetsionconfig class, which defines data type of this variables.
2. STAGE1 2: update schema.yaml: get all var in col with data types using python info() and paste it here. 
Create it as dictionalary : columns: 
                            column name: data type
target column :
name: quality

NOTE : U CAN REMOVE MISIING AND ALL. AS ALL CLEANED SO NOT DOING

3. STAGE2: UNDER CONFIG_ENTITY DEFINE ANOTHER CLASS AS DATAVALIDATION CONFIG:
WHICH WILL CONTAIN DATA TYPES OF THESE VARIBALES:
A. ROOT_DIR: DATA TYPE PATH
B: STATUS_DILE: TEXT
C: UNZIP DATA DIR: PATH
D: ALL SCHEMA: DICT


4. STAGE3: FOR THIS, U NEED TO UPDATE CONFIGURATIONMANAGER() UNDER CONFIGURATIO.PY UNDER CONFIG: 1. SAME READ YAML IFLES FOR CONFIG, SCHEMA,  PARAMS 
AND CREATE ROOT DIR ARTIFACTS
2. THEN DEFINE GET_DATA_VALIDATION_CONFIG() METHOD UNDER CONFIGURATIONMANAGER() AND IN WHICH we will define all 4 var defined at datavalidation config class and its return type is datavalidationconfig: so u get paths of all these 4 now.


4. once you get all these paths through calling getdatavalidationconfig() , now we call validation.py file which has methods like validateallcolumns() to check col type correct and then if true returns status txt file inside data valiation folder created under artifacts. status.txt return = true or false 

4. create pipeline using main.py() and add sequences it works, logger, eception

#########################################################################
# DATA TRANSFORMATION
SUMMARY /: # update config.yaml for data transformation
# step2: update entities like data class fr datatransformation config
# update configuration manager 

STAGE1: UDATE CONFIG.YAML FILE ADDIING DATA TRANSFORATION PART WHICH HAS PATHS TO ITS VAR DEFIND. HERE 2 VAR ARE DEFINE

STAGE2: UPDATE CONFIG_ENTITY UNDER OTHER  CONFIG FOLDER WHERE U ADD DATATRANSFORMATIONCONFIG() CLASS TO ADD DATA TYPES OF THE VAR DEFINED AT CONFIG.YAML.

STAGE3: UPDATE CONFIGURATIONMANAGER() AT CONFIGURATION.PY :
1. UNDER CONFIGURATIONMANGER() CLASS, ADD ANOTHER METHOD GETDATATRANSFORMATION() CLASS OF RETURN TYPE DATATRANSFORMATIONCONFIG CLASS, WHICH IS DEFINED AT CONFIGENTITY FOR DATATYPE DEFINING . HERE 2 VAR IS DEFINED AND RETURNING.

2. AFTER RETURNING AND GETTING THESE 2DATA PATHS , WE WILL CALL DATAVALIDATION.PY WHERE METHODS WILL 

note: at configuration.py, inside class configurationmanger(), initialisation for reading all 3 yaml will be there, creating dir artifat will be there, then defination get data tansformation will return 2 var path : root dir is used to create data validation folder under artifasts. and data path var is reading data wibe quality.

keeping all things same just class data transformation will intilaise these var and do train test split and save it under root dir 

summary:
entity(configentity) : add datatransformationconfig: contains return as data types of var root dir, data 

##################################################
MLFLOW: For prediction and reports, used mlflow at prediction.py or prediction pipeline  used dagshub for moving reports metrics from local server to cloud and attached git hub to dagshub for data versioning and many.

app.py: USE: When u try to change and experiment with prediction results using 
diff paramater eg changing alpha or l1 ratio at params.yaml u get diff results and versions at mlflow report. Now to make it easier for user, we make an app.py using flask and then used index.html results.html for user to input and get results using get /post. 

Containerised using Docker: 

Deployed this docker to EC2


#######################################################
De
##############################################################

## STEPS FOR MODEL TRAING USING MLFLOW

#### STEPS:
Clone the repo 
```bash
https://github.com/pooja-singh702/mlflow
```

## create a conda enviroment after opening the repo

``` bash
conda create -n mlproj python=3.8 -y
conda activate mlproj
```

## Step-02: install the requirements
```bash
pip install -r requirements.txt
```


## Step-02: install the requirements
```bash
pip install -r requirements.txt

```


## final run command
```bash
python app.py
```
Now, 
open local host and port

## Step-02: install the requirements
```bash
pip install -r requirements.txt
```


## Step-02: install the requirements
```bash
pip install -r requirements.txt
```

######################FINAL VERSION#########################################

# MLOps Project Structure

Welcome to the **MLOps Project** repository! This project follows best practices for Machine Learning Operations (MLOps), ensuring reproducibility, automation, and scalability of machine learning models.

Below is an overview of the **project structure** that defines how we organize code, data, models, and configurations for seamless collaboration and deployment.

## Project Structure Overview

```plaintext
.
├── .github/
│   └── workflows/
│       └── mlops-pipeline.yml  # GitHub Actions workflow file to automate the pipeline
├── artifacts/
│   ├── Data_Ingestion/         # Raw data from the ingestion stage
│   │   ├── data.zip/           # Raw data (zipped)
│   │   ├── winequality-red.csv # Raw dataset
│   ├── Data_Validation/        # Folder containing data validation outputs
│   │   ├── status.txt/         # Validation status or logs
│   │   ├── components/         # Components for the validation logic (if any)
│   └── Model_Evaluation/       # Model evaluation results
│       ├── metrics.json/       # JSON file storing model evaluation metrics (accuracy, AUC, etc.)
├── src/
│   └── mlProject/              # Main source code for the project
│       ├── __init__.py/        # Initialization file for mlProject
│       ├── data_ingestion.py/  # Data ingestion logic for collecting raw data
│       ├── data_transformation.py/ # Transformation of raw data to prepare for modeling
│       ├── data_validation.py/  # Validation of data to check quality and integrity
│       ├── model_evaluation.py/ # Logic for evaluating the model performance
│       ├── model_trainer.py/   # Script for training the machine learning model
│       └── utils/              # Utility functions like logging, config loading, etc.
│           └── common.py       # Common utility functions
├── config/
│   ├── configuration.py/      # Configuration for paths, model parameters, etc.
├── entity/
│   ├── config_entity.py/      # Configuration entity with paths or parameters for models and data
├── constants/
│   ├── __init__.py/           # Constants used throughout the project (e.g., file paths)
├── pipeline/
│   ├── prediction.py/         # Script for generating predictions using the trained model
│   ├── stage_01_data_ingestion.py/ # Data ingestion script for raw data collection
│   ├── stage_02_data_validation.py/ # Data validation script to check data integrity
│   ├── stage_03_data_transformation.py/ # Transformation of raw data into a usable format
│   ├── stage_04_model_training.py/    # Model training script
│   ├── stage_05_model_evaluation.py/  # Model evaluation script to evaluate model performance
└── .github/
    ├── workflows/
        ├── main.yaml/         # Defines the overall pipeline stages and automation in GitHub Actions


```















