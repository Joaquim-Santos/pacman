import pygame
from src.screen import Screen
from src.pacman import PacMan
from src.scenery import Scenery


class Game:
    def __init__(self) -> None:
        self.__screen = Screen(800, 600)
        self.__cell_size = 600 // 30
        self.__continue_game = True

        pacman = PacMan(self.__cell_size)
        self.__scenery = Scenery(self.__cell_size, pacman)

    def _verify_events(self) -> None:
        if pygame.event.get(pygame.QUIT):
            self.__continue_game = False

    def _move_pacman(self) -> None:
        self.__scenery.verify_events()
        self.__scenery.move_pacman(self.__screen)

    def start(self) -> None:

        while self.__continue_game:
            self.__screen.fill()
            self.__scenery.build(self.__screen)
            self._move_pacman()
            pygame.display.update()
            pygame.time.delay(100)

            self._verify_events()


Game().start()
