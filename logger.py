import logging
from datetime import datetime
import os

LOG_PATH = f"{datetime.now().strftime("%m-%d-%y-%H-%M-%S")}.log"

log_file = os.path.join(os.getcwd(),"logs")

os.makedirs(log_file,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_file,LOG_PATH)


logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format="[%(asctime)s %(lineno)d %(name)s-%(levelname)s-%(message)s]")

