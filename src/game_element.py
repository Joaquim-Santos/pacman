from abc import ABCMeta, abstractmethod

from src.screen import Screen


class GameElement(metaclass=ABCMeta):

    @abstractmethod
    def draw(self, screen: Screen) -> None:
        pass

    @abstractmethod
    def verify_events(self) -> None:
        pass

    @abstractmethod
    def apply_rules(self) -> None:
        pass
