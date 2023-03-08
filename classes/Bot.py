from const import *
from Player import Player

#TODO: Make bot beatable

class Bot(Player):
    def __init__(self) -> None:
        super().__init__()
        self.color = BOT_COLOR
        self.rect.x = MAX_WINDOW_SIZE[0] - MARGIN_SIZE * 6

    def update(self, ball_dir) -> None:
        self.dir = (0, ball_dir[1])
        self.rect.move_ip(self.dir)

        if self.rect.top < WALL.top + MARGIN_SIZE:
            self.rect.top = WALL.top + MARGIN_SIZE
        elif self.rect.bottom > WALL.bottom:
            self.rect.bottom = WALL.bottom