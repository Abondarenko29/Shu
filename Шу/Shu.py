from colors import *
import pygame as pg

class OurSprites (pg.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = pg.transform.scale (pg.image.load (image), (45, 45))    
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Area (OurSprites):
    def move (self):
        keys = pg.key.get_pressed ()
        if keys[pg.K_LEFT] and self.rect.x >= 5:
            self.rect.x -= self.speed
        elif keys[pg.K_RIGHT] and self.rect.x <= 950:
            self.rect.x += self.speed

class TextArea (OurSprites):
    def __init__ (self):
        super().__init__ ()

class Label (OurSprites):
    def __init__ (self, amount):
        super().__init__  ()
        self.amount = amount

player = Area ("player.png", 500, 735, 3)

pg.init ()
window = pg.display.set_mode ((1000, 800))
pg.display.set_caption ("Шу")
pg.mixer.music.load ("music.ogg")
pg.mixer.music.play ()
fon = pg.transform.scale (pg.image.load("fone.jpg"), (1000, 800))
pip_effect = pg.mixer.Sound ("pip_effect.ogg")
clock = pg.time.Clock ()
game = True
amountGame = 0
while game:
    window.blit (fon, (0, 0))
    player.reset ()
    player.move ()
    for e in pg.event.get ():
        if e.type == pg.QUIT:
            game = False
    pg.display.update ()
    clock.tick (120)