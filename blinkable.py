from abc import ABC, abstractmethod


class Blinkable(ABC):
    @abstractmethod
    def blink(self):
        pass
