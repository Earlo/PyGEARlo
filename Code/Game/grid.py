
import pygame

class grid():
    def __init__(self,size,res):

        self.surf = pygame.Surface(size)

        self.size = size
        self.res = res
        x = int(size[0]/res)
        y = int(size[1]/res)

        self.tiles = []

        self.centerpiece = None

        self.surf.fill((255,255,255))
        self.surf.set_alpha(120)

        for a in range(x):
            self.tiles.append([])
            for b in range(y):
                self.tiles[a].append(tile(self, [a,b] ) )
                #self.tiles[-1].draw(self.surf)


class tile(list):
    def __init__(self,grid,pos):
        self.occupied = False
        self.grid = grid
        self.pos = pos
    def draw(self, surf, c=[100,100,100]):
        pygame.draw.rect(surf, c, (self.pos[0]*self.grid.res,self.pos[1]*self.grid.res,self.grid.res,self.grid.res), 1)


