import pygame

from typing import Tuple

from src.colors import Colors
from src.screen import Screen


class PacMan:
    def __init__(self, screen_dimensions: Tuple[int, int]) -> None:
        self.__color = Colors().get_color('yellow')
        self.__radius = screen_dimensions[0]/40
        self.__pixel_width = 0
        self.__position = [int(self.__radius), int(self.__radius)]
        self.__speed = 0.1
        self.__max_position_x = screen_dimensions[0]
        self.__max_position_y = screen_dimensions[1]

    def walk_horizontal(self, screen: Screen) -> None:
        if (self.__position[0] + self.__radius) > self.__max_position_x or (self.__position[0] - self.__radius) < 0:
            self.__speed = -self.__speed

        self.__position[0] += self.__speed
        self._walk(screen)

    def walk_vertical(self, screen: Screen) -> None:
        if (self.__position[1] + self.__radius) > self.__max_position_y or (self.__position[1] - self.__radius) < 0:
            self.__speed = -self.__speed

        self.__position[1] += self.__speed
        self._walk(screen)

    def _walk(self, screen: Screen) -> None:
        pygame.draw.circle(screen.game_screen, self.__color, self.__position,
                           self.__radius, self.__pixel_width)
