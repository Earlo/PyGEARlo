

from . import unit
from . import bullets
from . import patterns
from . import effect


from ..Engine import events


import os
    
class enemy0(unit.unit):
    sprite = [os.path.join(os.path.dirname(os.path.realpath(__file__)),"assets", "enemy_1_smaller.png")]
    def __init__(self, GAME):
        super().__init__(GAME, sprite = self.sprite) 

        self.side = "ENEMY"

        self.hitbox = self.surf.get_bounding_rect()
        self.hp = 2
        self.isInside = False
                
        self.pattern = patterns.movePattern0(self)

        self.x = -32
        self.y = 50

        self.speed = 2.2

    def update(self):

        self.pattern.iterate()
        self.addToTile()
        if not self.isInside:
            self.isInside = not self.GAME.AREA.isOut(self,0,0)

        self.collision()
        if (self.deathConditions()):

            self.GAME.units.remove(self)
            if self.hp < 1:
                self.GAME.effects.append( effect.explosion( self.GAME, self.pos() ))
        else:
            self.blit()

    def deathConditions(self):
        #print(self.drawableRect())
        return (self.hp < 1) or (self.drawableRect().size == (0,0) and self.isInside)

class enemy1(enemy0):
    def __init__(self, GAME):
        super().__init__(GAME)
        self.pattern = patterns.movePattern1(self)




