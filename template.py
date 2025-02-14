import os
from pathlib import Path 
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name="WasteClassification"

list_of_files=[".github/workflows/.gitkeep",
               "data/.gitkeep",
               f"{project_name}/__init__.py",
               f"{project_name}/components/__init__.py",
               f"{project_name}/components/model_trainer.py",
               f"{project_name}/components/data_ingestion.py",
               f"{project_name}/components/data_validation.py",
               f"{project_name}/constant/__init__.py",
               f"{project_name}/constant/training_pipeline/__init__.py",
               f"{project_name}/constant/application.py",
               f"{project_name}/entity/config_entity.py",
               f"{project_name}/entity/artifacts_entity.py",
               f"{project_name}/entity/data_entity.py",
               f"{project_name}/exception/__init__.py",
               f"{project_name}/logger/__init__.py",
               f"{project_name}/pipeline/__init__.py",
               f"{project_name}/pipeline/training_pipeline.py",
               f"{project_name}/pipeline/prediction_pipeline.py",
               f"{project_name}/utils/__init__.py",
               f"{project_name}/utils/main_utils.py",
               "templates/index.html",
               "app.py",
               "Dockerfile",
               "requirements.txt",
               "setup.py"	
              ]

for file in list_of_files:
    file_path = Path(file)
    filedir,filename=os.path.split(file)
    if filedir!="":	
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating director {filedir} for file {filename}")

    if(not os.path.exists(filename) or (os.path.getsize(filename)==0)):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating file {filename}")
    else:
        logging.info(f"File {filename} already exists")
