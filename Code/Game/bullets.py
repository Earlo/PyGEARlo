import os 

from . import unit

class bullet(unit.unit):
    def __init__(self, GAME, sprite):
        super().__init__(GAME, sprite = sprite) 
        self.damage = 1
        self.tile.append(self)

    def update(self):
        self.tile.remove(self)
        dx = self.vec[0] * self.speed
        dy = self.vec[1] * self.speed
        self.x += dx
        self.y += dy
        self.addToTile()
        self.tile.append(self)
        if (self.deathConditions()):
            self.remove()
        else:
            self.blit()

    def remove(self):
        self.GAME.ammo.remove(self)
        self.tile.remove(self)

class blast(bullet):
    sprites = [[os.path.join(os.path.dirname(os.path.realpath(__file__)),"assets", "player_shot1.png")],
                [os.path.join(os.path.dirname(os.path.realpath(__file__)),"assets", "enemy_shot1.png")]]
    def __init__(self, user, vec, s):
        super().__init__(user.GAME, sprite = self.sprites[s]) 
        self.hasHit = False
        self.user = user
        self.FLAGS.append("SHOT")
        self.side = user.side
        user.GAME.ammo.append(self)


        self.speed = 5
        self.vec = vec
                
        self.x = self.user.x
        self.y = self.user.y

    def hit(self):
        self.hasHit = True

    def deathConditions(self):
        #print(self.drawableRect())
        return self.GAME.AREA.isOut(self,0,0) or self.hasHit
