import os
import logging
import logging.config
import yaml

def setLog(default_path='loggingConfig.yaml', default_level=logging.INFO):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    default_path = os.path.join(dir_path,default_path)
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

def main() -> None: 
    return

if __name__ == '__main__':
    logger = setLog()
    logger = logging.getLogger('__name__')
    logger.info('Logger set!')
    main()