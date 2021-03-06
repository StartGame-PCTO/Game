import cv2
import numpy as np
import pygame
import math
import Pallina as p
import config as c
pygame.mixer.init()                                                                                         #inizalizzazione modulo pygame per il suono
#definizione di alcune variabili globali
music = 0
soundWin = pygame.mixer.Sound("Sounds\Win.mp3")
soundMenu = pygame.mixer.Sound("Sounds\Menu.mp3")
soundClick = pygame.mixer.Sound("Sounds\Click.mp3")
soundLvl4 = pygame.mixer.Sound("Sounds\Lvl1.mp3")
soundLvl2 = pygame.mixer.Sound("Sounds\Lvl2.mp3")
soundLvl3 = pygame.mixer.Sound("Sounds\Lvl3.mp3")
soundLvl1 = pygame.mixer.Sound("Sounds\Lvl4.mp3")

def nothing(x):                                             
    pass

####################################
#INIZIALIZZAZIONE WEBCAM E TRACKBAR#
####################################

kernel = np.ones((8 ,8), np.uint8)
cap = cv2.VideoCapture(0)                                                                                   #utilizza cam di default (0)
cap.set(10, 100)                                                                                            #lucentezza della cam
cv2.namedWindow("Trackbars")                                                                                #Creazione trackbar 
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)                                                   
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)


"""lower_blue = np.array([30, 163, 99])
upper_blue = np.array([179, 255, 255])"""

def convertiX(x):                                                                                           #conversione delle coordinate X dell'oggetto in coordinate utilizzabili nella matrice
    return math.floor(x/c.CELL)

def convertiY(y):                                                                                           #conversione delle coordinate X dell'oggetto in coordinate utilizzabili nella matrice
    return math.floor(y/c.CELL)

#############################
#SELEZIONE DEGLI INDOVINELLI#
#############################

