import pygame

WIDTH = 800
HEIGHT = 600
SIDEBAR_WIDTH = 200
FPS = 60

numQueens = 10

SQUARE_SIZE = (WIDTH - SIDEBAR_WIDTH) // numQueens

QUEEN_IMAGE = pygame.transform.scale(
    pygame.image.load("example.png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hey Hajjar")
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(pygame.Color("white"))
        drawGameState(screen)
        pygame.display.flip()
    pygame.quit()


def drawGameState(screen):
    drawBoard(screen)


def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("light blue")]
    for row in range(numQueens):
        for col in range(numQueens):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(
                col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(QUEEN_IMAGE, pygame.Rect(col * SQUARE_SIZE,
                                                 row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


main()
