import cv2
from cv2 import DIST_MASK_3
import numpy as np
import pygame
import math
import Pallina as p
TEN = 8
level=[
    "ooooooooooooooooooooooooooooooooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++o+++++++o+",
    "ooooooooooooooooooooooooooooooooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooooooooooooooooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooooooooooooooooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+o+ooooo+++o+++++o+ooo+ooo+++ooo+++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "oooooooooooooooooooo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "oooooooooooooooooooo++++++++++ooo+++++++++++++++++++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "oooooooooooooooooooo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooooooooooooooooooooooooooooooo++++++++++ooooooooo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooooooooooooooooooooooooooooooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+o+ooo+ooooo+o+o+o+o+o+o+oo++++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+oo++++++++++++++++++++++++++++++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+oo++++++++++++++++++++++++++++++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+oo++++++++++++++++++++++++++++++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooooooo++++++++++ooooooooooooooooo++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooooooo+++++++++ooooooooooooooooooo+++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++++++oo+++++++++++ooooo++++++++++ooooooooooooooooooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo++++++++++oo+++o+oo++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "o+++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "o+++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++ooooooooooooooooooooooooooo+ooo+++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++ooooooooooooooooooooooooooooooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++ooooooooooooooooooooooooooooooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo+++++++++++oooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++++++++ooooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++ooooooooooooooooooooooooooooooooooooooooooooooooooo+++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++ooooooooooooooooooooooooooooooooooooooooooooooooooo+++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooooooooooooooooooooooo+++",
    "++++++++++++++oo++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooooooooooooooooooooooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++oo++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++oo++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo++++++++++ooooooooooooooooooooooooooooooooooooo+++++++++++ooooooooo++++++++++ooo+++",
    "++++++++++++++oo++++++++++ooooooooooooooooooooooooooooooooooooooo+++++++++ooooooooooo+++++++++ooo+++",
    "o+++++++++++++ooo+++++++++ooooooooooooooooooooooooooooooooooooooo+++++++++oooooooooo++++++++++ooo+++",
    "++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++++++oo++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++++++oo++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++oo+++++++++++oo+++++++++++++++++++++++++++++++++oo++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++ooooooooooo+ooo+++++++++++++++++++++++++++++++++ooooooooooooooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooooooooooooooo+++++++++++++++++++++++++++++++++ooooooooooooooo+++++oo++++++++++ooo+++",
    "++++++++++++++ooooooooooooooo+++++++++++++++++++++++++++++++++ooooooooooooooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++++++++ooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
]

def convertiX(x):
    return math.floor(x/TEN)

def convertiY(y):
    return math.floor(y/TEN)

def temp(screen):
    bg = pygame.image.load("lab01.jpeg")
    bg = pygame.transform.scale(bg, (800,800))
    kernel = np.ones((8 ,8), np.uint8)
    cap = cv2.VideoCapture(0)       #utilizza cam di default (0)
    cv2.namedWindow("Trackbars")
    cap.set(10, 100)        #lucentezza della cam


    player = p.Pallina(10,30)


    while True:
        _, frame = cap.read()       # _ bool per vedere se la cattura dal frame dalla cam ha avuto successo o meno, img frame della cam
        frameFlip = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frameFlip, cv2.COLOR_BGR2HSV)       #converto il frame da BGR in HSV    (H colore, S concentrazione colore, V lucentezza colore)

        lower_blue = np.array([30, 163, 99])
        upper_blue = np.array([179, 255, 255])
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
        if x > 240 and x < 360 and y > 200 and y < 280:
            print("centro, fermo")
        if x > 240 and x < 360 and y > 0 and y < 200:
            if level[convertiY((player.getY())-1)][convertiX(player.getX())] != "o":
                player.setY(-1)
        if x > 240 and x < 360 and y > 280 and y < 480:
            if level[convertiY((player.getY())+16)][convertiX(player.getX())] != "o":
                player.setY(1)
        if x > 0 and x < 240 and y > 200 and y < 280:
            if level[convertiY(player.getY())][convertiX((player.getX())-1)] != "o":
                player.setX(-1)
        if x > 360 and x < 640 and y > 200 and y < 280:
            if level[convertiY(player.getY())][convertiX((player.getX())+43)] != "o":
                player.setX(1)

        pygame.display.update()

def menu(screen):
    bg = pygame.image.load("menu.png")
    bg = pygame.transform.scale(bg, (800,800))
    conta = 0
    while conta<300:
        screen.blit(bg, (0,0))
        conta += 1
        pygame.display.update()


def main():
    DIMENSIONI = (len(level[1])*TEN,len(level)*TEN)
    pygame.init()
    pygame.display.set_caption('Prova')
    screen = pygame.display.set_mode(DIMENSIONI)
    menu(screen)
    temp(screen)
if __name__ == "__main__":
    main()