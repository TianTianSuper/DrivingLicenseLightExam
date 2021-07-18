import sys
import pygame
import broadcast
import problems
import time
import manager

SIZE = width, height = 1024, 768
TIMEOUT = 5


def run_exam():
    # 窗口
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(SIZE)
    icon = pygame.image.load("sources/exam.ico")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("科目三模拟夜考")
    myfont = pygame.font.Font(None, 60)

    background = pygame.image.load("sources/bg.jpg")
    screen.blit(background,(0,0))
    pygame.display.update()

    while True:
        test = manager.Manager()
        for i in range(0, len(test.problems_list[1])):
            # 分数显示
            textImage = myfont.render("Score: " + str(test.score), True, (0, 0, 255))
            screen.blit(background, (0, 0))
            screen.blit(textImage, (700, 80))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            broadcast.init(test.problems_list[1][i])  # 播放
            if i == 0 or i == len(test.problems_list[1]) - 1:
                continue
            else:
                start_time = time.time()
                times = []
                while time.time() - start_time <= 5:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_w:
                                times.append("w")
                                test.ispress_up()
                            if event.key == pygame.K_s:
                                times.append("s")
                                test.ispress_down()
                            if event.key == pygame.K_a:
                                times.append("a")
                                test.ispress_left()
                            if event.key == pygame.K_d:
                                times.append("d")
                                test.ispress_right()
                judge = test.check(i + 1, test.problems_list[0][i - 1], times)
                if judge is False:
                    test.score -= 10
                if test.score < 90:
                    break

        if test.score < 90:
            broadcast.init("考试结束")

        pygame.quit()

run_exam()
