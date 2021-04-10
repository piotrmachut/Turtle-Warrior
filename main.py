import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Turtle Warrior")

icon = pygame.image.load("assets/graphics/icon.png")
pygame.display.set_icon(icon)

running = True

while running:
    screen.fill((71, 57, 39))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
