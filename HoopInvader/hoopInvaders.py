#TO DO:
#Ball returns to player
#Game over screen
#Set specfic spawn heights
#Score system rework
#Menu System implementation
#Player 2 skin

import math
import pygame
import random
from Enemy import enemy
from pygame import mixer
# Initialize pygame
pygame.init()

#Creating the screen      #X = 800 Y = 600
screen = pygame.display.set_mode((800, 600))

#Setting the font for the game labels
font = pygame.font.Font("KGHAPPY.ttf",40)

#Implementing a timer
current_time = 0
gameTime = 60

def display_timer(x,y):
    timer = font.render("Time Remaining: "+str(current_time),True, (255,255,255))
    screen.blit(timer,(x,y))






#Setting the number of enemies
noOfEnemies = 4

#Title, Icon and background
pygame.display.set_caption("Hoop Invaders")
icon = pygame.image.load("ball.png")
pygame.display.set_icon(icon)
background = pygame.image.load("wall.png")

#Backing track
mixer.music.load("Like Mike - We're Playing Basketball.wav")
mixer.music.play(-1)

#Player
playerImg = pygame.image.load("player1.png")
playerX = 370
playerY = 430
playerX_change = 0
#Hoop
hoopList = []
hoopImg = pygame.image.load("hoop.png")

#Creating and storing the enemy hoops
for eachHoop in range(noOfEnemies):
    hoop = enemy(hoopImg,random.randint(0,800),random.randint(50,150))
    hoopList.append(hoop)


#Ball
ballImg = pygame.image.load("ball.png")
ballX = 0
ballY = 425
ballX_change = 0
ballY_change = 5

#Ball state
ball_state = "Ready"


#Score
score_value = 0

def display_score(x,y):
    score = font.render("score "+str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))


#Functions that draw an image onto the screen
def player(x,y):
    screen.blit(playerImg,(x,y))

def shoot(x,y):
    global ball_state
    ball_state = "Fire"
    screen.blit(ballImg, (x+16,y+10))

def returnBall(x,y):
    global ball_state
    ball_state = "Return"
    screen.blit(ballImg, (x,y))

def collision(objaX,objaY,objbX,objbY):
    #Calculating the distance between the two objects on the screen
    d = math.sqrt(math.pow(objaX - objbX,2)+(math.pow(objaY - objbY,2)))
    #Checking if the points are close enough to warrant a collision
    if d < 53:
        print(d)
        return True
    else:
        return False

#Game Loop
running = True
while running:
    # Anything persistent/static goes here (Eg.Background)
    screen.fill((165, 42, 42))
    screen.blit(background,(0,0))

    #Loop that checks for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left key pressed")
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                print("Right key pressed")
                playerX_change = 2
            #Shooting Mechanic
            if event.key == pygame.K_SPACE:
                print("Space key pressed")
                if ball_state == "Ready":
                    ballX = playerX +42
                    shoot(ballX, ballY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    #Adding a timer
    current_time =gameTime - pygame.time.get_ticks()//1000

    #Applying movement
    for eachHoop in hoopList:
        eachHoop.moveX()
    playerX += playerX_change

    #Setting boundaries#

    #For player
    if playerX < 0:
        playerX = 0
    elif playerX >=685:
        playerX = 685

    # For hoops

    for eachHoop in hoopList:
        eachHoop.checkInBounds()





    #Ball movement
    if ball_state == "Fire":
        shoot(ballX,ballY)
        ballY -= ballY_change
        if ballY <= 0:
            ball_state = "Return"


    if ball_state == "Return":
        returnBall(ballX,ballY)
        ballY += ballY_change
        if ballY > 430:
            ball_state = "Ready"
            ballY = 430


    # Collision detection- check each hoop on screen to see if it's been hit
    for eachHoop in hoopList:
        if collision(eachHoop.enemyX + 20, eachHoop.enemyY, ballX, ballY) == True:
            ball_state = "Return"
            print("Hit!")
            eachHoop.enemyY = random.randint(50,150)
            eachHoop.enemyX = random.randint(0, 800)
            score_value +=1


    #--------------------
    #Draw the updated screen
    player(playerX,playerY)
    for eachHoop in hoopList:
        eachHoop.drawEnemy(screen)

    display_score(10,530)
    display_timer(330,0)

    #Game over code
    if current_time <=0:
        print("Time up")
    print(ball_state)
    pygame.display.update()