def indovinello(screen,nlvl):
    x = pygame.image.load("Image\X.png")                                                                    #Caricamento dell'immagine X.png
    if nlvl == 1:                                                                                           #Selezione dell'indovinello per il livello 1
        bg = pygame.image.load("Image\Riddle1.png")                                                         #caricamento immagine per indovinello 1
        bg = pygame.transform.scale(bg, (800,800))                                                          #ridimensionamento immagine
        screen.blit(bg,(0,0))                                                                               #stampa dell'immagine
        while True:
            for event in pygame.event.get():                                                                
                if event.type == pygame.MOUSEBUTTONDOWN:                                                    #attende finch?? non viene cliccato un tasto del mouse
                    mouseX = event.pos[0]                                                                   #salva le coordinate del puntatore del mouse
                    mouseY = event.pos[1]
                    if mouseX > c.RISP1_BTN_CORD[0] and mouseX < c.RISP1_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP1_BTN_CORD[1] and mouseY < c.RISP1_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP1_BTN_CORD))               #stampa della x (risposta sbagliata)
                    if mouseX > c.RISP2_BTN_CORD[0] and mouseX < c.RISP2_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP2_BTN_CORD[1] and mouseY < c.RISP2_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP2_BTN_CORD))               #stampa della x (risposta sbagliata)
                    if mouseX > c.RISP3_BTN_CORD[0] and mouseX < c.RISP3_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP3_BTN_CORD[1] and mouseY < c.RISP3_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        return True                                     #ritorna True (risposta corretta)
            pygame.display.update()

    if nlvl == 2:                                                                                           #Selezione dell'indovinello per il livello 2
        bg = pygame.image.load("Image\Riddle2.png")                                                         #caricamento immagine per indovinello 2
        bg = pygame.transform.scale(bg, (800,800))                                                          #ridimensionamento immagine
        screen.blit(bg,(0,0))                                                                               #stampa dell'immagine
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:                                                    #attende finch?? non viene cliccato un tasto del mouse
                    mouseX = event.pos[0]                                                                   #salva le coordinate del puntatore del mouse
                    mouseY = event.pos[1]
                    if mouseX > c.RISP1_BTN_CORD[0] and mouseX < c.RISP1_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP1_BTN_CORD[1] and mouseY < c.RISP1_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP1_BTN_CORD))               #stampa della x (risposta sbagliata)
                    if mouseX > c.RISP2_BTN_CORD[0] and mouseX < c.RISP2_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP2_BTN_CORD[1] and mouseY < c.RISP2_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick) 
                        return True                                     #ritorna True (risposta corretta)
                    if mouseX > c.RISP3_BTN_CORD[0] and mouseX < c.RISP3_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP3_BTN_CORD[1] and mouseY < c.RISP3_BTN_CORD[1]+c.RISP_BTN_DIM[1]:    
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP3_BTN_CORD))               #stampa della x (risposta sbagliata)
            pygame.display.update()

    if nlvl == 3:                                                                                           #Selezione dell'indovinello per il livello 3
        bg = pygame.image.load("Image\Riddle3.png")                                                         #caricamento immagine per indovinello 3
        bg = pygame.transform.scale(bg, (800,800))                                                          #ridimensionamento immagine
        screen.blit(bg,(0,0))                                                                               #stampa dell'immagine
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:                                                    #attende finch?? non viene cliccato un tasto del mouse
                    mouseX = event.pos[0]                                                                   #salva le coordinate del puntatore del mouse
                    mouseY = event.pos[1]
                    if mouseX > c.RISP1_BTN_CORD[0] and mouseX < c.RISP1_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP1_BTN_CORD[1] and mouseY < c.RISP1_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP1_BTN_CORD))               #stampa della x (risposta sbagliata)
                    if mouseX > c.RISP2_BTN_CORD[0] and mouseX < c.RISP2_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP2_BTN_CORD[1] and mouseY < c.RISP2_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        return True                                     #ritorna True (risposta corretta)
                    if mouseX > c.RISP3_BTN_CORD[0] and mouseX < c.RISP3_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP3_BTN_CORD[1] and mouseY < c.RISP3_BTN_CORD[1]+c.RISP_BTN_DIM[1]:    
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP3_BTN_CORD))               #stampa della x (risposta sbagliata)
            pygame.display.update()

    if nlvl == 4:                                                                                           #Selezione dell'indovinello per il livello 4
        bg = pygame.image.load("Image\Riddle4.png")                                                         #caricamento immagine per indovinello 4
        bg = pygame.transform.scale(bg, (800,800))                                                          #ridimensionamento immagine
        screen.blit(bg,(0,0))                                                                               #stampa dell'immagine
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:                                                    #attende finch?? non viene cliccato un tasto del mouse
                    mouseX = event.pos[0]                                                                   #salva le coordinate del puntatore del mouse
                    mouseY = event.pos[1]
                    if mouseX > c.RISP1_BTN_CORD[0] and mouseX < c.RISP1_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP1_BTN_CORD[1] and mouseY < c.RISP1_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP1_BTN_CORD))               #stampa della x (risposta sbagliata)
                    if mouseX > c.RISP2_BTN_CORD[0] and mouseX < c.RISP2_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP2_BTN_CORD[1] and mouseY < c.RISP2_BTN_CORD[1]+c.RISP_BTN_DIM[1]:
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        return True                                     #ritorna True (risposta corretta)
                    if mouseX > c.RISP3_BTN_CORD[0] and mouseX < c.RISP3_BTN_CORD[0]+c.RISP_BTN_DIM[0] and mouseY > c.RISP3_BTN_CORD[1] and mouseY < c.RISP3_BTN_CORD[1]+c.RISP_BTN_DIM[1]:    
                        pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                        pygame.mixer.Sound.play(soundClick)
                        screen.blit(x,(c.RISP3_BTN_CORD))               #stampa della x (risposta sbagliata)

            pygame.display.update()

####################################################
#CONTROLLO DEL COLLASSO CONTRO I MURI DEL LABIRINTO#
####################################################

