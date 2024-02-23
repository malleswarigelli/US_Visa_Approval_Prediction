import os
from pathlib import Path # create system compatible path

project_name = "US_Visa"


list_of_files=[

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",     
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    
    f"{project_name}/configuration/__init__.py", 
    f"{project_name}/constant/__init__.py", 
    
    f"{project_name}/entity/__init__.py", 
    f"{project_name}/entity/config_entity.py", 
    f"{project_name}/entity/artifact_entity.py", 
    
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logging.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",
      
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    
    
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
    
]

for file in list_of_files:
    filepath = Path(file) # creates your system compatible filepath (windows/mac/ubantu etc)
    filedir, filename = os.path.split(filepath)
    # if filedir not empty, create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # overwrite
    # if path doesn't exist or pathsize=0, create empty file
    if (not os.path.exists(filepath)) or (os.path.getsize==0):
        with open(filepath, 'w') as f:
            pass 
    else:
        print(f"file is already present at:{filedir}")