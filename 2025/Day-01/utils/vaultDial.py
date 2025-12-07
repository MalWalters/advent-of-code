from logger_setup import setup_logger

logger = setup_logger(__name__)

class VaultDial:
    def __init__(self, max_number=99):
        self.max_number = max_number
        self.position = 50

    def rotate(self, direction: str, distance: int):
        size = self.max_number + 1
        spinDir = 1 if direction.upper() == "L" else -1

        start = self.position
        unbounded_end = start + spinDir * distance

        # Correct zero-cross calculation
        if spinDir > 0:  # left/CCW
            zero_crosses = (unbounded_end // size) - (start // size)
        else:            # right/CW
            zero_crosses = (start // size) - (unbounded_end // size)

        zero_crosses = max(0, zero_crosses)

        # Wrap around
        self.position = unbounded_end % size

        return self.position, zero_crosses