def wallControll(player,x,y,level):
    if x > 240 and x < 360 and y > 200 and y < 280:
            print("centro, fermo")
    if x > 240 and x < 360 and y > 0 and y < 200:
        if level[convertiY((player.getY())-3)][convertiX(player.getX())] != "o" and level[convertiY((player.getY())-3)][convertiX(player.getX()+30)] != "o":
            player.setY(-2)
    if x > 240 and x < 360 and y > 280 and y < 480:
        if level[convertiY((player.getY())+23)][convertiX(player.getX())] != "o" and level[convertiY((player.getY())+23)][convertiX(player.getX()+30)] != "o":
            player.setY(2)
    if x > 0 and x < 240 and y > 200 and y < 280:
        if level[convertiY(player.getY())][convertiX((player.getX())-3)] != "o" and level[convertiY(player.getY()+20)][convertiX((player.getX())-3)] != "o":
            player.setX(-2)
    if x > 360 and x < 640 and y > 200 and y < 280:
        if level[convertiY(player.getY())][convertiX((player.getX())+33)] != "o" and level[convertiY(player.getY()+20)][convertiX((player.getX())+33)] != "o":
            player.setX(2)
    if level[convertiY(player.getY())][convertiX((player.getX()))] == "P":  #Controllo per teletrasportare il player
        player.teleport(440,609)
    if level[convertiY(player.getY())][convertiX((player.getX()))] == "A":  #Controllo per la vittoria
        return True
    else: return False

#############################
#SELEZIONE DEGLI INDOVINELLI#
#############################

