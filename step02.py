import pygame 
import sys 
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step2 - Falling key")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont(None, 72)

TARGET_KEYS = ['D','F','J','K']
LANES = [50, 150, 250, 350]

key_y = -100
key_x = random.choice(LANES)
key_char = random.choice(TARGET_KEYS)
fall_speed = 5

def reset_key():
    global key_y, key_x, key_char

    key_y = -100
    key_x = random.choice(LANES)
    key_char = random.choice(TARGET_KEYS)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        #배경 설정  
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,255,255), (key_x -25, key_y,50,50))
    text = FONT.render(key_char, True,(0,0,0))
    screen.blit(text, (key_x - 20, key_y)) 

    key_y += fall_speed

    if key_y > HEIGHT:
        reset_key()

        # 화면 업데이트 
    pygame.display.update()
    clock.tick(60)