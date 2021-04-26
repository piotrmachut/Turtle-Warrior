import pygame

# Initialize game window, set window title and icon:
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Turtle Warrior")

icon = pygame.image.load("assets/graphics/icon.png")
pygame.display.set_icon(icon)

# Load player's character image and set its' basic position:
player_img = pygame.image.load("assets/graphics/player_donatello.png")
player_x = 368
player_y = 480
player_speed_x = 0
player_speed_y = 0


def player(x, y):
    screen.blit(player_img, (x, y))


running = True

while running:
    # Game screen background color
    screen.fill((71, 57, 39))

    # Player movements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_x = -0.1
            if event.key == pygame.K_RIGHT:
                player_speed_x = 0.1
            if event.key == pygame.K_UP:
                player_speed_y = -0.1
            if event.key == pygame.K_DOWN:
                player_speed_y = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed_y = 0

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

    # make magic come true: run player character function
    player(player_x, player_y)

    pygame.display.update()
