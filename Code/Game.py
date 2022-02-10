import cv2
import numpy as np
import pygame
import math
import Pallina as p
import config as c



def nothing(x):                                             
    pass
kernel = np.ones((8 ,8), np.uint8)
cap = cv2.VideoCapture(0)       #utilizza cam di default (0)
cv2.namedWindow("Trackbars")
cap.set(10, 100)        #lucentezza della cam
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)   #Create a trackbar 
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)


"""lower_blue = np.array([30, 163, 99])
upper_blue = np.array([179, 255, 255])"""

def convertiX(x):
    return math.floor(x/c.CELL)

def convertiY(y):
    return math.floor(y/c.CELL)

def indovinello(screen,nlvl):
    x = pygame.image.load("Image\X.png")
    if nlvl == 1:
        bg = pygame.image.load("Image\Riddle1.png")
        bg = pygame.transform.scale(bg, (800,800))
        screen.blit(bg,(0,0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX > c.RISP1_BTN_CORD[0] and mouseX < c.RISP1_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP1_BTN_CORD[1] and mouseY < c.RISP1_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        screen.blit(x,(c.RISP1_BTN_CORD))
                    if mouseX > c.RISP2_BTN_CORD[0] and mouseX < c.RISP2_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP2_BTN_CORD[1] and mouseY < c.RISP2_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        screen.blit(x,(c.RISP2_BTN_CORD))
                    if mouseX > c.RISP3_BTN_CORD[0] and mouseX < c.RISP3_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP3_BTN_CORD[1] and mouseY < c.RISP3_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        return True
            pygame.display.update()

    if nlvl == 2:
        bg = pygame.image.load("Image\Riddle2.png")
        bg = pygame.transform.scale(bg, (800,800))
        screen.blit(bg,(0,0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX > c.RISP1_BTN_CORD[0] and mouseX < c.RISP1_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP1_BTN_CORD[1] and mouseY < c.RISP1_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP1_BTN_CORD))
                    if mouseX > c.RISP2_BTN_CORD[0] and mouseX < c.RISP2_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP2_BTN_CORD[1] and mouseY < c.RISP2_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        return True
                    if mouseX > c.RISP3_BTN_CORD[0] and mouseX < c.RISP3_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP3_BTN_CORD[1] and mouseY < c.RISP3_BTN_CORD[1]+c.RISP_BTN_DIM[1]:    
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP3_BTN_CORD))
            pygame.display.update()

    if nlvl == 3:
        bg = pygame.image.load("Image\Riddle3.png")
        bg = pygame.transform.scale(bg, (800,800))
        screen.blit(bg,(0,0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX > c.RISP1_BTN_CORD[0] and mouseX < c.RISP1_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP1_BTN_CORD[1] and mouseY < c.RISP1_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP1_BTN_CORD))
                    if mouseX > c.RISP2_BTN_CORD[0] and mouseX < c.RISP2_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP2_BTN_CORD[1] and mouseY < c.RISP2_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        return True
                    if mouseX > c.RISP3_BTN_CORD[0] and mouseX < c.RISP3_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP3_BTN_CORD[1] and mouseY < c.RISP3_BTN_CORD[1]+c.RISP_BTN_DIM[1]:    
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP3_BTN_CORD))
            pygame.display.update()

    if nlvl == 4:
        bg = pygame.image.load("Image\Riddle4.png")
        bg = pygame.transform.scale(bg, (800,800))
        screen.blit(bg,(0,0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if mouseX > c.RISP1_BTN_CORD[0] and mouseX < c.RISP1_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP1_BTN_CORD[1] and mouseY < c.RISP1_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP1_BTN_CORD))
                    if mouseX > c.RISP2_BTN_CORD[0] and mouseX < c.RISP2_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP2_BTN_CORD[1] and mouseY < c.RISP2_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        return True
                    if mouseX > c.RISP3_BTN_CORD[0] and mouseX < c.RISP3_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP3_BTN_CORD[1] and mouseY < c.RISP3_BTN_CORD[1]+c.RISP_BTN_DIM[1]:    
                        pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP3_BTN_CORD))

            pygame.display.update()

def wallControll(player,x,y,level):
    if x > 240 and x < 360 and y > 200 and y < 280:
            print("centro, fermo")
    if x > 240 and x < 360 and y > 0 and y < 200:
        if level[convertiY((player.getY())-3)][convertiX(player.getX())] != "o" and level[convertiY((player.getY())-3)][convertiX(player.getX()+35)] != "o":
            player.setY(-3)
    if x > 240 and x < 360 and y > 280 and y < 480:
        if level[convertiY((player.getY())+38)][convertiX(player.getX())] != "o" and level[convertiY((player.getY())+38)][convertiX(player.getX()+35)] != "o":
            player.setY(3)
    if x > 0 and x < 240 and y > 200 and y < 280:
        if level[convertiY(player.getY())][convertiX((player.getX())-3)] != "o" and level[convertiY(player.getY()+35)][convertiX((player.getX())-3)] != "o":
            player.setX(-3)
    if x > 360 and x < 640 and y > 200 and y < 280:
        if level[convertiY(player.getY())][convertiX((player.getX())+38)] != "o" and level[convertiY(player.getY()+35)][convertiX((player.getX())+38)] != "o":
            player.setX(3)
    if level[convertiY(player.getY())][convertiX((player.getX()))] == "P":
        player.teleport(440,609)
    if level[convertiY(player.getY())][convertiX((player.getX()))] == "A":
        return True
    else: return False

