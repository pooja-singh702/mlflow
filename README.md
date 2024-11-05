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
