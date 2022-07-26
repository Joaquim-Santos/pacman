import pygame

from typing import Tuple

from src.colors import Colors
from src.screen import Screen


class PacMan:
    def __init__(self, block_size: int) -> None:
        self.__color = Colors().get_color('yellow')
        self.__radius = block_size // 2
        self.__pixel_width = 0
        self.__center = [self.__radius, self.__radius]
        self.__board_position = [1, 1]

        self.__mouth_points = None
        self.__mouth_color = Colors().get_color('black')
        self.__mouth_pixel_width = 0

        self.__eye_center = None
        self.__eye_color = Colors().get_color('black')
        self.__eye_radius = self.__radius // 10
        self.__eye_pixel_width = 0

        self.__speed = 0
        self.__movement_axis = 0
        self.__cell_length = block_size
        self.__target_positions = self.__board_position.copy()

        self.__set_center(0)
        self.__set_center(1)

    @property
    def target_positions(self) -> list:
        return self.__target_positions.copy()

    @property
    def board_position(self) -> list:
        return self.__board_position.copy()

    def verify_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.__speed = 1
                    self.__movement_axis = 0
                elif event.key == pygame.K_LEFT:
                    self.__speed = -1
                    self.__movement_axis = 0
                elif event.key == pygame.K_DOWN:
                    self.__speed = 1
                    self.__movement_axis = 1
                elif event.key == pygame.K_UP:
                    self.__speed = -1
                    self.__movement_axis = 1
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
                    self.__speed = 0

    def __set_mouth_points(self) -> None:
        self.__mouth_points = (
            self.__center,
            (self.__center[0] + self.__radius, self.__center[1]),
            (self.__center[0] + self.__radius, self.__center[1] - int(self.__radius * 0.7))
        )

    def __set_eye_center(self) -> None:
        self.__eye_center = (
                self.__center[0] + self.__radius // 3,
                self.__center[1] - int(self.__radius * 0.7)
        )

    def __set_center(self, axis: int) -> None:
        self.__center[axis] = (
                (self.__board_position[axis] * self.__cell_length) + self.__radius
        )

    def draw_pacman(self, screen: Screen) -> None:
        pygame.draw.circle(screen.game_screen, self.__color, self.__center,
                           self.__radius, self.__pixel_width)
        pygame.draw.polygon(screen.game_screen, self.__mouth_color, self.__mouth_points,
                            self.__mouth_pixel_width)
        pygame.draw.circle(screen.game_screen, self.__eye_color, self.__eye_center,
                           self.__eye_radius, self.__eye_pixel_width)

    def set_target_position(self) -> None:
        self.__target_positions[self.__movement_axis] += self.__speed

    def reset_target_position(self) -> None:
        self.__target_positions = self.board_position

    def walk(self) -> None:
        self.__board_position[self.__movement_axis] = self.__target_positions[self.__movement_axis]

        self.__set_center(self.__movement_axis)
        self.__set_mouth_points()
        self.__set_eye_center()
