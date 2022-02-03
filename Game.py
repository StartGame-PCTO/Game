import cv2
import numpy as np
import pygame

def colorDetec():
    DIMENSIONI = (600,600)
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONI)
    pygame.display.set_caption('Prova')
    colore = (255,0,0)
    nero = (0,0,0)
    state = True
    centroX = 300
    centroY = 300
    kernel = np.ones((8 ,8), np.uint8)

    def nothing(x):
        pass

    cap = cv2.VideoCapture(0)       #utilizza cam di default (0)
    cv2.namedWindow("Trackbars")
    '''cap.set(3, 640)
    cap.set(4, 480)'''
    cap.set(10, 100)        #lucentezza della cam

    cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)  
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

        

    '''    #min = [0, 0, 0]         max e min scala colori openCV
        #max = [180, 255, 255]
    '''
        
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
        screen.fill(colore)
        pygame.draw.circle(screen,nero,(centroX,centroY),10)
        if x > 240 and x < 360 and y > 200 and y < 280:
            print("centro, fermo")
        if x > 240 and x < 360 and y > 0 and y < 200:
            centroY -= 1
        if x > 240 and x < 360 and y > 280 and y < 480:
            centroY += 1
        if x > 0 and x < 240 and y > 200 and y < 280:
            centroX -= 1
        if x > 360 and x < 640 and y > 200 and y < 280:
            centroX += 1
        pygame.display.update()

def main():
    colorDetec()

if __name__ == "__main__":
    main()