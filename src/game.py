import pygame
from src.screen import Screen
from src.pacman import PacMan
from src.scenery import Scenery


class Game:
    def __init__(self) -> None:
        self.__screen = Screen(800, 600)
        self.__cell_size = 600 // 30

        pacman = PacMan(self.__cell_size)
        self.__scenery = Scenery(self.__cell_size, pacman)

    def start(self) -> None:

        while True:
            self.__screen.fill()

            self.__scenery.run(self.__screen)

            pygame.display.update()
            pygame.time.delay(100)


if __name__ == '__main__':
    Game().start()
