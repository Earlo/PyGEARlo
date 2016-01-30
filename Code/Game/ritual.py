
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
                print( len(CIRCLE.ctiles),(self.tile in CIRCLE.ctiles) )
                if (self.tile.grid.centerpiece == None):
                    CIRCLE.start( self, self.tile.grid )
                    #self.tile.grid.set_cp(self)
                elif( not (self.tile in CIRCLE.ctiles)):
                    CIRCLE.reset()
                    self.kill()
                print( self.tile == CIRCLE.ctiles[0])

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
    points = [[0,0],[2,0],[1,2]]
    x = points
    combos = [[-2,-1], [-2,1], [0,2],[0,0],[0,-2], [2,1], [2,-1] ]
    
    def __init__(self):
        self.ctiles = []

    def start(self,cp,grid):
        x0,y0 = cp.tile.pos

        grid.centerpiece = cp
        print(x0,y0)
        for x,y in self.combos:
            if (x0+x < 0 or y0+y < 0 or x0+x >= len(grid.tiles) or y0+y >= len(grid.tiles[0]) ):
                grid.centerpiece = None
                self.ctiles = []
                cp.kill()
                break
            else:
                t = grid.tiles[x0 + x][y0 + y]
                self.ctiles.append(t)
                t.draw(cp.GAME.AREA.surf, c = (255,255,100)) 


    def effect(self):
        print("something happened")
    def reset(self):
        print("you dun goofed")

CIRCLE = circle()
