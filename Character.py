import pygame
import copy

class PAC_MAN(pygame.sprite.Sprite):
    def __init__(self):
        self.location=[190,140]
        self.speed=2
        self.pm=pygame.image.load("./pacright.png")
        self.templocation=copy.deepcopy(self.location)


    def draw(self,win,direction):
        if direction=="right":
        	self.pm=pygame.image.load("./pacright.png")
        if direction=="left":
        	self.pm=pygame.image.load("./pacleft.png")
        if direction=="up":
        	self.pm=pygame.image.load("./pacup.png")
        if direction=="down":
        	self.pm=pygame.image.load("./pacdown.png")

        win.blit(self.pm,self.location)

class GHOSTS(pygame.sprite.Sprite):
    def __init__(self,location):
        self.location=location
        self.speed=3.5
        self.templocation=copy.deepcopy(self.location)
        self.dir="left"

    def draw(self,win,ghostnumber,location):
        if ghostnumber==1:
            self.gm=pygame.image.load("./ghost1.png")
        if ghostnumber==2:
            self.gm=pygame.image.load("./ghost2.png")
        if ghostnumber==3:
            self.gm=pygame.image.load("./ghost3.png")
        if ghostnumber==4:
            self.gm=pygame.image.load("./ghost4.png")

        self.location=location
        win.blit(self.gm,self.location)

class PELLETS(pygame.sprite.Sprite):
    def __init__(self):
        self.pel=pygame.image.load("./coin.png")
        
    
class POW_PELLETS(pygame.sprite.Sprite):
    def __init__(self):
        self.powpel=pygame.image.load("./powpellet.bmp")


