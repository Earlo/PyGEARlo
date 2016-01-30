import pygame

from . import unit
from . import effect
from . import vector

from ..Engine import events


import os


class beacon(unit.unit):
    sprite = [os.path.join(os.path.dirname(os.path.realpath(__file__)),"assets", "energy3.png")]
    def __init__(self, GAME, pos):
        super().__init__(GAME, sprite = self.sprite) 
        self.onSpot = False
        self.side = "ALLY"
        self.x = pos[0]
        self.y = pos[1]

        #self.speed = 0.1
        self.speed = 1
        self.addToTile()
        #self.GAME.grid.highlight()
    
    def hit(self,bullet):
        pass


    def addToTile(self):
        r = self.GAME.AREA.grid.res

        a = max(min(int(self.x // r), len( self.GAME.AREA.grid.tiles ) - 1), 0)
        b = max(min(int(self.y // r), len(self.GAME.AREA.grid.tiles[0]) - 1), 0)

        if (not self.GAME.AREA.grid.tiles[a][b].occupied):
            self.tile = self.GAME.AREA.grid.tiles[a][b]

    def update(self):
        if (not self.onSpot):
            r = self.tile.grid.res
            p = [self.tile.pos[0]*r +0.5*r ,self.tile.pos[1]*r+0.5*r]
            if (vector.dis(self.pos(), p) < self.speed):
                self.x = p[0]
                self.y = p[1]
                self.onSpot = True
                self.tile.occupied = True
                if (self.tile.grid.centerpiece == None):
                    CIRCLE.start( self, self.tile.grid )
                    #self.tile.grid.set_cp(self)
                elif( not (self.tile.pos in CIRCLE.ctiles.values() )):
                    CIRCLE.reset()
                    self.kill()
                else:
                    CIRCLE.place(self)
            else:
                if self.tile.occupied:
                    m = 1
                else:
                    m = -1
                dx,dy = vector.uvector(self.pos(), p)
                #print(dx,dy, vector.dis(self.pos(), p))
                self.x += -m*dx*self.speed
                self.y += -m*dy*self.speed
                self.addToTile()
        #check these 
        if (self.deathConditions()):
            self.kill()
        else:
            self.blit()

    def kill(self):
        self.GAME.effects.remove(self)
        if self.onSpot:
            self.tile.occupied = False

    def deathConditions(self):
        #print(self.drawableRect())
        return (self.drawableRect().size == (0,0))

class circle():
    hexr =  [(-2,-1) , (-2,1) , (0,2) , (0,-2) , (2,1) , (2,-1)] 
    crect =  [(-2,-1) , (-2,1) , (2,1) , (2,-1)] 
    upt = [(-2,1) , (0,-2) , (2,1)] 
    downt =  [(-2,-1) , (0,2) , (2,-1)] 

    combos = [[-2,-1], [-2,1], [0,2],[0,0],[0,-2], [2,1], [2,-1] ]
    
    def __init__(self):
        self.ctiles = {}
        self.beacons =  []
        self.filled = []

    def start(self,cp,grid):
        x0,y0 = cp.tile.pos
        self.GAME = cp.GAME
        self.grid = grid
        grid.centerpiece = cp
        for x,y in self.combos:
            if (x0+x < 0 or y0+y < 0 or x0+x >= len(grid.tiles) or y0+y >= len(grid.tiles[0]) ):
                grid.centerpiece = None
                self.ctiles = {}
                cp.kill()
                break
            else:
                t = grid.tiles[x0 + x][y0 + y]
                self.ctiles[ (x,y) ] = t.pos
                #self.ctiles.append( t.pos )
                t.draw(cp.GAME.AREA.effectSurf, c = (255,255,100)) 

    def place(self, b):
        for key,t in self.ctiles.items():
            if t == b.tile.pos:
                self.filled.append(key)
                self.beacons.append(b)
        self.testConnections()


    def testConnections(self):
        if  all( point in self.filled for point in self.hexr):
            self.removeEffect()
            self.drawCIRCLE(self.upt)
            self.drawCIRCLE(self.downt)
        elif  all( point in self.filled for point in self.crect): #rect
            self.removeEffect()
            self.drawCIRCLE(self.crect)
        elif  all( point in self.filled for point in self.upt): #triup
            self.removeEffect()
            self.drawCIRCLE(self.upt)
        elif  all( point in self.filled for point in self.downt): #tridown
            self.removeEffect()
            self.drawCIRCLE(self.downt)
    def effect(self):
        print("something happened")


    def reset(self):
        self.removeEffect()
        #self.grid.centerpiece.GAME.AREA.effectSurf.set_colorkey()
        #self.grid.centerpiece.GAME.AREA.effectSurf.fill((0,0,0,0))
        #self.grid.centerpiece.GAME.AREA.effectSurf.set_colorkey((0,0,0,0))
        self.ctiles = {}
        self.filled = []
        for b in self.beacons:
            b.kill()
        self.beacons =[]
        self.grid.centerpiece.kill()
        self.grid.centerpiece = None

    def removeEffect(self):
        self.grid.centerpiece.GAME.AREA.effectSurf.set_colorkey()
        self.grid.centerpiece.GAME.AREA.effectSurf.fill((0,0,0,0))
        self.grid.centerpiece.GAME.AREA.effectSurf.set_colorkey((0,0,0,0))

    def drawTiles(self):
        x0,y0 = self.grid.centerpiece.tile.pos
        for x,y in self.combos:
                t = grid.tiles[x0 + x][y0 + y]
                t.draw(cp.GAME.AREA.effectSurf, c = (255,255,100)) 

    def drawCIRCLE(self, ctype):
        r = self.grid.res
        points = []
        for k in ctype:
            p = self.ctiles[k]
            points.append( (p[0]*r + r/2, p[1]*r + r/2) )
        surf = self.grid.centerpiece.GAME.AREA.effectSurf
        pygame.draw.polygon(surf, (20,20,200), points, 5)
        pygame.draw.polygon(surf, (100,100,255), points, 3)
        pygame.draw.polygon(surf, (200,200,255), points, 1)




CIRCLE = circle()
