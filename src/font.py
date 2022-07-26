from typing import Union

import pygame

from pygame.surface import Surface, SurfaceType

from src.colors import Colors


class Font:

    def __init__(self, name: str, size: int) -> None:
        self.__name = name
        self.__size = size

    def render_font(self, text: str, color: str) -> Union[Surface, SurfaceType]:
        font = pygame.font.SysFont(self.__name, self.__size, True, False)
        return font.render(text, True, Colors().get_color(color))
