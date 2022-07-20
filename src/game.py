import pygame
from src.screen import Screen
from src.pacman import PacMan


class Game:
    def __init__(self) -> None:
        self.__screen = Screen(640, 480)
        self.__continue_game = True
        self.__pacman = PacMan(self.__screen.get_dimensions())

    def _verify_events(self) -> None:
        if pygame.event.get(pygame.QUIT):
            self.__continue_game = False

    def _move_pacman(self) -> None:
        self.__pacman.walk_vertical(self.__screen)

    def start(self) -> None:

        while self.__continue_game:
            self.__screen.fill()
            self._move_pacman()
            pygame.display.update()

            self._verify_events()


Game().start()