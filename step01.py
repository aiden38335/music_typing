import pygame 
import sys 

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step1 - Window")
clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        #배경 설정  
    screen.fill((0,0,0))

        # 화면 업데이트 
    pygame.display.update()
    clock.tick(60)

