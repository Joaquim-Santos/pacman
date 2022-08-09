import pygame

from pygame.event import Event
from typing import Tuple, List

from src.game_element import GameElement
from src.screen import Screen
from src.colors import Colors
from src.pacman import PacMan
from src.font import Font
from src.ghost import Ghost
from src.directions import Direction
from src.states import State


class Scenery(GameElement):
    def __init__(self, length: int) -> None:
        pygame.init()

        self.__pacman = PacMan(length)
        self.__ghosts = [
            Ghost(length, 'red'),
            Ghost(length, 'orange'),
            Ghost(length, 'pink'),
            Ghost(length, 'cyan')
        ]

        self.__state = State.PLAYING

        self.__block_length = length
        self.__pill_id = 1
        self.__wall_id = 2

        self.__points = 0
        self.__max_points = 0
        self.__lives = 5

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
        self.__lives_position = (
            (len(self.__matrix) + 1) * self.__block_length,
            100
        )

        self.__set_max_points()

    @staticmethod
    def __get_color(number: int) -> Tuple[int, int, int]:
        colors = {
            0: Colors().get_color('black'),
            1: Colors().get_color('white'),
            2: Colors().get_color('blue')
        }

        return colors[number]

    def __set_max_points(self):
        for line in self.__matrix:
            for column in line:
                if column == self.__pill_id:
                    self.__max_points += 1

    def __change_paused_playing_state(self) -> None:
        change_state = {
            State.PAUSED: State.PLAYING,
            State.PLAYING: State.PAUSED
        }

        try:
            self.__state = change_state[self.__state]
        except KeyError:
            pass

    def draw(self, screen: Screen) -> None:
        if self.__state == State.PLAYING:
            self.__draw_when_playing(screen)
        elif self.__state == State.PAUSED:
            self.__draw_when_playing(screen)
            self.__draw_when_paused(screen)
        elif self.__state == State.GAME_OVER:
            self.__draw_when_playing(screen)
            self.__draw_when_game_over(screen)
        elif self.__state == State.VICTORY:
            self.__draw_when_playing(screen)
            self.__draw_when_victory(screen)

    def __draw_object(self, x: int, y: int, object_type: int, screen: Screen) -> None:
        block = (x, y, self.__block_length, self.__block_length)
        color = self.__get_color(object_type)

        if object_type != self.__pill_id:
            pygame.draw.rect(screen.game_screen, color, block, 0)
        else:
            x += self.__block_length // 2
            y += self.__block_length // 2

            pygame.draw.circle(screen.game_screen, color, (x, y), self.__block_length // 10, 0)

    @staticmethod
    def draw_centred_text(screen: Screen, text: str) -> None:
        paused_surface = Font("arial", 26) \
            .render_font(text, 'yellow')
        paused_position = (
            (screen.game_screen.get_width() - paused_surface.get_width()) // 2,
            (screen.game_screen.get_height() - paused_surface.get_height()) // 2
        )
        screen.game_screen.blit(paused_surface, paused_position)

    def __draw_when_playing(self, screen: Screen) -> None:
        for number_line, line in enumerate(self.__matrix):
            for number_column, column in enumerate(line):
                x = number_line * self.__block_length
                y = number_column * self.__block_length

                self.__draw_object(x, y, column, screen)

        self.__render_score(screen)

        self.__pacman.draw(screen)

        for ghost in self.__ghosts:
            ghost.draw(screen)

    def __draw_when_paused(self, screen: Screen) -> None:
        self.draw_centred_text(screen, "PAUSED")

    def __draw_when_game_over(self, screen: Screen) -> None:
        self.draw_centred_text(screen, "GAME OVER")

    def __draw_when_victory(self, screen: Screen) -> None:
        self.draw_centred_text(screen, "VOCÊ VENCEU!!!")

    def verify_events(self, events: List[Event]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.__change_paused_playing_state()

        self.__pacman.verify_events(events)

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
        lives_surface = Font("arial", 26)\
            .render_font(f"Lives: {self.__lives}", 'yellow')

        screen.game_screen.blit(score_surface, self.__score_position)
        screen.game_screen.blit(lives_surface, self.__lives_position)

    def __get_ghost_possible_directions(self, ghost: Ghost) -> List[Direction]:
        ghost_positions = ghost.board_position
        ghost_y = ghost_positions[1]
        ghost_x = ghost_positions[0]

        possible_directions = []

        if self.__matrix[ghost_x][ghost_y - 1] != self.__wall_id:
            possible_directions.append(Direction.UP)
        if self.__matrix[ghost_x][ghost_y + 1] != self.__wall_id:
            possible_directions.append(Direction.DOWN)
        if self.__matrix[ghost_x - 1][ghost_y] != self.__wall_id:
            possible_directions.append(Direction.UP.LEFT)
        if self.__matrix[ghost_x + 1][ghost_y] != self.__wall_id:
            possible_directions.append(Direction.UP.RIGHT)

        return possible_directions

    def __verify_game_over(self, ghost: Ghost) -> bool:
        if self.__pacman.board_position == ghost.board_position:
            self.__lives -= 1
            self.__pacman.reset_board_position()

        return self.__lives == 0

    def __verify_victory(self) -> bool:
        return self.__points == self.__max_points

    def apply_rules(self) -> None:
        if self.__state == State.PLAYING:
            self.apply_rules_when_playing()
        elif self.__state == State.PAUSED:
            self.apply_rules_when_paused()
        elif self.__state == State.GAME_OVER:
            self.apply_rules_when_game_over()
        elif self.__state == State.VICTORY:
            self.apply_rules_when_victory()

    def apply_rules_when_playing(self) -> None:
        self.__pacman.set_target_position()

        if self.__movement_is_allowed():
            self.__get_pill()
            self.__pacman.apply_rules()
        else:
            self.__pacman.reset_target_position()

        for ghost in self.__ghosts:
            directions = self.__get_ghost_possible_directions(ghost)
            ghost.choice_direction(directions)
            ghost.apply_rules()

            if self.__verify_game_over(ghost):
                self.__state = State.GAME_OVER

        if self.__verify_victory():
            self.__state = State.VICTORY

    def apply_rules_when_paused(self) -> None:
        pass

    def apply_rules_when_game_over(self) -> None:
        pass

    def apply_rules_when_victory(self) -> None:
        pass

    def run(self, screen: Screen, events: List[Event]) -> None:
        self.verify_events(events)
        self.apply_rules()
        self.draw(screen)
