import pygame 
import sys 
import random
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Typing")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont(None, 72)
score_font = pygame.font.SysFont(None, 36)

TARGET_KEYS = ['D','F','J','K']
LANES = [50, 150, 250, 350]

key_y = -100
key_x = random.choice(LANES)
key_char = random.choice(TARGET_KEYS)
fall_speed = 5
score = 0
lives = 3

BASE_DIR = Path(__file__).resolve().parent
SOUND_DIR = BASE_DIR / 'sound'
hit_sound = pygame.mixer.Sound(str(SOUND_DIR/"check.ogg"))

#hit_sound = pygame.mixer.Sound("flies/music_typing /sound/check.ogg")

def reset_key():
    global key_y, key_x, key_char

    key_y = -100
    key_x = random.choice(LANES)
    key_char = random.choice(TARGET_KEYS)

def show_gameover():
    screen.fill((0,0,0))
    text = FONT.render("GAME OVER", True, (255,0,0))
    screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2 - 40))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: 
            if 450 < key_y < 520:

                if event.unicode.upper() == key_char:
                    score += 1
                    hit_sound.play()
                    reset_key()

       
        #배경 설정  
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,255,255), (key_x -25, key_y,50,50))
    text = FONT.render(key_char, True,(0,0,0))
    screen.blit(text, (key_x - 20, key_y)) 

    pygame.draw.line(screen, (255,0,0), (0,500), (WIDTH, 500),3)

    score_text = score_font.render(f"Score: {score}", True, (255,255,255))
    lives_text = score_font.render(f"Lives: {lives}", True, (255,255,255))
    screen.blit(score_text, (10,10))
    screen.blit(lives_text, (10,50))


    key_y += fall_speed

    if key_y > HEIGHT:
        lives -= 1
        if lives <= 0: 
            show_gameover()
        reset_key()

        # 화면 업데이트 
    pygame.display.update()
    clock.tick(60)