import pygame

from typing import Tuple, List

from src.game_element import GameElement
from src.screen import Screen
from src.colors import Colors
from src.pacman import PacMan
from src.font import Font
from src.ghost import Ghost


class Scenery(GameElement):
    def __init__(self, length: int, pacman: PacMan, ghosts: List[Ghost]) -> None:
        pygame.init()

        self.__pacman = pacman
        self.__ghosts = ghosts

        self.__block_length = length
        self.__pill_id = 1
        self.__wall_id = 2
        self.__points = 0

        self.__matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

        self.__score_position = (
            (len(self.__matrix) + 1) * self.__block_length,
            50
        )

        self.__directions = {
            'up': 1,
            'down': 2,
            'right': 3,
            'left': 4
        }

    @staticmethod
    def __get_color(number: int) -> Tuple[int, int, int]:
        colors = {
            0: Colors().get_color('black'),
            1: Colors().get_color('white'),
            2: Colors().get_color('blue')
        }

        return colors[number]

    def __draw_object(self, x: int, y: int, object_type: int, screen: Screen) -> None:
        block = (x, y, self.__block_length, self.__block_length)
        color = self.__get_color(object_type)

        if object_type != self.__pill_id:
            pygame.draw.rect(screen.game_screen, color, block, 0)
        else:
            x += self.__block_length // 2
            y += self.__block_length // 2

            pygame.draw.circle(screen.game_screen, color, (x, y), self.__block_length // 10, 0)

    def draw(self, screen: Screen) -> None:
        for number_line, line in enumerate(self.__matrix):
            for number_column, column in enumerate(line):
                x = number_line * self.__block_length
                y = number_column * self.__block_length

                self.__draw_object(x, y, column, screen)

        self.__render_score(screen)

    def verify_events(self) -> None:
        if pygame.event.get(pygame.QUIT):
            exit()

    def __movement_is_allowed(self) -> bool:
        matrix_dimensions = [len(self.__matrix), len(self.__matrix[0])]
        target_positions = self.__pacman.target_positions
        line = target_positions[0]
        column = target_positions[1]

        in_matrix_dimensions = (0 <= line < matrix_dimensions[0]) and \
                               (0 <= column < matrix_dimensions[1])

        not_in_wall = (self.__matrix[line][column] != self.__wall_id)

        return in_matrix_dimensions and not_in_wall

    def __get_pill(self):
        target_positions = self.__pacman.target_positions
        line = target_positions[0]
        column = target_positions[1]

        if self.__matrix[line][column] == self.__pill_id:
            self.__matrix[line][column] = 0
            self.__points += 1

    def __render_score(self, screen: Screen) -> None:
        score_surface = Font("arial", 26)\
            .render_font(f"Score: {self.__points}", 'yellow')
        screen.game_screen.blit(score_surface, self.__score_position)

    def __get_ghost_possible_directions(self, ghost: Ghost) -> List[int]:
        ghost_positions = ghost.board_position
        ghost_y = ghost_positions[1]
        ghost_x = ghost_positions[0]

        possible_directions = []

        if self.__matrix[ghost_x][ghost_y - 1] != self.__wall_id:
            possible_directions.append(self.__directions['up'])
        if self.__matrix[ghost_x][ghost_y + 1] != self.__wall_id:
            possible_directions.append(self.__directions['down'])
        if self.__matrix[ghost_x - 1][ghost_y] != self.__wall_id:
            possible_directions.append(self.__directions['left'])
        if self.__matrix[ghost_x + 1][ghost_y] != self.__wall_id:
            possible_directions.append(self.__directions['right'])

        return possible_directions

    def apply_rules(self) -> None:
        self.__pacman.set_target_position()

        if self.__movement_is_allowed():
            self.__get_pill()
            self.__pacman.apply_rules()
        else:
            self.__pacman.reset_target_position()

        print(self.__get_ghost_possible_directions(self.__ghosts[0]))

    def run(self, screen: Screen):
        self.draw(screen)
        self.verify_events()
        self.apply_rules()

        self.__pacman.draw(screen)
        self.__pacman.verify_events()

        self.__ghosts[0].draw(screen)
