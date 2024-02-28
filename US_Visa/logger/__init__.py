import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
print('log_dir:',LOG_FILE)

log_dir = "logs"

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok=True)
print('log_dir:',log_dir)

logging.basicConfig(
    filename=logs_path,
    level=logging.DEBUG,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    
)