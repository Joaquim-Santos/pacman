import pygame
from src.screen import Screen
from src.pacman import PacMan


class Game:
    def __init__(self) -> None:
        self.__screen = Screen(800, 600)
        self.__continue_game = True
        self.__pacman = PacMan(self.__screen.get_dimensions())

    def _verify_events(self) -> None:
        if pygame.event.get(pygame.QUIT):
            self.__continue_game = False

    def _move_pacman(self) -> None:
        self.__pacman.walk(self.__screen, 0)

    def start(self) -> None:

        while self.__continue_game:
            self.__screen.fill()
            self._move_pacman()
            pygame.display.update()
            pygame.time.delay(100)

            self._verify_events()


Game().start()
