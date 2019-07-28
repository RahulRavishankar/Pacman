import pygame 
from Character import PAC_MAN,GHOSTS,PELLETS,POW_PELLETS
import temp_collision as tc 
import random


pygame.init()                              #initialize pygame

win=pygame.display.set_mode((400,400))
pygame.display.set_caption("PAC-MAN")

clock=pygame.time.Clock()
blue=(0,0,255)
direction="right"    #default direction
collision=False     #default value of collision
pm=pygame.image.load("./pacright.png")

pacman=PAC_MAN()
directionlist=["right","left","up","down"]

pellet=PELLETS()
powpellet=POW_PELLETS()
pellets_locations=[(45,45),(45,75),(45,105),(45,135),(45,165),(75,45),(105,45),(135,45),(135,75),(135,105),(135,135),(135,165),(135,195),(135,225),(135,255),(135,285),
(90,285),(90,255),(90,315),(90,345),(67.5,345),(45,345),(45,305),(45,245),(45,210),(75,210),(105,210),(105,187.5),(75,187.5),(75,165),(105,165),
(345,45),(345,75),(345,105),(345,135),(345,165),  (285,45),(255,45),(255,75),(255,105),(255,135),(255,165),(255,195),(255,225),(255,255),(255,285),
(285,165),(315,165),(285,187.5),(315,187.5),
(300,255),(300,285),(300,315),(300,345),(322.5,345),(345,345),(345,315),(345,245),(345,210),(315,210),(285,210),
(175,315),(175,285),(175,255),(175,225),(175,195),(175,165),(175,145),    (90,80),(300,135),
(215,345),(215,315),(215,285),(215,255),(215,225)]

powpel_locations=[(175,342.5),(312.5,42.5),(42.5,275),(342.5,280)]

#colours
white = (255,255,255)
black = (0,0,0)
boardwhite = (220,220,220)
boardblack = (140,140,140)
red=(150,0,0)
yellow=(100,100,0)
green=(0,100,0)
blue=(0,0,100)
lightgreen=(0,255,0)
lightyellow=(255,255,0)
lightblue=(0,0,255)
lightred = (255,0,0)
brown = (110,70,70)

#displaywidth = 655
#blockwidth = 60
#extborder = 50
fps = 30

tinyfont = pygame.font.SysFont("comicsansms",15)
smallfont = pygame.font.SysFont("comicsansms",25)
mediumfont = pygame.font.SysFont("comicsansms",35)
largefont = pygame.font.SysFont("comicsansms",50)

def txtobject(msg,colour,size):
    if size=="small":
        txtsurface=smallfont.render(msg,True,colour)
    elif size=="medium":
        txtsurface=mediumfont.render(msg,True,colour)
    elif size=="large":
        txtsurface=largefont.render(msg,True,colour)
    elif size=="tiny":
        txtsurface=tinyfont.render(msg,True,colour)
    return txtsurface , txtsurface.get_rect()


def message(msg,colour,ydisplace=0,size="small"):
    txtsurface , txtrect = txtobject(msg,colour,size)
    txtrect.center =(200),(200)+ydisplace
    win.blit(txtsurface,txtrect)

def text2button(msg,colour,xaxis,yaxis,width,height,size="tiny"):
    txtsurface , txtrect = txtobject(msg,colour,size)
    txtrect.center =xaxis+(width/2),yaxis+(height/2)
    win.blit(txtsurface,txtrect)

def welcomepage():
    intro=True
    win.fill(black)
    message("PACMAN",red,-100,"large")
    pygame.display.update()
    clock.tick(30)
    pygame.time.delay(1500)
    

def button(msg,x,y,width,height,inactivecolour,activecolour,action=None):
    cursor=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+width > cursor[0] > x and y+height > cursor[1] > y:
        pygame.draw.rect(win,activecolour,(x,y,width,height))
        if click[0]==1 and action!=None:
            if action=="QUIT":
                pygame.quit()
                quit()
            elif action == "PLAY":
                main()
    else:
        pygame.draw.rect(win,inactivecolour,(x,y,width,height))
    text2button(msg,black,x,y,width,height)

    pygame.display.update()

                
