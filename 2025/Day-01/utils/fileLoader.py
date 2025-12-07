# fileloader.py
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def return_list(relative_path: str) -> list[str]:
    logger.debug(f'FileLoader looking for {relative_path}')
    base = Path(__file__).parent.parent  # go up to project/
    full_path = base / relative_path
    logger.debug(f'FileLoader looking for {full_path}')
    return full_path.read_text().splitlines()   
