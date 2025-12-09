import logging
from utils.logger_setup import setup_logger
from utils.fileLoader import return_list

import os

logger = setup_logger(level=logging.INFO)

data_source = 'data/input.csv'

def main():
    try:
        lines = return_list(data_source)
    except FileNotFoundError:
        logger.warning("File does not exist or is empty")
        return

    logger.debug(f"Input file contains {len(lines)} lines")

if __name__ == "__main__":
    logger.info("Starting the application")
    main()
