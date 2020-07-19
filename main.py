import pygame

pygame.init()

stone_size_x = 48
stone_size_y = 50

icon = pygame.image.load('assets/go_icon.jpg')
black_stone = pygame.image.load('assets/black_stone.png')
pygame.transform.scale(black_stone, (stone_size_x, stone_size_y))
white_stone = pygame.image.load('assets/white_stone.png')
pygame.transform.scale(white_stone, (stone_size_x, stone_size_y))

res_x = 900
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


def game_func():
    return 0


def end_func():
    return 0


#
game_state = 0

switch = {
    0: menu_func,
    1: game_func,
    2: end_func
}

running = True

while running:
    screen.fill((52, 182, 229))

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

    stone(100, 200)

    pygame.display.update()