def lvl(screen,nlvl):
    vittoria = pygame.image.load("Image\Win.png")
    vittoria = pygame.transform.scale(vittoria, (800,800))
    if nlvl == 1:
        pygame.mixer.Sound.set_volume(soundLvl1,0.5)    #set the volume of the background track
        pygame.mixer.Sound.play(soundLvl1, -1) 
        level = c.LEVEL1
        bg = pygame.image.load("Image\Lab1.jpeg")
        bg = pygame.transform.scale(bg, (800,800))
        x,y = 20,50
    if nlvl == 2:
        pygame.mixer.Sound.set_volume(soundLvl2,0.5)    #set the volume of the background track
        pygame.mixer.Sound.play(soundLvl1, -1) 
        bg = pygame.image.load("Image\Lab2.png")
        bg = pygame.transform.scale(bg, (800,800))
        x,y = 760,420
        level = c.LEVEL2
    if nlvl == 3:
        pygame.mixer.Sound.set_volume(soundLvl3,0.5)    #set the volume of the background track
        pygame.mixer.Sound.play(soundLvl1, -1) 
        bg = pygame.image.load("Image\Lab3.png")
        bg = pygame.transform.scale(bg, (800,800))
        x,y = 350,1
        level = c.LEVEL3
    if nlvl == 4:
        pygame.mixer.Sound.set_volume(soundLvl4,0.5)    #set the volume of the background track
        pygame.mixer.Sound.play(soundLvl1, -1) 
        bg = pygame.image.load("Image\Lab4.png")
        bg = pygame.transform.scale(bg, (800,800))
        x,y = 45,1
        level = c.LEVEL4

    player = p.Pallina(x,y)


    while True:
        _, frame = cap.read()       # _ bool per vedere se la cattura dal frame dalla cam ha avuto successo o meno, img frame della cam
        frameFlip = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frameFlip, cv2.COLOR_BGR2HSV)       #converto il frame da BGR in HSV    (H colore, S concentrazione colore, V lucentezza colore)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        lower_blue = np.array([l_h, l_s, l_v])
        upper_blue = np.array([u_h, u_s, u_v])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        mask = cv2.erode(mask, kernel, iterations=5)
        mask = cv2.dilate(mask, kernel, iterations=5)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        x, y, w, h = cv2.boundingRect(opening)

        result = cv2.bitwise_and(frameFlip, frameFlip, mask=mask)

        cv2.imshow("frame", frameFlip)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)  
        if cv2.waitKey(1) == 27:        #controllo se nel millisecondo è stato schiacciato esc (27) esce dal loop e chiude tutte le finestre
            break

        print(x,y)
        screen.blit(bg, (0,0))
        player.show(screen)
        win = wallControll(player,x,y,level)
        if win == True and indovinello(screen,nlvl):
            if nlvl == 1:
                pygame.mixer.Sound.stop(soundLvl1)
            if nlvl == 2:
                pygame.mixer.Sound.stop(soundLvl2)
            if nlvl == 3:
                pygame.mixer.Sound.stop(soundLvl3)
            if nlvl == 4:
                pygame.mixer.Sound.stop(soundLvl4)
            break
        pygame.display.update()
    
    while True:
        screen.blit(vittoria,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                if mouseX > c.NEXT_BTN_CORD[0] and mouseX < c.NEXT_BTN_CORD[0]+c.MN_BTN_DIM[0] and mouseY > c.NEXT_BTN_CORD[1] and mouseY < c.NEXT_BTN_CORD[1]+c.MN_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick)
                    return True
                if mouseX > c.MENU_BTN_CORD[0] and mouseX < c.MENU_BTN_CORD[0]+c.MN_BTN_DIM[0] and mouseY > c.MENU_BTN_CORD[1] and mouseY < c.MENU_BTN_CORD[1]+c.MN_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick)
                    return False
        pygame.display.update()
    
