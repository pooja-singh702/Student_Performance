## track all logs





import logging
import os
from datetime import datetime

# Create a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory path
logs_directory = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_directory, exist_ok=True)

# Complete path for the log file
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example log message
logging.info("Logging has started.")

#

# if __name__ =="__main__":
#         logging.info("loging has started")