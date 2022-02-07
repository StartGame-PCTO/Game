import cv2
from cv2 import DIST_MASK_3
import numpy as np
import pygame
import math
import Pallina as p
import config as c

"""lower_blue = np.array([30, 163, 99])
upper_blue = np.array([179, 255, 255])"""

def convertiX(x):
    return math.floor(x/c.CELL)

def convertiY(y):
    return math.floor(y/c.CELL)

def nothing(x):                                             
    pass

def wallControll(player,x,y):
    if x > 240 and x < 360 and y > 200 and y < 280:
            print("centro, fermo")
    if x > 240 and x < 360 and y > 0 and y < 200:
        if c.LEVEL1[convertiY((player.getY())-1)][convertiX(player.getX())] != "o":
            player.setY(-1)
    if x > 240 and x < 360 and y > 280 and y < 480:
        if c.LEVEL1[convertiY((player.getY())+16)][convertiX(player.getX())] != "o":
            player.setY(1)
    if x > 0 and x < 240 and y > 200 and y < 280:
        if c.LEVEL1[convertiY(player.getY())][convertiX((player.getX())-1)] != "o":
            player.setX(-1)
    if x > 360 and x < 640 and y > 200 and y < 280:
        if c.LEVEL1[convertiY(player.getY())][convertiX((player.getX())+43)] != "o":
            player.setX(1)
    if c.LEVEL1[convertiY(player.getY())][convertiX((player.getX())+43)] == "A":
        print("HAI VINTO")


def temp(screen):
    bg = pygame.image.load("lab01.jpeg")
    bg = pygame.transform.scale(bg, (800,800))
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


    player = p.Pallina(20,50)


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
        wallControll(player,x,y)

        pygame.display.update()

def menu(screen):
    bg = pygame.image.load("menu.png")
    bg = pygame.transform.scale(bg, (800,800))
    while True:
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                if mouseX > c.START_BTN_CORD[0] and mouseX < c.START_BTN_CORD[0]+c.START_BTN_DIM[0] and mouseY > c.START_BTN_CORD[1] and mouseY < c.START_BTN_CORD[1]+c.START_BTN_DIM[1]:
                    return # A TARATURA

                if mouseX > c.LEVEL_BTN_CORD[0] and mouseX < c.LEVEL_BTN_CORD[0]+c.LEVEL_BTN_DIM[0] and mouseY > c.LEVEL_BTN_CORD[1] and mouseY < c.LEVEL_BTN_CORD[1]+c.LEVEL_BTN_DIM[1]:
                    while True:
                        print("Level") # A LIVELLI

        pygame.display.update()


def main():
    dim = (len(c.LEVEL1[1])*c.CELL,len(c.LEVEL1)*c.CELL)
    pygame.init()
    pygame.display.set_caption('Fly Maze')
    screen = pygame.display.set_mode(dim)
    menu(screen)
    temp(screen)


if __name__ == "__main__":
    main()