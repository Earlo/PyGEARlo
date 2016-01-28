
import calendar

import pygame
from pygame.locals import *



from ..Gui import menu 


from .game_constants import *
from ..constants import *
from ..Engine import events


##example of a really boring game
class game():
    def __init__(self,PROGRAM, save = None):
        self.PROGRAM = PROGRAM
        if save == None:
            self.start_game()

        self.char = charachter(self)

        r = self.PROGRAM.surf_BGR.get_rect()
        r.topleft = (0,0)
        events.blit_request(r, self.PROGRAM.surf_BGR)

    def game_loop(self):
        self.calendar.pass_time(60)
        self.char.update()

    def start_game(self):
        self.calendar = game_calendar(self)

    def game_gui(self):
        surf = self.PROGRAM.surf_GUI
        self.top_bar = menu.menu_box(surf, (1,.15), (0.,0.), (50,50,50))
        text = self.calendar.get_date()
        self.datebox = menu.label(self.top_bar.surf, 1, (0.,0.), text)
        self.top_bar.add_widgets( [self.datebox] )
        
        #self.pos = (0, self.top_bar.surf.get_height())

        #gamearea rect would work better



        return [self.top_bar]

    def chage_var(self,var):
        pass

class charachter():
    def __init__(self, GAME):
        self.GAME = GAME
        self.x = 0
        self.y = 0
        self.surf = pygame.Surface((8, 8))
        self.surf.fill((19,18,1))
        self.surf.set_colorkey((19,18,1))
        self.rect = pygame.draw.circle(self.surf, (0,200,200), (3,3) , 2, 0) 
    def update(self):
        keys = pygame.key.get_pressed()
        dx,dy = 0,0
        if keys[K_UP]: dy-=1
        if keys[K_DOWN]: dy+=1
        if keys[K_LEFT]: dx-=1
        if keys[K_RIGHT]: dx+=1
        
        self.erase()
        self.x += dx
        self.y += dy

        self.blit()


    def erase(self):
        self.blit(surf = self.GAME.PROGRAM.surf_VOID) #erase self
       
    def blit(self, update = True, surf = None, area = None):
        if surf == None:
            surf = self.surf
        if not area == None:
            pos = [x + y for x, y in zip( (self.x,y), area.topleft)]
        else:
            pos = (self.x,self.y)
        self.GAME.PROGRAM.surf_GAME.blit(surf, pos, area) #draw self on parent surface
 
        if update:
            if area == None:
                area = self.surf.get_rect().copy()
                area.topleft = (self.x,self.y)
            else:
                area.move_ip((self.x,self.y))
            events.blit_request(area, self.GAME.PROGRAM.surf_GAME)   #edit later     
    
class game_calendar():
    def __init__(self, GAME, year = START_YEAR, month = START_MONTH, day = START_DAY, hour = START_HOUR, minute = START_MIN):
        self.GAME = GAME
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def pass_time(self, added_m = 0):
        added_h = 0
        m = int( self.minute )
        h = int( self.hour )
        m += added_m
        while (m >= 60):
            m -= 60
            added_h += 1
        h += added_h
        while (h >= 24):
            h -= 24
            self.next_date( )

        if m >= 10:
            self.minute = str( m )
        else:
            self.minute = "0" + str( m )
        if h >= 10:
            self.hour = str(h)
        else:
            self.hour = "0" + str( h )

        self.GAME.datebox.change_text( self.get_date( ) )
        self.GAME.top_bar.draw( )
        self.GAME.top_bar.blit( )
        
    def next_date(self):
        d = int( self.day )
        m = int( self.month )
        y = int( self.year )
        d += 1
        if d > calendar.monthrange( y, m )[ 1 ]:
            d = 1
            m += 1
            if m == 13:
                m = 1
                y += 1
        self.day = str( d )
        self.month = str( m )
        self.year = str( y )

    def get_date(self):
        loc = self.GAME.PROGRAM.language
        wd = loc.weekday( calendar.weekday( int(self.year), int(self.month), int(self.day) ) )
        d = loc.date( self.day, self.month, self.year )
        t = self.hour + ":" + self.minute #make more generic later
        return [wd, d, t]
        
