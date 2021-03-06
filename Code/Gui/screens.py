from pygame import Surface as PSurf

from . import menu as m

from ..constants import *

from ..Game.game import game

def SMainMenu(PROGRAM):

    surf = PROGRAM.surf_GUI
    gui = []

    #menu_bar = m.menu_box(surf,PSurf(RelCord(surf,.6,.8)),RelCord(surf,.2,.1),(25,50,100), title = "Kuukyy")
    menu_bar = m.menu_box(surf, (.6,.8), (.2,.1), (25,50,100), title = "Kuukyy")

    buttons = []
    ps = menu_bar.surf
    buttons.append(m.button(ps, (.4,.2), (.3,.1), "Star program", [ONETIME,PROGRAM.load_GUI,SNewGAme]))
    buttons.append(m.button(ps, (.4,.2), (.3,.31), "GUI test", [ONETIME,PROGRAM.load_GUI,SGuiTest]))
    buttons.append(m.button(ps, (.2,.2), (.1,.62), "nothing1", [ONETIME,nothing], colour = [200,20,25]))
    buttons.append(m.button(ps, (.2,.2), (.35,.62), "nothing2", [ONETIME,nothing], colour = [20,25,200]))
    buttons.append(m.button(ps, (.2,.2), (.6,.62), "nothing3", [ONETIME,nothing], colour = [25,200,20]))

    menu_bar.add_widgets(buttons)
    gui.append(menu_bar)


    PROGRAM.GUI = gui

    
def SNewGAme(PROGRAM): #setup for the game
    PROGRAM.GAME = game(PROGRAM)
    CharSelect(PROGRAM)

def Sgame(PROGRAM):
#    PROGRAM.GAME.start()
    PROGRAM.GUI = PROGRAM.GAME.game_gui()
    PROGRAM.function = PROGRAM.GAME.game_loop

def CharSelect(PROGRAM):
    surf = PROGRAM.surf_GUI
    gui = []

    #menu_bar = m.menu_box(surf,PSurf(RelCord(surf,.6,.8)),RelCord(surf,.2,.1),(25,50,100), title = "Kuukyy")
    menu_bar = m.menu_box(surf, (.6,.8), (.2,.1), (25,50,100), title = "Kuukyy")

    buttons = []
    ps = menu_bar.surf
    buttons.append(m.button(ps, (.2,.2), (.1,.62), "nothing1", [ONETIME,nothing], colour = [200,20,25]))
    buttons.append(m.button(ps, (.2,.2), (.35,.62), "nothing2", [ONETIME,nothing], colour = [20,25,200]))
    buttons.append(m.button(ps, (.2,.2), (.6,.62), "nothing3", [ONETIME,nothing], colour = [25,200,20]))
    gui.append(m.button(surf,(.16,.08),(.01 ,.01 ),"Main menu",[ONETIME,PROGRAM.load_GUI,SMainMenu]))
    gui.append(m.button(surf,(.16,.08),(.74 ,.01 ),"Start Game",[ONETIME,PROGRAM.load_GUI,Sgame]))

    menu_bar.add_widgets(buttons)
    gui.append(menu_bar)

    PROGRAM.GUI = gui



def SGuiTest(PROGRAM): 
    PROGRAM.reset_GUI()

    gui = []
    surf = PROGRAM.surf_GUI

    menu_bar = m.scroll_menu_box(surf, (.9,.9), (.025,.025), (25,50,100), (1,2.4), title = "lel :-D" )
    buttons = []
    surf = menu_bar.surf

    string = "Menu"
    for x in range (5):
        for y in range(20):
            l = len(string)
            #gy = y + l
            #s = string + string * (y // l)
            s = string + string * y
            
            r = y % l
           # s += string[0:r]
            buttons.append(m.button(surf,(.165,.095),(.05 + .17*x,.05 + .1*y),s,[ONETIME,PROGRAM.load_GUI,SMainMenu]))
    
            #gui.append(m.button(surf,PSurf((100 + x*4 ,50 + x*2)),(100*x+x^2*4,50*y+y*2*x+y),s,[ONETIME,SMainMenu]))
    menu_bar.add_widgets(buttons)
    gui.append(menu_bar)
    PROGRAM.GUI = gui
        
