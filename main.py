import pygame

pygame.init()

stone_size_x = 48
stone_size_y = 50

icon = pygame.image.load('assets/go_icon.jpg')
black_stone = pygame.image.load('assets/black_stone.png')
pygame.transform.scale(black_stone, (stone_size_x, stone_size_y))
white_stone = pygame.image.load('assets/white_stone.png')
pygame.transform.scale(white_stone, (stone_size_x, stone_size_y))

res_x = 600
res_y = 600

screen = pygame.display.set_mode((res_x, res_y))

pygame.display.set_icon(icon)
pygame.display.set_caption("Go")


def stone(x, y):
    screen.blit(black_stone, (x, y))
    screen.blit(white_stone, (res_x - x, res_y - y))
    return 0


def menu_func():
    return 0


board_dimension = 9
block_size = (res_y * 0.9) / board_dimension

def drawGrid():
    for x in range(board_dimension - 1):
        for y in range(board_dimension - 1):
            rect = pygame.Rect(x*block_size + res_x*0.1, y*block_size + res_y*0.1,
                               block_size, block_size)
            pygame.draw.rect(screen, (237, 182, 102), rect, 1)


def game_func():
    drawGrid()


def end_func():
    return 0


#
game_state = 1

switch = {
    0: menu_func,
    1: game_func,
    2: end_func
}

running = True

while running:
    screen.fill((52, 182, 229))

    game_func()

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

    stone(100, 200)

    pygame.display.update()