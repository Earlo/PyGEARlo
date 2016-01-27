
import calendar


from ..Gui import menu 

from .game_constants import *
from ..constants import *

##example of a really boring game
class game():
    def __init__(self,PROGRAM, save = None):
        self.PROGRAM = PROGRAM
        if save == None:
            self.start_game()
    
    def game_loop(self):
        self.calendar.pass_time(60)


    def start_game(self):
        self.calendar = game_calendar(self)

    def game_gui(self):
        surf = self.PROGRAM.surf_GUI
        self.top_bar = menu.menu_box(surf, (1,.15), (0.,0.), (50,50,50))
        text = self.calendar.get_date()
        self.datebox = menu.label(self.top_bar.surf, 1, (0.,0.), text)
        self.top_bar.add_widgets( [self.datebox] )

        #motivation_bar = menu.bar( self.top_bar.surf, (0.4, 0.05), (0.55, 0.05), "test", self.character , )


        return [self.top_bar]

    def chage_var(self,var):
        pass


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
        