def start(screen,nlvl):
    bg = pygame.image.load("Image\Calibration.png")
    ok = pygame.image.load("Image\Ok.png")
    no = pygame.image.load("Image\\No.png")
    bg = pygame.transform.scale(bg, (800,800))
    ok = pygame.transform.scale(ok, (300,200))
    no = pygame.transform.scale(no, (300,200))
    centerTitle2 = ok.get_rect(center=(c.DIM_IMG[0]/2,c.DIM_IMG[1]/2))
    waitTime = 0
    while True:
        screen.blit(bg,(0,0))

        _, frame = cap.read()       # _ bool per vedere se la cattura dal frame dalla cam ha avuto successo o meno, img frame della cam
        frameFlip = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frameFlip, cv2.COLOR_BGR2HSV)       #converto il frame da BGR in HSV    (H colore, S concentrazione colore, V lucentezza colore)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        lower_blue = np.array([l_h, l_s, l_v])
        upper_blue = np.array([u_h, u_s, u_v])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        mask = cv2.erode(mask, kernel, iterations=5)
        mask = cv2.dilate(mask, kernel, iterations=5)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        x, y, w, h = cv2.boundingRect(opening)

        result = cv2.bitwise_and(frameFlip, frameFlip, mask=mask)

        cv2.imshow("frame", frameFlip)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)

        if cv2.waitKey(1) == 27:        #controllo se nel millisecondo è stato schiacciato esc (27) esce dal loop e chiude tutte le finestre
            break
        
        if x > 240 and x < 360 and y > 200 and y < 280:
            screen.blit(ok, centerTitle2)
            waitTime+=1
            if waitTime==50:
                pygame.mixer.Sound.stop(soundMenu)
                rigioca = lvl(screen,nlvl)
                if rigioca == True and nlvl < 4:
                        nlvl += 1
                else:
                    break
        else:
            screen.blit(no, centerTitle2)
            waitTime=0

        pygame.display.update()

def level(screen):
    bg = pygame.image.load("Image\LabAll.png")    
    menu = pygame.image.load("Image\ButtonMenu.png")
    bg = pygame.transform.scale(bg, (800,800))
    menu = pygame.transform.scale(menu,(180,80))
    while True:
        screen.blit(bg,(0,0))
        screen.blit(menu,(310,700))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                if mouseX > c.LVL1_BTN_CORD[0] and mouseX < c.LVL1_BTN_CORD[0]+c.LVL_BTN_DIM[0] and mouseY > c.LVL1_BTN_CORD[1] and mouseY < c.LVL1_BTN_CORD[1]+c.LVL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick)
                    start(screen,1)
                if mouseX > c.LVL2_BTN_CORD[0] and mouseX < c.LVL2_BTN_CORD[0]+c.LVL_BTN_DIM[0] and mouseY > c.LVL2_BTN_CORD[1] and mouseY < c.LVL2_BTN_CORD[1]+c.LVL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick)
                    start(screen,2)
                if mouseX > c.LVL3_BTN_CORD[0] and mouseX < c.LVL3_BTN_CORD[0]+c.LVL_BTN_DIM[0] and mouseY > c.LVL3_BTN_CORD[1] and mouseY < c.LVL3_BTN_CORD[1]+c.LVL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick)
                    start(screen,3)
                if mouseX > c.LVL4_BTN_CORD[0] and mouseX < c.LVL4_BTN_CORD[0]+c.LVL_BTN_DIM[0] and mouseY > c.LVL4_BTN_CORD[1] and mouseY < c.LVL4_BTN_CORD[1]+c.LVL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick)
                    start(screen,4)
                if mouseX > c.MENU2_BTN_CORD[0] and mouseX < c.MENU2_BTN_CORD[0]+c.MENU2_BTN_DIM[0] and mouseY > c.MENU2_BTN_CORD[1] and mouseY < c.MENU2_BTN_CORD[1]+c.MENU2_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick)
                    return
        pygame.display.update()

def menu(screen):
    bg = pygame.image.load("Image\Menu.png")
    bg = pygame.transform.scale(bg, (800,800))


    pygame.mixer.Sound.set_volume(soundMenu,0.5)    #set the volume of the background track
    pygame.mixer.Sound.play(soundMenu, -1)  

    while True:
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                if mouseX > c.START_BTN_CORD[0] and mouseX < c.START_BTN_CORD[0]+c.START_BTN_DIM[0] and mouseY > c.START_BTN_CORD[1] and mouseY < c.START_BTN_CORD[1]+c.START_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick) 
                    start(screen,1)
                    

                if mouseX > c.LEVEL_BTN_CORD[0] and mouseX < c.LEVEL_BTN_CORD[0]+c.LEVEL_BTN_DIM[0] and mouseY > c.LEVEL_BTN_CORD[1] and mouseY < c.LEVEL_BTN_CORD[1]+c.LEVEL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)    #set the volume of the background track
                    pygame.mixer.Sound.play(soundClick) 
                    level(screen)

        pygame.display.update()

def main():
    pygame.mixer.init()
    global soundMenu
    global soundClick
    global soundLvl1
    global soundLvl2
    global soundLvl3
    global soundLvl4
    soundMenu = pygame.mixer.Sound("Sounds\Menu.mp3")
    soundClick = pygame.mixer.Sound("Sounds\Click.mp3")
    soundLvl1 = pygame.mixer.Sound("Sounds\Lvl1.mp3")
    soundLvl2 = pygame.mixer.Sound("Sounds\Lvl2.mp3")
    soundLvl3 = pygame.mixer.Sound("Sounds\Lvl3.mp3")
    soundLvl4 = pygame.mixer.Sound("Sounds\Lvl4.mp3")
    dim = (len(c.LEVEL1[1])*c.CELL,len(c.LEVEL1)*c.CELL)
    pygame.init()
    pygame.display.set_caption('Fly Maze')
    screen = pygame.display.set_mode(dim)
    menu(screen)


if __name__ == "__main__":
    main()