def lvl(screen,nlvl):
    vittoria = pygame.image.load("Image\Win.png")
    vittoria = pygame.transform.scale(vittoria, (800,800))
    #LIVELLO 1
    if nlvl == 1:
        pygame.mixer.Sound.set_volume(soundLvl1,0.5)                                                        #Setta la traccia musicale del livello 1
        pygame.mixer.Sound.play(soundLvl1, -1)  
        level = c.LEVEL1                                                                                    #Carica la matrice del livello 1
        bg = pygame.image.load("Image\Lab1.jpeg")                                                           #Carica il backgroud del livello 1
        bg = pygame.transform.scale(bg, (800,800))
        x,y = 20,50                                                                                         #Setta le coordinate iniziali del player
    
    #LIVELLO 2
    if nlvl == 2:
        pygame.mixer.Sound.set_volume(soundLvl2,0.5)                                                        #Setta la traccia musicale del livello 2
        pygame.mixer.Sound.play(soundLvl2, -1)
        bg = pygame.image.load("Image\Lab2.png")                                                            #Carica il backgroud del livello 2
        bg = pygame.transform.scale(bg, (800,800))
        x,y = 760,420                                                                                       #Setta le coordinate iniziali del player
        level = c.LEVEL2                                                                                    #Carica la matrice del livello 2
    
    #LIVELLO 3
    if nlvl == 3:
        pygame.mixer.Sound.set_volume(soundLvl3,0.5)                                                        #Setta la traccia musicale del livello 3
        pygame.mixer.Sound.play(soundLvl3, -1) 
        bg = pygame.image.load("Image\Lab3.png")                                                            #Carica il backgroud del livello 3
        bg = pygame.transform.scale(bg, (800,800))
        x,y = 355,1                                                                                         #Setta le coordinate iniziali del player
        level = c.LEVEL3                                                                                    #Carica la matrice del livello 3

    #LIVELLO 4
    if nlvl == 4:
        pygame.mixer.Sound.set_volume(soundLvl4,0.5)                                                        #Setta la traccia musicale del livello 4
        pygame.mixer.Sound.play(soundLvl4, -1) 
        bg = pygame.image.load("Image\Lab4.png")                                                            #Carica il backgroud del livello 4
        bg = pygame.transform.scale(bg, (800,800))
        x,y = 45,1                                                                                          #Setta le coordinate iniziali del player
        level = c.LEVEL4                                                                                    #Carica la matrice del livello 4

    player = p.Pallina(x,y)                                                                                 #Crea l'oggetto player con le coordinate precedentemente date


    while True:
        _, frame = cap.read()                                                                               # _ bool per vedere se la cattura dal frame dalla cam ha avuto successo o meno, img frame della cam
        frameFlip = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frameFlip, cv2.COLOR_BGR2HSV)                                                    #converto il frame da BGR in HSV    (H colore, S concentrazione colore, V lucentezza colore)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        lower_blue = np.array([l_h, l_s, l_v])                                                              #parte "bassa" del range dei colori (colore pi?? scuro)
        upper_blue = np.array([u_h, u_s, u_v])                                                              #parte "alta" del range dei colori (colore pi?? chiaro)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)                                                     #creazione maschera (vengono salvati solo i colori che stanno nel range)

        mask = cv2.erode(mask, kernel, iterations=5)                                                        #perfezionamento della maschera
        mask = cv2.dilate(mask, kernel, iterations=5)                                                       #perfezionamento della maschera
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        x, y, w, h = cv2.boundingRect(opening)                                                              #salvataggio delle coordinate dell'oggetto

        result = cv2.bitwise_and(frameFlip, frameFlip, mask=mask)                                           #risultato finale della maschera

        #cv2.imshow("frame", frameFlip)
        #cv2.imshow("mask", mask)
        cv2.imshow("result", result)                                                                        #visualizzazione del risultato finale
        if cv2.waitKey(1) == 27:                                                                            #controllo se nel millisecondo ?? stato schiacciato esc (27) esce dal loop e chiude tutte le finestre
            break

        print(x,y)                                                                                          #stampa delle coordinate (solo debug)
        screen.blit(bg, (0,0))                                                                              #stampa del labirinto in base al livello selezionato
        player.show(screen)                                                                                 #stampa del player nell'area di gioco
        win = wallControll(player,x,y,level)                                                                #controllo della vittoria e del collasso contro un muro
        if win == True and indovinello(screen,nlvl):
            pygame.mixer.Sound.set_volume(soundWin,0.5)                                                     #Suono della vittoria se si vince
            pygame.mixer.Sound.play(soundWin)
            if nlvl == 1:                                                                                   #Si stoppa il suono di sottofondo in base al livello
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
        screen.blit(vittoria,(0,0))                                                                         #stampa della schermata di vittoria
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                                                        #attende finch?? non viene cliccato un tasto del mouse
                mouseX = event.pos[0]                                                                       #salva le coordinate del puntatore del mouse
                mouseY = event.pos[1]
                if mouseX > c.NEXT_BTN_CORD[0] and mouseX < c.NEXT_BTN_CORD[0]+c.MN_BTN_DIM[0] and mouseY > c.NEXT_BTN_CORD[1] and mouseY < c.NEXT_BTN_CORD[1]+c.MN_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick)
                    return True                                     #ritornta True (se si vuole procedere al prossimo livello)
                if mouseX > c.MENU_BTN_CORD[0] and mouseX < c.MENU_BTN_CORD[0]+c.MN_BTN_DIM[0] and mouseY > c.MENU_BTN_CORD[1] and mouseY < c.MENU_BTN_CORD[1]+c.MN_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick)
                    return False                                    #ritorna False (se si vuole tornare al menu)
        pygame.display.update()
    
