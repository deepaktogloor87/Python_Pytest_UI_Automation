import os
import logging
import datetime


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Determine the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Get the directory one level up from the project root
    parent_directory = os.path.dirname(project_root)

    # Ensure the 'logs' directory exists within the parent directory
    logs_dir = os.path.join(parent_directory, "logs")
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Formatter with filename
    formatter = logging.Formatter('%(asctime)s -  %(name)s - %(filename)s - %(funcName)s -%(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Dynamic filename for the log file based on the current date and time, saved within the 'logs' directory
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(logs_dir, f"apollo_logs_{current_time}.log")

    file_handler = logging.FileHandler(file_name)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
