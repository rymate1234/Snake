# Wormy (a Nibbles clone)
# By cd al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

#KRT 14/06/2012 modified Start Screen and Game Over screen to cope with mouse events
#KRT 14/06/2012 Added a non-busy wait to Game Over screen to reduce processor loading from near 100%
import random, pygame, sys
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation(CELLWIDTH, CELLHEIGHT):
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
