from typing import Tuple


class Colors:
    def __init__(self) -> None:
        self.__colors = {
            'yellow': (255, 255, 0),
            'black': (0, 0, 0)
        }

    def get_color(self, color: str) -> Tuple[int, int, int]:
        return self.__colors[color]
