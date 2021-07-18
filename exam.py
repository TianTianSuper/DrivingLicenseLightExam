import sys
import pygame
import broadcast
import problems
import manager


size = width, height = 1024, 768

def run_exam():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("科目三模拟夜考")

    screen.fill((30, 30, 30))
    pygame.display.update()


    # 监听键盘
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pygame.quit()
                    sys.exit()



run_exam()