def displaypic(location):
    for i in location:
        if i[2] != []:
            win.blit(i[2],i[0][::-1])


welcomepage()    

def draw_powpellets():
    for i in powpel_locations:
        win.blit(powpellet.powpel,i)

def draw_pellets():
    for i in pellets_locations:
            win.blit(pellet.pel,i)

def drawwalls():
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
    for i in list(zip(locations,dimensions)) : 
        pygame.draw.rect(win,blue,pygame.Rect(i),0)

def redrawwindow():
    win.fill((0,0,0)) 
    
    draw_pellets()
    draw_powpellets()

    ziplist=list(zip(ghostlist,ghostnolist))
    for i,j in ziplist:
        i.draw(win,j,i.location)

    pacman.draw(win,direction)
    drawwalls()
    pygame.display.update()

def main():
    global ghost1,ghost2,ghost3,ghost4,ghostlist,ghostnolist,pellets_locations,powpel_locations,score
    score=0
    ghost1=GHOSTS([80,110])
    ghost2=GHOSTS([290,80])
    ghost3=GHOSTS([35,335])
    ghost4=GHOSTS([285,335])
    ghostlist=[ghost1,ghost2,ghost3,ghost4]
    ghostnolist=[1,2,3,4]

    run=True
    while run:
        clock.tick(30)      #30fps
        global direction
        for event in pygame.event.get():
             # If user hits 'X'
            if event.type==pygame.QUIT:
                run=False

        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and tc.left_temp_collision(pacman)==False:
            pacman.location[0]=pacman.location[0]-pacman.speed
            direction="left"
            

        elif keys[pygame.K_RIGHT] and tc.right_temp_collision(pacman)==False:
            pacman.location[0]=pacman.location[0]+pacman.speed
            direction="right"
            

        elif keys[pygame.K_UP] and tc.up_temp_collision(pacman)==False:                   #y is increasing downwards
            pacman.location[1]=pacman.location[1]-pacman.speed
            direction="up"
            

        elif keys[pygame.K_DOWN] and tc.down_temp_collision(pacman)==False:
            pacman.location[1]=pacman.location[1]+pacman.speed
            direction="down"


        for i in ghostlist:          
            #if tc.left_temp_collision(i)==True or tc.right_temp_collision(i)==True or tc.up_temp_collision(i)==True or tc.down_temp_collision(i)==True:
            i.dir=random.choice(directionlist)
            if i.dir=="left" and tc.left_temp_collision(i)==False:
                i.location[0]=i.location[0]-i.speed
            elif i.dir=="right" and tc.right_temp_collision(i)==False:
                i.location[0]=i.location[0]+i.speed
            elif i.dir=="up" and tc.up_temp_collision(i)==False:
                i.location[1]=i.location[1]-i.speed
            elif i.dir=="down" and tc.down_temp_collision(i)==False:
                i.location[1]=i.location[1]+i.speed

        score,pellets_locations=tc.pacman_pellet_collision(score,pacman,pellets_locations)          #checks collision between pacman and pellets
        score,powpel_locations=tc.pacman_powpellet_collision(score,pacman,powpel_locations)         #checks collision between pacman and power-pellets

        for i in ghostlist:
            if tc.pacman_ghost_collision(pacman,i)==True:                               #checks collision between pacman and ghosts
                run=False

        redrawwindow()



main()
def exitpage(score):
    intro=True
    win.fill(black)
    message("GAME OVER",red,-100,"large")
    message1("Score = "+str(score),red,-100,"large")
    pygame.display.update()
    clock.tick(30)
    pygame.time.delay(1500)
                
def displaypic(location):
    for i in location:
        if i[2] != []:
            win.blit(i[2],i[0][::-1])

exitpage(score)


#print("GAME OVER!!")
print(score)
pygame.quit()

