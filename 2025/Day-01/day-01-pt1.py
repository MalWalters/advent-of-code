import logging
from utils.logger_setup import setup_logger
from utils.fileLoader import return_list
from utils.vaultDial import VaultDial
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

    dialAtZero = 0
    dial = VaultDial()  # starts at 50

    for item in lines:
        logger.debug(f"dial.pos: {dial.position}")
        logger.debug(item)
        direction = item[:1]
        distance = int(item[1:])
        position, zero_crosses = dial.rotate(direction, distance)
        logger.debug(f"Position: {position}")
        if zero_crosses > 0:
            logger.info(f"crossed zero becuase {item}. Now at {position}")
            dialAtZero += zero_crosses
        elif position == 0:
            logger.debug(f"At zero becuase {item}")
            dialAtZero += 1

        logger.debug(f"Move {direction}{distance}: position={position}, zero_crosses={zero_crosses}")

    logger.info(f"Number of times the dial is at or passes through zero: {dialAtZero}")
    return dial.position


if __name__ == "__main__":
    main()
