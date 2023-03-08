from MyRect import MyRect
from const import *
import pygame as pg

class Player(MyRect):
    def __init__(self) -> None:
        super().__init__(MARGIN_SIZE + WALL_SIZE[1], 0, *PLAYER_SIZE)
        self.color = PLAYER_COLOR
        self.dir = (0,0)
        self.rect.centery = MAX_WINDOW_SIZE[1] // 2

    def update(self) -> None:
        self.dir = (0,0)
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.dir = (0, -PLAYER_SPEED)
        if keys[pg.K_DOWN]:
            self.dir = (0, PLAYER_SPEED)

        self.rect.move_ip(self.dir)

        if self.rect.top < WALL.top + MARGIN_SIZE:
            self.rect.top = WALL.top + MARGIN_SIZE
        elif self.rect.bottom > WALL.bottom:
            self.rect.bottom = WALL.bottom


