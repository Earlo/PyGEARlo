
import math

from . import bullets
from . import vector

class movePattern0():
    def __init__(self, owner):
        self.owner = owner
        self.current = 0
        self.step = 0.02
        # 1, -1
        self.overflow = 90
        self.reset = -90


    def iterate(self):
        S = math.copysign(1,self.current)
        x = math.cos(math.sin(self.current))**2
        y = S*math.sin(math.sin(self.current))**2
        
        self.owner.x += x*self.owner.speed
        self.owner.y += y*self.owner.speed

        self.current += self.step
        if math.fabs((self.current)) > self.overflow:
            bullets.blast( self.owner, [0,1], 1 )

            self.step = -self.step

class movePattern1():
    def __init__(self,owner):

        self.owner = owner #olento joka seuraa ohjelmaa # voit kommentoida pois testatessa

        #voit keksiä minkä tahansa nimisiä muuttujia tässä joita voit hyödyntää algorytmissäsi
        self.suunnat = [[2,0],[0,1],[-1,0],[0,-1]]
        self.current = 0
        self.counter = 0
        self.overflow = 30


    def iterate(self):
        S = math.copysign(1,self.current)
        

        x, y = self.suunnat[ self.current ]     

        #print(x,y)
        #voit myös kommentoida nämä kaksi riviä pois testatessa   
        self.owner.x += x*self.owner.speed
        self.owner.y += y*self.owner.speed

        self.counter +=1
        if (self.counter % self.overflow == 0): #jos counterin jakojäännös overflowsta on 0
            bullets.blast( self.owner, [0,1], 1 )
            self.counter = 0
            self.current += 1
            if (self.current % len(self.suunnat) == 0):
                self.current = 0

class movePattern2():
    def __init__(self,owner):

        self.owner = owner #olento joka seuraa ohjelmaa # voit kommentoida pois testatessa

        #voit keksiä minkä tahansa nimisiä muuttujia tässä joita voit hyödyntää algorytmissäsi
        self.suunnat = [[2,0],[0,1],[-1,0],[0,-1]]
        self.current = 0
        self.counter = 0
        self.overflow = 30


    def iterate(self):
        S = math.copysign(1,self.current)
        

        x, y = self.suunnat[ self.current ]     

        #print(x,y)
        #voit myös kommentoida nämä kaksi riviä pois testatessa   
        self.owner.x += x*self.owner.speed
        self.owner.y += y*self.owner.speed

        self.counter +=1
        if (self.counter % self.overflow == 0): #jos counterin jakojäännös overflowsta on 0
            bullets.blast( self.owner, [0,1], 1 )
            self.counter = 0
            self.current += 1
            if (self.current % len(self.suunnat) == 0):
                self.current = 0


class movePattern3():
    def __init__(self,owner):

        self.owner = owner #olento joka seuraa ohjelmaa # voit kommentoiis testatessada po
        #voit keksiä minkä tahansa nimisiä muuttujia tässä joita voit hyödyntää algoryäsitmiss

        self.suunnatToY = [[0,2],[0, -2]]
        self.suunnatToX = [[2, 0],[-2,0]]
        self.current = 0
        self.counter = 0
        self.overflow = 1




    def iterate(self):
        playerY = self.owner.GAME.char.y
        playerX = self.owner.GAME.char.x

        S = math.copysign(1,self.current)
        x = self.owner.x
        y = self.owner.y

        v = vector.uvector(self.owner.pos(), self.owner.GAME.char.pos())


       # if(math.fabs(playerX - x) >= math.fabs(playerY - y)):
       #     if(playerX - x >= 0):
       #         x, y = self.suunnatToX[0]
       #     else:
       #         x, y = self.suunnatToX[1]
       # else:
       #     if(playerY- y >= 0):
       #         x, y = self.suunnatToY[0]
       #     else:
       #         x, y = self.suunnatToY[1]

        #print(x,y)
        #voit myös kommentoida nämä kaksi riviä pois testatessa
        self.owner.x += v[0]*self.owner.speed
        self.owner.y += v[1]*self.owner.speed

        self.counter +=1
        #if (self.counter % self.overflow == 0): #jos counterin jakojäännös overflowsta on 0
         #   bullets.blast( self.owner, [0,1], 1 )
         #   self.counter = 0
         #   self.current += 1
         #   if (self.current % len(self.suunnat) == 0):
         #       self.current = 0
