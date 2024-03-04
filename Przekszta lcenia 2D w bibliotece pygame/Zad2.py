import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
BACKGROUND_COLOR = (255, 255, 255)
CIRCLE_COLOR = (0, 0, 0)
SQUARE_COLOR = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))


circle_radius = 200
circle_position = (WIDTH // 2, HEIGHT // 2)

square_size = 180
square_position = (WIDTH // 2 - square_size // 2, HEIGHT // 2 - square_size // 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.circle(screen, CIRCLE_COLOR, circle_position, circle_radius)

    pygame.draw.rect(screen, SQUARE_COLOR, pygame.Rect(square_position, (square_size, square_size)))

    pygame.display.flip()

pygame.quit()