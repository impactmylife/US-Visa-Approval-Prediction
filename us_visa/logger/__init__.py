import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m-%d_%Y_%H-%M-%S')}.log" # This helps to create different files for different timestamps

log_dir = "logs"

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(logs_path, exist_ok=True) # creating  directory

logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(name)s -%(levelname)s - %(message)s", # name of the log file, log level name, and message
    level = logging.DEBUG
)
