import pygame
import random
import math

# Initialize game window, set window title and icon:
pygame.init()

# Game scores
score = 0
font = pygame.font.Font("assets/fonts/Turtles.otf", 32)
score_text_x = 10
score_text_y = 10


def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (x, y))


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

# Load enemy characters image and set its speed
enemy_img = []
enemy_x = []
enemy_y = []
enemy_speed_x = []
number_of_enemies = 6

for i in range(number_of_enemies):
    enemy_img.append(pygame.image.load("assets/graphics/enemy_casey.png"))
    enemy_x.append(random.randint(1, 735))
    enemy_y.append(0)
    enemy_speed_x.append(random.choice([-6, -5, -4, -3, 4, 5, 6]))

# Load weapon image
weapon_img = pygame.image.load("assets/graphics/weapon_shuriken.png")
weapon_x = -50
weapon_y = -50
weapon_speed_y = 5
weapon_state = "ready"


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def weapon(x, y):
    global weapon_state
    weapon_state = "throw"
    screen.blit(weapon_img, (x + 16, y + 10))


def is_hit(enemy_x, enemy_y, weapon_x, weapon_y):
    distance = math.sqrt((math.pow(enemy_x - weapon_x, 2) + math.pow(enemy_y - weapon_y, 2)))
    if distance < 25:
        return True


def generate_enemy(i):
    global enemy_x, enemy_y, enemy_speed_x
    enemy_x[i] = random.randint(1, 735)
    enemy_y[i] = 0
    enemy_speed_x[i] = random.choice([-6, -5, -4, 4, 5, 6])


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
    for i in range(number_of_enemies):
        if enemy_x[i] <= 0:
            enemy_speed_x[i] *= -1
            enemy_y[i] += 32
        elif enemy_x[i] >= 736:
            enemy_speed_x[i] *= -1
            enemy_y[i] += 32

        # Check if weapon hit enemy
        hit = is_hit(enemy_x[i], enemy_y[i], weapon_x, weapon_y)
        if hit:
            weapon_state = "ready"
            weapon_y = -50
            score += 1
            generate_enemy(i)

        enemy(enemy_x[i], enemy_y[i], i)

        enemy_x[i] += enemy_speed_x[i]

    if weapon_y <= -32:
        weapon_y = -50
        weapon_state = "ready"

    if weapon_state == "throw":
        weapon(weapon_x, weapon_y)
        weapon_y -= weapon_speed_y

    player(player_x, player_y)
    show_score(score_text_x, score_text_y)

    pygame.display.update()
    clock.tick(60)