def start(screen,nlvl):
    global music
    bg = pygame.image.load("Image\Calibration.png")                                                         #caricamento immagine di calibrazione
    ok = pygame.image.load("Image\Ok.png")                                                                  #caricamento immagine OK
    no = pygame.image.load("Image\\No.png")                                                                 #caricamento immagine NO
    bg = pygame.transform.scale(bg, (800,800))                                                              #ridimensionamento immagine
    ok = pygame.transform.scale(ok, (300,200))                                                              #ridimensionamento immagine
    no = pygame.transform.scale(no, (300,200))                                                              #ridimensionamento immagine
    centerTitle2 = ok.get_rect(center=(c.DIM_IMG[0]/2,c.DIM_IMG[1]/2))                                      #ricerca del centro dello schermo
    waitTime = 0
    while True:
        screen.blit(bg,(0,0))                                                                               #stampa dell'immagine di sfondo

        _, frame = cap.read()                                                                               # _ bool per vedere se la cattura dal frame dalla cam ha avuto successo o meno, img frame della cam
        frameFlip = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frameFlip, cv2.COLOR_BGR2HSV)                                                    #converto il frame da BGR in HSV    (H colore, S concentrazione colore, V lucentezza colore)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        lower_blue = np.array([l_h, l_s, l_v])                                                              #parte "bassa" del range dei colori (colore pi?? scuro)
        upper_blue = np.array([u_h, u_s, u_v])                                                              #parte "alta" del range dei colori (colore pi?? chiaro)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)                                                     #creazione maschera (vengono salvati solo i colori che stanno nel range)

        mask = cv2.erode(mask, kernel, iterations=5)                                                        #perfezionamento della maschera
        mask = cv2.dilate(mask, kernel, iterations=5)                                                       #perfezionamento della maschera
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        x, y, w, h = cv2.boundingRect(opening)                                                              #salvataggio delle coordinate dell'oggetto

        result = cv2.bitwise_and(frameFlip, frameFlip, mask=mask)                                           #risultato finale della maschera

        #cv2.imshow("frame", frameFlip)
        #cv2.imshow("mask", mask)
        cv2.imshow("result", result)                                                                        #visualizzazione del risultato finale

        if cv2.waitKey(1) == 27:                                                                            #controllo se nel millisecondo ?? stato schiacciato esc (27) esce dal loop e chiude tutte le finestre
            break
        
        if x > 240 and x < 360 and y > 200 and y < 280:                                                     #se l'oggetto ?? posizionato al centro, quindi in posizione corretta, stampa OK
            screen.blit(ok, centerTitle2)
            waitTime+=1
            if waitTime==50:                                                                                #attende un po' di tempo
                pygame.mixer.Sound.stop(soundMenu)                                                          #ferma il suono del menu
                music = 0
                rigioca = lvl(screen,nlvl)                                                                  #fa partire il livello
                if rigioca == True and nlvl < 4:                                                            #se si preme next e i livelli non sono terminati aumenta il livello di 1 (prossimo livello)
                        nlvl += 1
                else:
                    break
        else:
            screen.blit(no, centerTitle2)                                                                   #se l'oggetto non ?? posizionato al centro, quindi non in posizione corretta, stampa NO
            waitTime=0

        pygame.display.update()

