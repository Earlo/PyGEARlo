
import calendar

import pygame
from pygame.locals import *

import os



from ..Gui import menu 

from . import charachter
from . import enemy
from . import grid


from .game_constants import *

from ..constants import *
from ..Engine import events


##example of a really boring game
class game():
    def __init__(self,PROGRAM, save = None):
        self.PROGRAM = PROGRAM
        if save == None:
            self.start_game()


    def game_loop(self):
        self.AREA.update()
        #print(len(self.effects), len(self.units), len(self.ammo) ) 
        for e in self.effects:
            e.update()
        for u in self.units:
            u.update()
        for a in self.ammo:
            a.update()
        self.stage.update()

    def start_game(self):

        self.AREA = gameArea( self, self.PROGRAM.surf_GAME, (.7,.90), (0.05,0.05) )       

        self.char = charachter.charachter(self)
        self.units = [self.char]
        self.ammo = []
        self.effects = []

        self.stage = stage0(self)
        #self.calendar = game_calendar(self)

    def game_gui(self):
        surf = self.PROGRAM.surf_GUI

        self.bgr = menu.menu_box(surf, (.75,1), (0.,0.), (1,1,1))
        self.side_bar = menu.menu_box(surf, (.25,1), (0.75,0.), (1,1,1),title = "game stats here")

        #text = self.calendar.get_date()
        #self.datebox = menu.label(self.top_bar.surf, 1, (0.,0.), text)
        #self.top_bar.add_widgets( [self.datebox] )
       
        #events.blit_request(self.AREA.c_rect, self.PROGRAM.surf_BGR)

        return [self.bgr,self.side_bar]


class gameArea(menu.widget):
    sprite = [os.path.join(os.path.dirname(os.path.realpath(__file__)),"assets", "BGR_0.png")]
    def __init__(self, GAME, parent_surf, rsurf, rpos):
        super().__init__() 
        self.rsurf = rsurf
        self.rpos = rpos
        self.content = []
        self.adjust(parent_surf)

        self.rect = self.surf.get_rect() #is the size of the gamearea


        self.surf = pygame.image.load(self.sprite[0])
        #self.surf.set_colorkey((255,1,1))
        
        self.effectSurf = pygame.Surface(self.rect.size)
        self.effectSurf.fill((0,0,0,0))
        self.effectSurf.set_colorkey((0,0,0,0))

        self.grid = grid.grid( self.rect.size, 40 )

        self.scroll = +self.rect.h-self.surf.get_height()
        #self.scrollspeed = .1

        self.GAME = GAME

    def adjust(self, p_surf, parent = None):
        self.adjust_p(p_surf, parent)
        self.adjust_r()

    def update(self):
        self.blit()
        self.scroll += self.GAME.stage.scrollspeed()
        if (self.scroll == 0):
            self.GAME.stage.scrollON = 0
        #print(self.scroll)

    def checkBorders(self,unit,dx,dy):
        if self.checkX( unit, dx):
            dx = 0
        if self.checkX( unit, dy):
            dy = 0

        return dx, dy

    def checkX(self, unit, dx):
        return ( (unit.x - unit.rect.w/2 + dx < 0) or (unit.x + unit.rect.w/2 + dx > self.rect.w) )

    def checkY(self, unit, dy):
        return ( (unit.y - unit.rect.h/2 + dy < 0) or (unit.y + unit.rect.h/2 + dy > self.rect.h) )

    def isOut(self, unit, dy, dx):
        return self.checkX(unit, dx) or self.checkY(unit, dy)

    def blit(self, update = True, surf = None, area = None):
        if surf == None:
            surf = self.surf
        if not area == None:
            pos = [x + y for x, y in zip(self.relative_position(), area.topleft)]
        else:
            pos = self.relative_position()[:]
        pos[1] += self.scroll
        self.parent_surf.blit(surf, pos, area) #draw self on parent surface
 
        if update:
            if area == None:
                area = self.rect.copy()
                #area.topleft = pos
                area.topleft = self.relative_position()[:]
            else:
                area.move_ip(self.relative_position())
            events.blit_request(area,self.parent_surf)   #edit later
            self.parent_surf.blit(self.effectSurf, area.topleft )
            #events.blit_request(area,self.parent_surf)   #edit later

import math
class stage0():
    def __init__(self,GAME):
        self.GAME = GAME
        self.step = 0
        self.scrollON = 1
        self.cooldown = 20
        self.state = False

        self.logic()
    def update(self):
        self.logic()
        self.cooldown -= 1
        self.step += 1

    def scrollspeed(self):
        return self.scrollON*(1)
        #return math.sin(self.step/20)**2

    def logic(self):
        if len(self.GAME.units) < 6 and self.cooldown < 1:
            if self.state:
                e = enemy.enemy1(self.GAME)
            else:
                e = enemy.enemy1(self.GAME)
            self.state = not self.state
            self.cooldown = 10
            self.GAME.units.append(e)

def XtoYinZ(x,y,z,step):
    return(x + y - (step - z) )