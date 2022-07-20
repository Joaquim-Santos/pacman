import pygame

from pygame.surface import Surface
from typing import Tuple

from src.colors import Colors


class Screen:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

        self.__game_screen = pygame.display.set_mode((width, height))
        self.__color = Colors().get_color('black')

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def game_screen(self) -> Surface:
        return self.__game_screen

    def get_dimensions(self) -> Tuple[int, int]:
        dimensions = (self.width, self.height)
        return dimensions

    def fill(self) -> None:
        self.game_screen.fill(self.__color)
