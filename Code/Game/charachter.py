import os
import collections
import math

import pygame

from pygame.locals import *

from . import unit
from . import bullets
from . import ritual
from . import effect

from ..Engine import events
fpath = os.path.dirname(os.path.realpath(__file__))

class charachter(unit.unit):
    sprite = [os.path.join(fpath,"assets", "energy1.png"),
            os.path.join(fpath,"assets", "energy2.png"),
            os.path.join(fpath,"assets", "energy3.png")]
    def __init__(self, GAME):
        super().__init__(GAME, sprite = self.sprite) 
        self.x = 300
        self.y = 500

        self.tail = [effect.energyTail(self.GAME,self.pos(),[self.sprite[2]]),
                     effect.energyTail(self.GAME,self.pos(),[self.sprite[2]]),
                     effect.energyTail(self.GAME,self.pos(),[self.sprite[1]]),
                     effect.energyTail(self.GAME,self.pos(),[self.sprite[1]]) ]  

        self.oldpos = collections.deque([self.pos()]*40, 40)
        self.side = "ALLY"

        self.weapon = blaster( self ) 

        self.speed = 3.0
        #self.surf.fill((10,10,150))
        self.hitbox = pygame.draw.circle(self.surf, (0,200,200), self.rect.center , 2, 0)


    def update(self):
        
        self.weapon.update()

        keys = pygame.key.get_pressed()
        dx,dy = 0,0
        if keys[K_UP]: dy-=self.speed
        if keys[K_DOWN]: dy+=self.speed
        if keys[K_LEFT]: dx-=self.speed
        if keys[K_RIGHT]: dx+=self.speed
        #print(self.y)
        self.oldpos.append(self.pos())

        n = len(self.tail)
        e = 7
        for t in self.tail:
            x, y = self.oldpos[int(e*-n)]
            y += n*e*(self.GAME.stage.scrollspeed() * 2)
            t.update(x,y)
            n -= 1

        dx,dy = self.GAME.AREA.checkBorders(self,dx,dy)

        if keys[K_z]:self.weapon.shoot()
        #if keys[K_c]:self.placeBeacon()

        #if keys[K_SPACE]: pygame.image.save(self.GAME.AREA.surf, "test")
        
        ##self.erase()
        self.x += dx
        self.y += dy
        self.addToTile()
        self.blit()

    def placeBeacon(self):
        self.GAME.effects.append( ritual.beacon( self.GAME, self.pos() ) )

class blaster():
    def __init__(self, user):
        self.user = user
        self.type = bullets.blast
        self.shotParam = ( self.user, [0,-1], 0)
        self.cooldown = 8
        self.load = 0
   
    def shoot(self):
        if (self.load == 0):
            self.type( *self.shotParam )
            self.load = self.cooldown

    def update(self):
        if self.load > 0:
            self.load -= 1

