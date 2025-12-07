import logging
import os
from pathlib import Path

def setup_logger(name='VaultLogger', log_file_name='vault_log.txt', level=logging.INFO):
    """
    Sets up a logger that writes to a log file in a 'logs' directory next to the script
    and also outputs to the console.
    """
    # Get the directory of the current script
#    script_dir = os.path.dirname(os.path.realpath(__file__)).parent

    script_path = Path(__file__).resolve()  # full path to script
    script_dir = script_path.parent.parent   # parent of the script folder


    # Create 'logs' subdirectory
    logs_dir = os.path.join(script_dir, 'logs')
    os.makedirs(logs_dir, exist_ok=True)

    # Full path to the log file
    log_file_path = os.path.join(logs_dir, log_file_name)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # prevent double logging if imported multiple times

    # Check if handlers already exist (avoid duplicate logs)
    if not logger.handlers:
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # File handler
        file_handler = logging.FileHandler(log_file_path, mode='w')
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
