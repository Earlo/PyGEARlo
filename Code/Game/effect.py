
import os

import pygame

class effect():
    def __init__(self, GAME, time, pos):
        self.GAME = GAME
        self.time = time
        self.timer = 0 
        #self.sprites = sprite
        self.frame = 0
        self.dead = False

        self.surf = pygame.image.load(self.sprites[0])
        self.surf.set_colorkey(self.surf.get_at((0, 0)))

        self.rect = self.surf.get_rect()
        self.x = pos[0]
        self.y = pos[1]
        self.vec = [0,0]
        self.speed = 0
        
    def pos(self):
        return (self.x,self.y)

    def upleftPos(self): #upleft position
        return (self.x - self.surf.get_width()/2, self.y - self.surf.get_height()/2)

    def gPos(self):
        return [int(x + y) for x, y in zip(self.upleftPos(), self.GAME.AREA.c_rect.topleft)] 

    def erase(self):#does not work properly (?)

        self.blit(surf = self.GAME.PROGRAM.surf_VOID, area = self.rect)
        area = self.surf.get_rect().copy()
        area.topleft = self.gPos()
 
    def drawableRect(self):
        return self.GAME.AREA.rect.clip( self.rect.move(self.upleftPos()) )
       
    def blit(self, update = True, surf = None, area = None):
        if surf == None:
            surf = self.surf
        if not area == None:
            pos = [x + y for x, y in zip( self.gPos(), area.topleft)]
        else:
            pos = self.gPos()
        self.GAME.PROGRAM.surf_GAME.blit(surf, pos, area) #draw self on parent surface

    def update(self):
        self.timer += 1
        f = self.timer // self.time
        if not f == self.frame:
            if (f < len(self.sprites) ):
                self.frame = f  
                self.surf = pygame.image.load(self.sprites[self.frame])
                self.surf.set_colorkey(self.surf.get_at((0, 0)))
            else:
                self.dead = True



fpath = os.path.dirname(os.path.realpath(__file__))
class explosion(effect):
    sprites = [os.path.join(fpath,"assets", "explosion1.png"),
            os.path.join(fpath,"assets", "explosion2.png"),
            os.path.join(fpath,"assets", "explosion3.png"),
            os.path.join(fpath,"assets", "explosion4.png")]

    def __init__(self, GAME, pos):
        super().__init__(GAME, 2, pos)

    def update(self):
        super().update()
        dx = self.vec[0] * self.speed
        dy = self.vec[1] * self.speed
        self.x += dx
        self.y += dy
        if (self.dead):
            self.GAME.effects.remove(self)
        else:
            self.blit()

        
