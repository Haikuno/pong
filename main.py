import sys
sys.path.append('./classes')

from const import *
from Player import Player
from Bot import Bot
from Ball import Ball
# from Score import Score
#TODO: Implement score system.
import pygame as pg


surface = pg.Surface((1920, 1080))
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)

pg.display.set_caption(GAME_NAME)

clock = pg.time.Clock()
time = 0

player = Player()
bot = Bot()
ball = Ball(speed=5)
score = 0

objects = { "player": player,
            "bot": bot,
            "ball": ball
            }

running = True
while running:
    # Time
    time_now = pg.time.get_ticks()
    if time_now - time > TIME_STEP:
        time = time_now
        surface.fill(BACKGROUND_COLOR)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.VIDEORESIZE:
                screen = pg.display.set_mode((  event.w, event.h),
                                                pg.RESIZABLE)

        # Update objects
        player.update()
        bot.update(ball_dir=ball.dir)
        ball.update(objects, score)

        # Draw
        for object in objects.values():
            object.draw(surface)
        pg.draw.rect(surface, WALL_COLOR, WALL, 10)

        # Update screen
        scaled_surface = pg.transform.smoothscale(  surface,
                                                    (screen.get_width(), screen.get_height()))
        screen.blit(scaled_surface, (0, 0))
        pg.display.flip()
        clock.tick(MAX_FPS)
