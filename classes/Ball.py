from MyRect import MyRect
from const import *

class Ball(MyRect):
    def __init__(self, speed) -> None:
        super().__init__(0, 0, *BALL_SIZE)
        self.color = BALL_COLOR
        self.rect.center = (MAX_WINDOW_SIZE[0] // 2, MAX_WINDOW_SIZE[1] // 2)
        self.dir = [-speed, 0]
        self.speed = 3

    def reset(self, score, scorer) -> None:
        self.rect.center = (MAX_WINDOW_SIZE[0] // 2, MAX_WINDOW_SIZE[1] // 2)
        score.update(scorer)

    def update(self, objects, score) -> None:
        self.rect.move_ip(self.dir)

        if self.rect.top < WALL.top + MARGIN_SIZE:
            self.rect.top = WALL.top + MARGIN_SIZE
            self.dir = [self.dir[0], -self.dir[1]]
        elif self.rect.bottom > WALL.bottom:
            self.rect.bottom = WALL.bottom
            self.dir = [self.dir[0], -self.dir[1]]

        if self.rect.left < WALL.left:
            self.reset(score, "bot")
        elif self.rect.right > WALL.right:
            self.reset(score, "player")

        if self.rect.colliderect(objects["player"].rect):
            if objects["player"].dir[1] == PLAYER_SPEED:
                self.dir = [-self.dir[0], self.speed]
            elif objects["player"].dir[1] == -PLAYER_SPEED:
                self.dir = [-self.dir[0], -self.speed]
            else:
                self.dir = [-self.dir[0], self.dir[1]]

            self.rect.x = objects["player"].rect.right

        if self.rect.colliderect(objects["bot"].rect):
            if objects["bot"].dir[1] == BOT_SPEED:
                self.dir = [-self.dir[0], self.speed]
            elif objects["bot"].dir[1] == -BOT_SPEED:
                self.dir = [-self.dir[0], -self.speed]
            else:
                self.dir = [-self.dir[0], self.dir[1]]

            self.rect.x = objects["bot"].rect.left - BALL_SIZE[0]
