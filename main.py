import pygame
import random
import math

# Initialize game window, set window title and icon:
pygame.init()

score = 0

# Game clock
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
player_speed_change = 2

# Load casey character image
casey_img = pygame.image.load("assets/graphics/enemy_casey.png")
casey_x = random.randint(1, 735)
casey_y = 0
casey_speed_x = random.choice([-6, -5, -4, -3, 4, 5, 6])

# Load weapon image
weapon_img = pygame.image.load("assets/graphics/weapon_shuriken.png")
weapon_x = 0
weapon_y = 0
weapon_speed_y = 5
weapon_state = "ready"


def player(x, y):
    screen.blit(player_img, (x, y))


def casey(x, y):
    screen.blit(casey_img, (x, y))


def weapon(x, y):
    global weapon_state
    weapon_state = "throw"
    screen.blit(weapon_img, (x + 16, y + 10))


def is_hit(casey_x, casey_y, weapon_x, weapon_y):
    distance = math.sqrt((math.pow(casey_x - weapon_x, 2) + math.pow(casey_y - weapon_y, 2)))
    if distance < 25:
        return True


def generate_casey():
    global casey_x, casey_y, casey_speed_x
    casey_x = random.randint(1, 735)
    casey_y = 0
    casey_speed_x = random.choice([-6, -5, -4, 4, 5, 6])


running = True

while running:
    # Game screen background color
    screen.fill((71, 57, 39))

    for event in pygame.event.get():
        # Closing game window
        if event.type == pygame.QUIT:
            running = False

        # Throwing shuriken weapon
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if weapon_state == "ready":
                    weapon_y = player_y
                    weapon_x = player_x
                    weapon(weapon_x, weapon_y)

    # Fixed players movements
    keys = pygame.key.get_pressed()
    player_speed_x = 0
    player_speed_y = 0

    if keys[pygame.K_LEFT]:
        player_speed_x = -player_speed_change
    elif keys[pygame.K_RIGHT]:
        player_speed_x = player_speed_change

    if keys[pygame.K_UP]:
        player_speed_y = -player_speed_change
    elif keys[pygame.K_DOWN]:
        player_speed_y = player_speed_change

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

    if weapon_y <= -32:
        weapon_y = -50
        weapon_state = "ready"

    if weapon_state == "throw":
        weapon(weapon_x, weapon_y)
        weapon_y -= weapon_speed_y

    # Check if weapon hit enemy
    hit = is_hit(casey_x, casey_y, weapon_x, weapon_y)
    if hit:
        weapon_state = "ready"
        weapon_y = -50
        score += 1
        generate_casey()

    casey(casey_x, casey_y)

    pygame.display.update()
    clock.tick(60)
