import logging

logger = logging.getLogger(__name__)

def rotateDial(startPosition: int, direction: str, distance: int ):
    """
    Accepts 3 char
    
    :param startPosition: Description
    :type startPosition: int
    :param instruction: Description
    :type instruction: str
    """

    dial_length = 100
    
    if direction == "L":
        currentPosition = startPosition - distance
        if currentPosition < 0:
            currentPosition = 100 + currentPosition
    else:
        currentPosition = startPosition + distance
        if currentPosition > 99:
            currentPosition -= 100
    return currentPosition