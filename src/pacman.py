import pygame

from typing import Tuple

from src.colors import Colors
from src.screen import Screen


class PacMan:
    def __init__(self, screen_dimensions: Tuple[int, int]) -> None:
        self.__color = Colors().get_color('yellow')
        self.__radius = screen_dimensions[0] // 40
        self.__pixel_width = 0
        self.__center = [self.__radius, self.__radius]

        self.__mouth_points = None
        self.__mouth_color = Colors().get_color('black')
        self.__mouth_pixel_width = 0

        self.__eye_center = None
        self.__eye_color = Colors().get_color('black')
        self.__eye_radius = self.__radius // 10
        self.__eye_pixel_width = 0

        self.__speed = 0.2
        self.__max_positions = [screen_dimensions[0], screen_dimensions[1]]

    def __set_mouth_points(self) -> None:
        self.__mouth_points = (
            self.__center,
            (self.__center[0] + self.__radius, self.__center[1]),
            (self.__center[0] + self.__radius, self.__center[1] - self.__radius)
        )

    def __set_eye_center(self) -> None:
        self.__eye_center = (
                self.__center[0] + self.__radius // 3,
                self.__center[1] - int(self.__radius * 0.7)
        )

    def walk(self, screen: Screen, axis: int) -> None:
        bigger_than_max = (self.__center[axis] + self.__radius) > self.__max_positions[axis]
        smaller_than_zero = (self.__center[axis] - self.__radius) < 0

        if bigger_than_max or smaller_than_zero:
            self.__speed = -self.__speed

        self.__center[axis] += self.__speed
        self.__set_mouth_points()
        self.__set_eye_center()

        pygame.draw.circle(screen.game_screen, self.__color, self.__center,
                           self.__radius, self.__pixel_width)
        pygame.draw.polygon(screen.game_screen, self.__mouth_color, self.__mouth_points,
                            self.__mouth_pixel_width)
        pygame.draw.circle(screen.game_screen, self.__eye_color, self.__eye_center,
                           self.__eye_radius, self.__eye_pixel_width)
