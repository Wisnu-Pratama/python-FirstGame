#PYGAME TEMPLATES
import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Initialize pygame and create Window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Game Loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    #Process Input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

    #Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #*after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()