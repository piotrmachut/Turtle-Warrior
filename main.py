import pygame
import random

# Initialize game window, set window title and icon:
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Turtle Warrior")

icon = pygame.image.load("assets/graphics/icon.png")
pygame.display.set_icon(icon)

# Load player's character image and set its basic position:
player_img = pygame.image.load("assets/graphics/player_donatello.png")
player_x = 368
player_y = 480
player_speed_x = 0
player_speed_y = 0

# Load casey character image
casey_img = pygame.image.load("assets/graphics/enemy_casey.png")
casey_x = random.randint(0, 736)
casey_y = 0
casey_speed_x = 3


def player(x, y):
    screen.blit(player_img, (x, y))


def casey(x, y):
    screen.blit(casey_img, (x, y))


running = True

while running:
    # Game screen background color
    screen.fill((71, 57, 39))

    # Player movements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fixed players movements
    keys = pygame.key.get_pressed()
    player_speed_x = 0
    player_speed_y = 0

    if keys[pygame.K_LEFT]:
        player_speed_x = -2
    elif keys[pygame.K_RIGHT]:
        player_speed_x = 2

    if keys[pygame.K_UP]:
        player_speed_y = -2
    elif keys[pygame.K_DOWN]:
        player_speed_y = 2

    player_x += player_speed_x
    player_y += player_speed_y

    casey_x += casey_speed_x

    # Set game area for player:
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    if player_y <= 0:
        player_y = 0
    elif player_y >= 536:
        player_y = 536

    # Set game area for Casey character:
    if casey_x <= 0:
        casey_speed_x *= -1
        casey_y += 32
    elif casey_x >= 736:
        casey_speed_x *= -1
        casey_y += 32

    # Make magic come true: run player and enemy characters functions
    player(player_x, player_y)

    casey(casey_x, casey_y)

    pygame.display.flip()
    clock.tick(60)
