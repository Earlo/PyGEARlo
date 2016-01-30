import pygame

LANGUAGE = "english"

SWIDTH =  800
SHEIGTH = 600

FONT = "Calibri" #I know. Will change later

#millisecnds
LETTER_INPUT_HELD_DOWN_DELAY    = 100
LETTER_INPUT_HELD_DOWN_INTERWAL = 20
INPUT_BOX_ACTIVITY_INDICATOR = "|"

update_screen_event = pygame.USEREVENT + 1
function_call_event = pygame.USEREVENT + 2
MAINCHA = 0 
ONETIME = 1

def nothing():
    print ("nothing") #:D
    pass


