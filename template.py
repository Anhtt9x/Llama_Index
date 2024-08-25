
import os
from pathlib import Path


list_of_files=[
    "src/__init__.py",
    "src/data_ingestion.py",
    "src/embedding.py",
    "src/model_api.py",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]


for file in list_of_files:
    file = Path(file)

    file_dir, file_name = os.path.split(file)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)

    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,"w")as f:
            pass 
    else:
        print("File already excist")