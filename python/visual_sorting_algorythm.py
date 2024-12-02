import pygame
import random
import time


pygame.init()
res_x = 420
res_y = 600
screen = pygame.display.set_mode((res_x, res_y))
clock = pygame.time.Clock()
running = True
dt = 0

lst = [random.randint(10, int(res_y) // 10) for i in range(50)]
bar_width = res_x / len(lst)
ph = 0

def draw_bars(lst, highlighted_index = None):
    screen.fill("black")
    for i, height in enumerate(lst):
        color = (0,255,0) if i == highlighted_index else (255,255,255)
        pygame.draw.rect(screen, color , (i * bar_width , res_y - height*10, bar_width, height * 10))
    pygame.display.update()

while running:

    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            draw_bars(lst, j)
            pygame.time.delay(10)
            if event.type == pygame.QUIT:
                running = False
            if lst[j] > lst[j + 1]:
                ph = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = ph
                print(lst)
                

    pygame.display.flip()

    clock.tick(60)

pygame.quit()            

