from typing import Tuple


class Colors:
    def __init__(self) -> None:
        self.__colors = {
            'yellow': (255, 255, 0),
            'black': (0, 0, 0),
            'blue': (0, 0, 255),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'orange': (255, 165, 0),
            'pink': (255, 192, 203),
            'cyan': (0, 255, 255)
        }

    def get_color(self, color: str) -> Tuple[int, int, int]:
        return self.__colors[color]
