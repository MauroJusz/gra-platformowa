import pygame
from pygame.locals import *
import random



class Platform():

    image = pygame.image.load("platform.png")
    counter = 0


    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.image = pygame.image.load("platform.png")
        self.Rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if Platform.counter % 20 == 0:
            self.x = 0
            self.image = pygame.transform.scale(self.image,( SCREEN_WIDTH, self.image.get_height()))
        self.Rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        Platform.counter += 1



    def draw(self):
        screen.blit(self.image, (self.x + offsetX, self.y + offsetY))




scianaL = 95
scianaP = 675


# Rozpoczyna działanie PyGame
pygame.init()

# Dzięki tym dwóm linijkom mamy stałe 60 klatek na sekundę;
clock = pygame.time.Clock()
fps = 60


# ZMIENNE GRACZA:

# # Zmienne przechowujące pozycje gracza:
playerX = 400
playerY = 350

# # Zmienne przechowujące prędkość gracza:
playerVelocityX = 0
playerVelocityY = 0

# Wymiary okna gry przechowywane w postaci dwóch zmiennych:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# screen - Okienko gry (oraz wybranie rozdzielczości ekranu;
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Nazwa okienka
pygame.display.set_caption('Icy Tower (be)')

canJump = False


platformList = []
for i in range(500):
    posX = random.randint(scianaL + 30, scianaP - Platform.image.get_width() + 10)
    posY = 400 - 100 * i
    platformList.append(Platform(posX, posY))

offsetX = 0
offsetY = 0


# Wczytanie obrazka do obiektu
hero = pygame.image.load('stickman.png')
background = pygame.image.load('background.png')
red_bg = pygame.image.load('red_bg.png')
green_bg = pygame.image.load('green_bg.png')



run = True
while run:

    # Zegar gry - pilnuje, żeby gra działała w 60-ciu FPS-ach.
    clock.tick(fps)

    # LOGIKA GRY:

    # Przechwytywanie klawiszy gry:
    keys = pygame.key.get_pressed()
    if keys[K_UP] and canJump:
        playerVelocityY = - (10 + 0.7 * abs(playerVelocityX))
        canJump = False
    if keys[K_DOWN]:
        playerVelocityY += 1
    if keys[K_LEFT]:
        playerVelocityX -= 0.5
    if keys[K_RIGHT]:
        playerVelocityX += 0.5
    if keys[K_w]:
        offsetY += 3
    if keys[K_s]:
        offsetY += -3

    # Dodanie siły grawitacji do gry;
    playerVelocityY += 0.5

    # Dodanie siły oporu:
    playerVelocityX *= 0.98
    playerVelocityY *= 0.98


    playerX += playerVelocityX
    playerY += playerVelocityY



    # Sprawdzanie, czy gracz nie wyszedł poza ekran;
    if playerX < 95:
        playerX = 95
        playerVelocityX *= -1
    if playerX > 675 - hero.get_width():
        playerX = 675 - hero.get_width()
        playerVelocityX *= -1


    if playerY > SCREEN_HEIGHT - hero.get_height():
        playerY = SCREEN_HEIGHT - hero.get_height()
        playerVelocityY = 0
        canJump = True


    playerRect = Rect(playerX, playerY, hero.get_width(), hero.get_height())

    for platform in platformList:
        if playerRect.colliderect(platform.Rect) and playerVelocityY > 0:
            playerY = platform.y - hero.get_height()
            canJump = True
            playerVelocityY = 0
            playerVelocityX *= 0.95


    # RYSOWANIE OBIEKTÓW W GRZE:

    # Wypełnienie ekranu gry:
    screen.fill((0, 0, 30))

    # Rysowane obiektów na ekranie

    screen.blit(background, (0, 0 * SCREEN_HEIGHT + offsetY / 3))
    screen.blit(background, (0, 2 * SCREEN_HEIGHT + offsetY / 3 - 3 * SCREEN_HEIGHT))
    screen.blit(background, (0, 3 * SCREEN_HEIGHT + offsetY / 3 - 5 * SCREEN_HEIGHT))
    screen.blit(background, (0, 4 * SCREEN_HEIGHT + offsetY / 3 - 7 * SCREEN_HEIGHT))
    screen.blit(red_bg, (0, 5 * SCREEN_HEIGHT + offsetY / 3 - 9 * SCREEN_HEIGHT ))
    screen.blit(red_bg, (0, 6 * SCREEN_HEIGHT + offsetY / 3 - 11 * SCREEN_HEIGHT))
    screen.blit(red_bg, (0, 7 * SCREEN_HEIGHT + offsetY / 3 - 13 * SCREEN_HEIGHT))
    screen.blit(red_bg, (0, 8 * SCREEN_HEIGHT + offsetY / 3 - 15 * SCREEN_HEIGHT))
    screen.blit(red_bg, (0, 9 * SCREEN_HEIGHT + offsetY / 3 - 17 * SCREEN_HEIGHT))
    screen.blit(green_bg, (0, 10 * SCREEN_HEIGHT + offsetY / 3 - 19 * SCREEN_HEIGHT))
    screen.blit(green_bg, (0, 11 * SCREEN_HEIGHT + offsetY / 3 - 21 * SCREEN_HEIGHT))

    for platform in platformList:
        platform.draw()

    screen.blit(hero, (playerX + offsetX, playerY + offsetY))



    # To jest TURBOWAŻNE I NIE USUWAJ TEGO!!!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if playerY + offsetY < 200:
        offsetY += 2
    if playerY + offsetY < 150:
        offsetY += 3
    if playerY + offsetY < 100:
        offsetY += 5
    if playerY + offsetY > SCREEN_HEIGHT:
        run = False




    offsetY += 1




    # To tworzy nową klatkę gry;
    pygame.display.update()

pygame.quit()



