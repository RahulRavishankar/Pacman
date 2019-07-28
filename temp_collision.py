import pygame
import copy
from Character import PAC_MAN,GHOSTS,PELLETS,POW_PELLETS
win=pygame.display.set_mode((400,400))
pm=pygame.image.load("./pacright.png")     #pacman image
gm=pygame.image.load("./ghost1.png")       #ghost image
pellet=PELLETS()
powpellet=POW_PELLETS()
pacman=PAC_MAN()
blue=(0,0,255)
#checks collision between pacman and walls when left key is pressed.....also used to detect collision of ghosts with wall when dir="left"
def left_temp_collision(pacman):
    pacman.templocation=copy.deepcopy(pacman.location)
    pacman.templocation[0]=pacman.templocation[0]-pacman.speed
    collision=False
    locations=[(20,20),(35,20),(155,35),(155,70),(230,35),(230,20),(365,20),(35,185),(335,185),  (35,365),(115,315),(130,315),(150,315),(165,365),  
    (235,315),(250,315),(270,315),(285,365),
    (65,65),(80,140),(110,65),(275,65),(290,65),(320,65),
    (65,230),(80,230),(285,230),(320,230),
    (155,125),(170,125),(230,125),(200,185)]
    dimensions=[(15,360),(135,15),(15,35),(90,15),(15,35),(135,15),(15,360),(30,15),(30,15),  (80,15),(15,65),(20,15),(15,65),(70,15),  
    (15,65),(20,15),(15,65),(80,15),
    (15,90),(30,15),(15,90),(15,90),(30,15),(15,90),
    (15,105),(35,15),(35,15),(15,105),
    (15,130),(60,15),(15,60),(45,15)]
    for i in list(zip(locations,dimensions)): 
        if win.blit(pm,pacman.templocation).colliderect(pygame.draw.rect(win,blue,pygame.Rect(i),0)):
            collision=True
    return collision

#checks collision between pacman and walls when right key is pressed.....also used to detect collision of ghosts with wall when dir="right"
def right_temp_collision(pacman):       
    pacman.templocation=copy.deepcopy(pacman.location)
    pacman.templocation[0]=pacman.templocation[0]+pacman.speed
    collision=False
    locations=[(20,20),(35,20),(155,35),(155,70),(230,35),(230,20),(365,20),(35,185),(335,185),  (35,365),(115,315),(130,315),(150,315),(165,365),  
    (235,315),(250,315),(270,315),(285,365),
    (65,65),(80,140),(110,65),(275,65),(290,65),(320,65),
    (65,230),(80,230),(285,230),(320,230),
    (155,125),(170,125),(230,125),(200,185)]
    dimensions=[(15,360),(135,15),(15,35),(90,15),(15,35),(135,15),(15,360),(30,15),(30,15),  (80,15),(15,65),(20,15),(15,65),(70,15),  
    (15,65),(20,15),(15,65),(80,15),
    (15,90),(30,15),(15,90),(15,90),(30,15),(15,90),
    (15,105),(35,15),(35,15),(15,105),
    (15,130),(60,15),(15,60),(45,15)]
    for i in list(zip(locations,dimensions)): 
        if win.blit(pm,pacman.templocation).colliderect(pygame.draw.rect(win,blue,pygame.Rect(i),0)):
            collision=True
    return collision


#checks collision between pacman and walls when up key is pressed.....also used to detect collision of ghosts with wall when dir="up"
def up_temp_collision(pacman):
    pacman.templocation=copy.deepcopy(pacman.location)
    pacman.templocation[1]=pacman.templocation[1]-pacman.speed
    collision=False
    locations=[(20,20),(35,20),(155,35),(155,70),(230,35),(230,20),(365,20),(35,185),(335,185),  (35,365),(115,315),(130,315),(150,315),(165,365),  
    (235,315),(250,315),(270,315),(285,365),
    (65,65),(80,140),(110,65),(275,65),(290,65),(320,65),
    (65,230),(80,230),(285,230),(320,230),
    (155,125),(170,125),(230,125),(200,185)]
    dimensions=[(15,360),(135,15),(15,35),(90,15),(15,35),(135,15),(15,360),(30,15),(30,15),  (80,15),(15,65),(20,15),(15,65),(70,15),  
    (15,65),(20,15),(15,65),(80,15),
    (15,90),(30,15),(15,90),(15,90),(30,15),(15,90),
    (15,105),(35,15),(35,15),(15,105),
    (15,130),(60,15),(15,60),(45,15)]
    for i in list(zip(locations,dimensions)): 
        if win.blit(pm,pacman.templocation).colliderect(pygame.draw.rect(win,blue,pygame.Rect(i),0)):
            collision=True
    return collision

#checks collision between pacman and walls when down key is pressed.....also used to detect collision of ghosts with wall when dir="down"
def down_temp_collision(pacman):
    pacman.templocation=copy.deepcopy(pacman.location)
    pacman.templocation[1]=pacman.templocation[1]+pacman.speed
    collision=False
    locations=[(20,20),(35,20),(155,35),(155,70),(230,35),(230,20),(365,20),(35,185),(335,185),  (35,365),(115,315),(130,315),(150,315),(165,365),  
    (235,315),(250,315),(270,315),(285,365),
    (65,65),(80,140),(110,65),(275,65),(290,65),(320,65),
    (65,230),(80,230),(285,230),(320,230),
    (155,125),(170,125),(230,125),(200,185)]
    dimensions=[(15,360),(135,15),(15,35),(90,15),(15,35),(135,15),(15,360),(30,15),(30,15),  (80,15),(15,65),(20,15),(15,65),(70,15),  
    (15,65),(20,15),(15,65),(80,15),
    (15,90),(30,15),(15,90),(15,90),(30,15),(15,90),
    (15,105),(35,15),(35,15),(15,105),
    (15,130),(60,15),(15,60),(45,15)]
    for i in list(zip(locations,dimensions)): 
        if win.blit(pm,pacman.templocation).colliderect(pygame.draw.rect(win,blue,pygame.Rect(i),0)):
            collision=True
    return collision


def pacman_pellet_collision(score,pacman,locations):
    for i in locations:
        if win.blit(pellet.pel,i).colliderect(win.blit(pm,pacman.location)):
            locations.pop(locations.index(i))
            score=score+10

    return score,locations

def pacman_powpellet_collision(score,pacman,locations):
    for i in locations:
        if win.blit(powpellet.powpel,i).colliderect(win.blit(pm,pacman.location)):
            locations.pop(locations.index(i))
            score=score+50

    return score,locations

def pacman_ghost_collision(pacman,ghost):
    if win.blit(gm,ghost.location).colliderect(win.blit(pm,pacman.location)):
        return True