import pygame

class Pallina():
    def __init__(self,x,y):
        self.pallina = pygame.image.load("Pallina.png")
        self.centroX = x
        self.centroY = y
    
    def show(self,screen):
        screen.blit(self.pallina,(self.centroX,self.centroY))
    
    def setX(self,x):
        self.centroX = self.centroX + (x)

    def setY(self,y):
        self.centroY = self.centroY + (y)