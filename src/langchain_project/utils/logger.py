import sys
import logging 
import datetime
import os

LOG_DIR=os.path.join(os.getcwd(),"logs")

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE = datetime.now().strftime("%Y_%m_%d")+".log"
LOG_PATH= os.path.join(LOG_DIR,LOG_FILE)

logging.basicConfig(

    handlers=[logging.FileHandler(LOG_PATH)],
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"

)