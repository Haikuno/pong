from pygame import Rect
from pygame import draw

class MyRect():
    def __init__(self, *args) -> None:
        self.rect = Rect(args)

    def update() -> None:
        ...

    def draw(self,screen) -> None:
        draw.rect(screen, self.color, self.rect)