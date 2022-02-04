import cv2
import numpy as np
import pygame
import math
import Pallina as p
TEN = 10

def convertiX(x):
    return math.floor(x/TEN)

def convertiY(y):
    return math.floor(y/TEN)

def WallControll(x,y,player,level):
    if x > 240 and x < 360 and y > 200 and y < 280:
            print("centro, fermo")
    if x > 240 and x < 360 and y > 0 and y < 200:
        if level[convertiY((player.getY)-1)][convertiX(player.getX)] != "R":
            player.setY(-1)
    if x > 240 and x < 360 and y > 280 and y < 480:
        if level[convertiY((player.getY)+1)][convertiX(player.getX)] != "R":
            player.setY(1)
    if x > 0 and x < 240 and y > 200 and y < 280:
        if level[convertiY(player.getY)][convertiX((player.getX)-1)] != "R":
            player.setX(-1)
    if x > 360 and x < 640 and y > 200 and y < 280:
        if level[convertiY(player.getY)][convertiX((player.getX)+1)] != "R":
            player.setX(1)

def main():
    level=[
    "RRRRRRRRRRRRRRRRRRRRRRRRRRR:::::::RRRRRRRRRRRRRRRRRRRRRRRRRR",
    "++++++++++++++++++++++++++R:::::::R+++++++++++++++++++++++++",
    "++++++++++++++++++++++++++R:::::::R+++++++++++++++++++++++++",
    "++++++++++++++++++++++++++R:::::::R+++++++++++++++++++++++++",
    "++++++++++++++++++++++++++R:::::::R+++++++++++++++++++++++++",
    "++++++++++++++++++++++++++R:::::::R+++++++++++++++++++++++++",
    "RRRRRRRRRRRRRRRRRRRR++++++R:::::::R++++++RRRRRRRRRRRRRRRRRRR",
    "::::::::::::::::::RR++++++R:::::::R++++++R::::::::::::::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++R::::::::::::::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++R::::::::::::::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++R::::::::::::::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++R::::::::::::::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++R::::::::::::::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++R::::::::::::::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++R::::::::::::::::::",
    ":::RRRRRRRRRRRRRRRRR++++++R:::::::R++++++R::::::::::::::::::",
    ":::R++++++++++++++++++++++R:::::::R++++++R::::::::::::::::::",
    ":::R++++++++++++++++++++++R:::::::R++++++R++++++++++++::::::",
    ":::R++++++++++++++++++++++R:::::::R++++++++++++++++++R::::::",
    ":::R++++++++++++++++++++++R:::::::R++++++++++++++++++R::::::",
    ":::RRRRRRRRRRRRRRRRR++++++R:::::::R++++++++++++++++++R::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++++++++++++++R::::::",
    "::::::::::::::::::RR++++++R:::::::R++++++++++++++++++R::::::",
    "::::::::::::::::::RR++++++R:::::::RRRRRRRRRRRRR++++++R::::::",
    "::::::::::::::::::RR++++++R:::::::::::::::::::R++++++R::::::",
    "::::::RRRRRRRRR:::RR++++++R:::::::::::::::::::R++++++R::::::",
    "::::::RR++++++R:::RR++++++R:::::::::::::::::::R++++++R::::::",
    "::::::RR++++++R:::RR++++++R:::::::::::::::::::R++++++R::::::",
    "::::::RR++++++R:::RR++++++RRRRRRRRRRRRR:::::::R++++++R::::::",
    "::::::RR++++++R:::RR++++++++++++++++++R:::::::R++++++R::::::",
    "::::::RR++++++R:::RR++++++++++++++++++R:::::::R++++++R::::::",
    "::::::RR++++++R:::RR++++++++++++++++++R:::::::R++++++R::::::",
    "::::::RR++++++R:::RR++++++++++++++++++R:::::::R++++++R::::::",
    "::::::RR++++++R:::RR++++++++++++++++++R:::::::R++++++R::::::",
    "::::::RR++++++R:::@RRRRRRRRR++++++++++RRRRRRRRR++++++RRRRRRR",
    "::::::RR++++++R::::::::::::R+++++++++++++++++++++++++++++++R",
    "::::::RR++++++RRRRRRRRRRRRRR+++++++++++++++++++++++++++++++R",
    "::::::RR+++++++++++++++++++++++++++++++++++++++++++++++++++R",
    "::::::RR+++++++++++++++++++++++++++++++++++++++++++++++++++R",
    "::::::RR+++++++++++++++++++++++++++++++++++++++++++++++++++R",
    "::::::RR+++++++++++++++++++++++++++++++++++++++++++++++++++R",
    "::::::RR+++++++++++++++++++++++++++++++++++++++++++++++++++R",
    "::::::RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::",
    "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::",
]
    DIMENSIONI = (len(level[1])*TEN,len(level)*TEN)
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONI)
    bg = pygame.image.load("labirintoprova.jpeg")
    pygame.display.set_caption('Prova')
    kernel = np.ones((8 ,8), np.uint8)
    cap = cv2.VideoCapture(0)       #utilizza cam di default (0)
    cap.set(10, 100)        #lucentezza della cam
     

    player = p.Pallina(300,300)


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
        WallControll(x,y,player,level)

        pygame.display.update()

if __name__ == "__main__":
    main()