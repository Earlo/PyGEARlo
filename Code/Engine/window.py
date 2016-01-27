
import pygame
from ..constants import *


class window_handler():
    def __init__(self):
        self.w = SWIDTH
        self.h = SHEIGTH
        self.create_surfaces()

        self.needs_resize = False
        self.last_resie_request = 0

        self.updates = {}

        self.GUI = []

        from ..Gui import screens
        self.load_GUI( screens.SMainMenu )

    def create_surfaces(self): #TODO reconsider this
        #self.MainWindow = pygame.display.set_mode((self.w, self.h), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
        self.MainWindow = pygame.display.set_mode((self.w, self.h), pygame.DOUBLEBUF|pygame.RESIZABLE)
        
        self.surf_GUI = pygame.Surface((self.w, self.h)) #GUI surface
        self.MainWindow.blit(self.surf_GUI,(0,0))
        self.surf_GUI.set_colorkey((0,0,0))
        self.surfaces = {}
        self.surfaces[self.surf_GUI] = 0 #surface is a key for it's draw depht
        #self.surfaces["GUI"] = [self.surf_GUI, 0] #surface is a key for it's draw depht

    def refresh_GUI(self):
        for wid in self.GUI:
            wid.draw()
            wid.blit()

    def reset_GUI(self):
        self.surf_GUI.set_colorkey(None)

        self.surf_GUI.fill((0,0,0))
        self.MainWindow.blit(self.surf_GUI,(0,0))
        self.surf_GUI.set_colorkey((0,0,0))

        #self.surf_GUI = pygame.Surface((self.SWIDTH, self.SHEIGTH))
        self.GUI = []
        self.active_text_field = None
        #pygame.display.flip()

    def load_GUI(self,GUI):
        self.reset_GUI()

        GUI(self)
        self.GUI_template = GUI

        self.refresh_GUI()
        pygame.display.flip()

    def adjust_GUI(self):

        for wid in self.GUI:
            wid.adjust(self.surf_GUI)
        self.refresh_GUI()

    def update_resolution(self):


        self.create_surfaces()
        self.adjust_GUI()
        #pygame.display.flip()

    def rezise_request(self, event):
        self.needs_resize = True
        self.last_resie_request = pygame.time.get_ticks()
        
        self.w = event.w
        self.h = event.h

    def add_update(self, event):
        s = event.surf
        r = event.rect
        try:
            index = self.surfaces[s]
            try:
                self.updates[index].append( [s,r] )
            except KeyError:
                self.updates[index] = [ [s,r] ]
        except KeyError:
            pass #TODO make up something smart here later, OK? 


    def update_display(self):
        flip = False
        if self.needs_resize:
            if pygame.time.get_ticks() - self.last_resie_request > 50:
                self.update_resolution()
                self.needs_resize = False
                flip = True
            
        sorted(self.updates)
        upd = []
        for depth in self.updates:
            for change in self.updates[depth]:
                s,r = change
                self.MainWindow.blit(s,r,r)
                #self.MainWindow.blit(s,r)
                upd.append(r)
            self.updates[depth] = []
        if not upd == [] and not flip:
            pygame.display.update(upd)
        elif flip:
            pygame.display.flip()


