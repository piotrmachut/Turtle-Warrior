import pygame
import random
import math
from pygame import mixer

# Initialize game window, set window title and icon:
pygame.init()

# Game soundtrack
mixer.music.load("assets/sounds/assets_qpec_-_The_Warrior.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)

# Game score
score = 0
score_font = pygame.font.Font("assets/fonts/Turtles.otf", 32)
score_text_x = 10
score_text_y = 10


def show_score(x, y):
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (x, y))


# Game clock
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Turtle Warrior")

icon = pygame.image.load("assets/graphics/icon.png")
pygame.display.set_icon(icon)

# Load player's character image and set its basic position:
player_img = pygame.image.load("assets/graphics/player_donatello.png")
default_player_x = 368
default_player_y = 480
player_x = default_player_x
player_y = default_player_y
player_speed_x = 0
player_speed_y = 0
player_speed_change = 2

# Load enemy characters image and set its speed
enemy_img = []
enemy_x = []
enemy_y = []
enemy_speed_x = []
number_of_enemies = 6
enemies_characters = ["assets/graphics/enemy_casey.png",
                      "assets/graphics/enemy_karai.png",
                      "assets/graphics/enemy_bebop.png",
                      "assets/graphics/enemy_rocksteady.png",
                      "assets/graphics/enemy_shredder.png",
                      "assets/graphics/enemy_footclan.png"]

for i in range(number_of_enemies):
    enemy_img.append(pygame.image.load(random.choice(enemies_characters)))
    enemy_x.append(random.randint(1, 735))
    enemy_y.append(0)
    enemy_speed_x.append(random.choice([-6, -5, -4, -3, 4, 5, 6]))

# Load weapon image
weapon_img = pygame.image.load("assets/graphics/weapon_shuriken.png")
weapon_x = -50
weapon_y = -50
weapon_speed_y = 5
weapon_state = "ready"

game_over_font = pygame.font.Font("assets/fonts/Turtles.otf", 70)
game_state = "play"


def game_over():
    global game_state, number_of_enemies, enemy_y
    for j in range(number_of_enemies):
        enemy_y[j] = 2000
    game_state = "over"
    game_over_text = game_over_font.render("Game over!", True, (0, 0, 0))
    screen.blit(game_over_text, (200, 250))


def new_game():
    global game_state, score, player_x, player_y, default_player_x, default_player_y
    game_state = "play"
    score = 0
    for i in range(number_of_enemies):
        generate_enemy(i)
    player_x = default_player_x
    player_y = default_player_y


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def weapon(x, y):
    global weapon_state
    weapon_state = "throw"
    screen.blit(weapon_img, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, object_x, object_y, d):
    distance = math.sqrt((math.pow(enemy_x - object_x, 2) + math.pow(enemy_y - object_y, 2)))
    if distance < d:
        return True


def generate_enemy(i):
    global enemy_x, enemy_y, enemy_speed_x
    enemy_x[i] = random.randint(1, 735)
    enemy_y[i] = 0
    enemy_speed_x[i] = random.choice([-6, -5, -4, 4, 5, 6])


running = True

while running:
    # Game screen background
    background = pygame.image.load("assets/graphics/background.png")
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # Closing game window
        if event.type == pygame.QUIT:
            running = False

        # Throwing shuriken weapon
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if weapon_state == "ready":
                    weapon_sound = mixer.Sound("assets/sounds/shuriken2.wav")
                    weapon_sound.play()
                    weapon_y = player_y
                    weapon_x = player_x
                    weapon(weapon_x, weapon_y)
            if game_state == "over":
                if event.key == pygame.K_ESCAPE:
                    new_game()

    # Fixed players movements
    keys = pygame.key.get_pressed()
    player_speed_x = 0
    player_speed_y = 0

    if game_state == "play":
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

    # Set game area for enemies:
    for i in range(number_of_enemies):

        if enemy_y[i] > 536:
            game_over()
            break

        if enemy_x[i] <= 0:
            enemy_speed_x[i] *= -1
            enemy_y[i] += 32
        elif enemy_x[i] >= 736:
            enemy_speed_x[i] *= -1
            enemy_y[i] += 32

        # Check if weapon hit enemy
        hit = is_collision(enemy_x[i], enemy_y[i], weapon_x, weapon_y, 25)
        if hit:
            death_sound = mixer.Sound("assets/sounds/death-grunt.wav")
            death_sound.play()
            weapon_state = "ready"
            weapon_y = -50
            score += 1
            generate_enemy(i)

        collision = is_collision(enemy_x[i], enemy_y[i], player_x, player_y, 50)
        if collision:
            game_over()
            break

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