def level(screen):
    global music
    bg = pygame.image.load("Image\LabAll.png")                                                              #caricamento immagine di tutti i labirinti
    menu = pygame.image.load("Image\ButtonMenu.png")                                                        #caricamento immagine del bottone menu
    bg = pygame.transform.scale(bg, (800,800))                                                              #ridimensionamento immagine
    menu = pygame.transform.scale(menu,(180,80))                                                            #ridimensionamento immagine
    while True:
        if music == 0:
            pygame.mixer.Sound.set_volume(soundMenu,0.5)                                                    #Se non vi ?? gi??, fa partire la musica del menu
            pygame.mixer.Sound.play(soundMenu, -1)
            music = 1
        screen.blit(bg,(0,0))                                                                               #stampa dell'immagine
        screen.blit(menu,(310,700))                                                                         #stampa dell'immagine
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                                                        #attende finch?? non viene cliccato un tasto del mouse
                mouseX = event.pos[0]                                                                       #salva le coordinate del puntatore del mouse
                mouseY = event.pos[1]
                if mouseX > c.LVL1_BTN_CORD[0] and mouseX < c.LVL1_BTN_CORD[0]+c.LVL_BTN_DIM[0] and mouseY > c.LVL1_BTN_CORD[1] and mouseY < c.LVL1_BTN_CORD[1]+c.LVL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick)
                    start(screen,1)                                 #fa partire il livello 1
                if mouseX > c.LVL2_BTN_CORD[0] and mouseX < c.LVL2_BTN_CORD[0]+c.LVL_BTN_DIM[0] and mouseY > c.LVL2_BTN_CORD[1] and mouseY < c.LVL2_BTN_CORD[1]+c.LVL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick)
                    start(screen,2)                                 #fa partire il livello 2
                if mouseX > c.LVL3_BTN_CORD[0] and mouseX < c.LVL3_BTN_CORD[0]+c.LVL_BTN_DIM[0] and mouseY > c.LVL3_BTN_CORD[1] and mouseY < c.LVL3_BTN_CORD[1]+c.LVL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick)
                    start(screen,3)                                 #fa partire il livello 3
                if mouseX > c.LVL4_BTN_CORD[0] and mouseX < c.LVL4_BTN_CORD[0]+c.LVL_BTN_DIM[0] and mouseY > c.LVL4_BTN_CORD[1] and mouseY < c.LVL4_BTN_CORD[1]+c.LVL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick)
                    start(screen,4)                                 #fa partire il livello 4
                if mouseX > c.MENU2_BTN_CORD[0] and mouseX < c.MENU2_BTN_CORD[0]+c.MENU2_BTN_DIM[0] and mouseY > c.MENU2_BTN_CORD[1] and mouseY < c.MENU2_BTN_CORD[1]+c.MENU2_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick)
                    return                                          #torna al menu
        pygame.display.update()

def menu(screen):
    global music
    bg = pygame.image.load("Image\Menu.png")                                                                #caricamento immagine del menu
    bg = pygame.transform.scale(bg, (800,800))                                                              #ridimensionamento immagine
    while True:
        if music == 0:
            pygame.mixer.Sound.set_volume(soundMenu,0.5)                                                    #Se non vi ?? gi??, fa partire la musica del menu
            pygame.mixer.Sound.play(soundMenu, -1)
            music = 1
        screen.blit(bg, (0,0))                                                                              #stampa dell'immagine
        for event in pygame.event.get():                                                                    
            if event.type == pygame.MOUSEBUTTONDOWN:                                                        #attende finch?? non viene cliccato un tasto del mouse
                mouseX = event.pos[0]                                                                       #salva le coordinate del puntatore del mouse
                mouseY = event.pos[1]
                if mouseX > c.START_BTN_CORD[0] and mouseX < c.START_BTN_CORD[0]+c.START_BTN_DIM[0] and mouseY > c.START_BTN_CORD[1] and mouseY < c.START_BTN_CORD[1]+c.START_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick) 
                    start(screen,1)                                 #fa partire il livello 1
                    

                if mouseX > c.LEVEL_BTN_CORD[0] and mouseX < c.LEVEL_BTN_CORD[0]+c.LEVEL_BTN_DIM[0] and mouseY > c.LEVEL_BTN_CORD[1] and mouseY < c.LEVEL_BTN_CORD[1]+c.LEVEL_BTN_DIM[1]:
                    pygame.mixer.Sound.set_volume(soundClick,1)     #Suono del Click del mouse
                    pygame.mixer.Sound.play(soundClick) 
                    level(screen)                                   #va alla schermata per la scelta dei livelli

        pygame.display.update()

def main():
    dim = (len(c.LEVEL1[1])*c.CELL,len(c.LEVEL1)*c.CELL)                                                    #setta le dimensioni dello schermo
    pygame.init()                                                                                           #inizializzazione del modulo pygame
    pygame.display.set_caption('Fly Maze')                                                                  #nome della scheda con il gioco
    screen = pygame.display.set_mode(dim)                                                                   #creazione dello schermo
    menu(screen)                                                                                            #inizio del gioco

if __name__ == "__main__":
    main()