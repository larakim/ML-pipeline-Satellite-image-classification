import logging
import os
import sys


log_format = "['%(asctime)s':'%(levelname)s':'%(module)s':'%(message)s']"

log_dirs = "logs"
log_filepath = os.path.join(log_dirs,"running_logs.log")
os.makedirs(log_dirs,exist_ok=True)


logging.basicConfig(
    format=log_format,
    level= logging.INFO,
    handlers= [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger("Img_classif_logger")
