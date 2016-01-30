import pygame



#clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

class unit():
    def __init__(self, GAME, sprite = None):
        self.FLAGS = []
        self.tile = None
        self.GAME = GAME
        if sprite == None:
            self.surf = pygame.Surface((32, 32))
            self.surf.fill((50,100,10))
        else:
            self.surf = pygame.image.load(sprite[0])
            self.surf.set_colorkey(self.surf.get_at((0, 0)))
        self.rect = self.surf.get_rect()
        self.hitbox = self.rect
        self.x = 0
        self.y = 0
        self.tile = self.GAME.AREA.grid.tiles[0][0]
        #self.tile.append(self)

    def addToTile(self):
        r = self.GAME.AREA.grid.res

        a = max(min(int(self.x // r), len( self.GAME.AREA.grid.tiles ) - 1), 0)
        b = max(min(int(self.y // r), len(self.GAME.AREA.grid.tiles[0]) - 1), 0)

        self.tile = self.GAME.AREA.grid.tiles[a][b]

    def collision(self): #really shit code, but will do
        for i in self.tile:
            if not i.side == self.side:
                if self.hitbox.move(*self.pos()).colliderect(i.hitbox.move(*i.pos())):
                    self.hit(i)

        
    def hit(self,bullet):
        self.hp -= bullet.damage
        bullet.hit()

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
        

        #game ares is flipped every time
        #if update:
        #    if area == None:
        #        area = self.drawableRect()
        #    else:
        #        area.move_ip((self.x,self.y)) #fix
        #    events.blit_request( area , self.surf)   #edit later     
