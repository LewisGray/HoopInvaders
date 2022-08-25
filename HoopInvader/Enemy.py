import pygame
class enemy:
    def __init__(self,enemyImg,enemyX,enemyY):
        self.enemyImg = enemyImg
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = 1
        self.enemyY_change = 30

    def drawEnemy(self,screen):
        screen.blit(self.enemyImg, (self.enemyX,self.enemyY))

    def checkInBounds(self):
        if self.enemyX < 0:
            self.enemyX = 0
            self.enemyX_change = 1
            self.enemyY += self.enemyY_change
        elif self.enemyX >= 700:
            self.enemyX = 700
            self.enemyX_change = -1
            self.enemyY += self.enemyY_change

    def moveX(self):
        self.enemyX += self.enemyX_change