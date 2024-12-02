import os
import logging
import logging.config
import yaml

sourceFileName = 'input.txt'

def setLog(default_path='loggingConfig.yaml', default_level=logging.INFO):
    default_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), default_path)
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print('Error in logging configuration, using default configs')
                logging.basicConfig(level=default_level)
    else:
        print('Config file not found')
    return

def readData(sourceFileName: str) -> list:
    logger.info("Reading from source file.")
    sourceFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), sourceFileName)
    if os.path.exists(sourceFile):
        with open(sourceFile, 'rt') as f:
            try:
                data = f.read().splitlines()
            except Exception as e:
                logger.error(e)
    return data

def calcDiff(data: list) -> int:
    logger.info('Splitting into two lists')
    leftCol = []
    rightCol = []
    total = 0
    for line in data:
        leftCol.append(line.split()[0])
        rightCol.append(line.split()[1])
    if len(leftCol) != len(rightCol):
        logger.warning("List lengths don't match")
    logger.info('Sorting lists')
    leftCol.sort()
    rightCol.sort()
    lineCount = 0
    logger.info('Calculating total difference')
    while lineCount < len(leftCol):
        total +=  abs(int(leftCol[lineCount]) - int(rightCol[lineCount]))
        lineCount += 1
    return total

def main() -> None:
    data = readData(sourceFileName)
    logger.info(f'The total difference is {calcDiff(data)}')
    return

if __name__ == '__main__':
    logger = setLog()
    logger = logging.getLogger('__name__')
    logger.info('Logger set!')
    main()