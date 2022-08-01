import pygame

from src.game_element import GameElement
from src.colors import Colors
from src.screen import Screen


class Ghost(GameElement):
    def __init__(self, block_size: int, color: str) -> None:
        self.__color = Colors().get_color(color)
        self.__board_position = [7, 6]
        self.__size = block_size

    @property
    def board_position(self) -> list:
        return self.__board_position.copy()

    def draw(self, screen: Screen) -> None:
        ghost_slice = self.__size // 8
        pos_x = self.__board_position[0] * self.__size
        pos_y = self.__board_position[1] * self.__size

        shape = [
            (pos_x, pos_y + self.__size),
            (pos_x + ghost_slice, pos_y + (2 * ghost_slice)),
            (pos_x + (2 * ghost_slice), pos_y + (ghost_slice // 2)),
            (pos_x + (3 * ghost_slice), pos_y),
            (pos_x + (5 * ghost_slice), pos_y),
            (pos_x + (6 * ghost_slice), pos_y + (ghost_slice // 2)),
            (pos_x + (7 * ghost_slice), pos_y + (ghost_slice * 2)),
            (pos_x + self.__size, pos_y + self.__size),
        ]

        inner_eye_ray = ghost_slice // 2
        outer_eye_ray = ghost_slice

        left_eye_pos = (
                pos_x + (ghost_slice * 2.5),
                pos_y + (ghost_slice * 2.5)
        )
        right_eye_pos = (
            pos_x + (ghost_slice * 5.5),
            pos_y + (ghost_slice * 2.5)
        )

        outer_eye_color = Colors().get_color('white')
        inner_eye_color = Colors().get_color('black')

        pygame.draw.polygon(screen.game_screen, self.__color, shape, 0)

        pygame.draw.circle(screen.game_screen, outer_eye_color, left_eye_pos, outer_eye_ray, 0)
        pygame.draw.circle(screen.game_screen, inner_eye_color, left_eye_pos, inner_eye_ray, 0)
        pygame.draw.circle(screen.game_screen, outer_eye_color, right_eye_pos, outer_eye_ray, 0)
        pygame.draw.circle(screen.game_screen, inner_eye_color, right_eye_pos, inner_eye_ray, 0)

    def verify_events(self) -> None:
        pass

    def apply_rules(self) -> None:
        pass
