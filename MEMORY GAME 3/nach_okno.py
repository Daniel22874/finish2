import pygame
import sys
from main import FirstWindow
import random
from random import shuffle


def load_phrases_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        phrases = file.readlines()
        return [phrase.strip() for phrase in phrases]


class Snow(pygame.sprite.Sprite):
    def __init__(self, *group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/pngwing.com (1) (1).png').convert_alpha()
        self.rect = self.image.get_rect()


pygame.init()
x, y = 960, 600
Max_fps = 30
screen = pygame.display.set_mode((x, y))
pygame.display.set_icon(pygame.image.load('image/d5355674e573981ae597a29532009617.webp'))
pygame.display.set_caption("Memory game")
clock = pygame.time.Clock()
fonesound = pygame.mixer.Sound('image/Geometry Dash (256  kbps).mp3')
fonesound.set_volume(0.04)
fonesound.play(-1)


def main_menu():
    # создание кнопок
    first_button = FirstWindow(x / 2 - (252 / 2), 100, 252, 74, 'Играть', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    second_button = FirstWindow(x / 2 - (252 / 2), 200, 252, 74, 'Настройки', 'image/knopka.png', 'image/knopka2.png',
                                'image/сlick.mp3')
    trie_button = FirstWindow(x / 2 - (252 / 2), 400, 252, 74, 'Выход', 'image/knopka.png', 'image/knopka2.png',
                              'image/сlick.mp3')
    special_button = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, '52', 'image/4.png', 'image/104286.png',
                                 'image/52.mp3')
    running = True
    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render('Меню', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for i in [first_button, second_button, trie_button, special_button]:
                i.handle_event(event)
            if trie_button.clicked:
                pygame.quit()
                sys.exit()
            if second_button.clicked:
                fade()
                setting_menu()
            if first_button.clicked:
                fade()
                game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()

        for i in [first_button, second_button, trie_button, special_button]:
            i.check_hover(pygame.mouse.get_pos())

        for i in [first_button, second_button, trie_button, special_button]:
            i.draw(screen)
        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)
        pygame.display.flip()


def main_menu_night():
    # создание кнопок
    first_button = FirstWindow(x / 2 - (252 / 2), 100, 252, 74, 'Играть', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    second_button = FirstWindow(x / 2 - (252 / 2), 200, 252, 74, 'Настройки', 'image/knopka.png', 'image/knopka2.png',
                                'image/сlick.mp3')
    trie_button = FirstWindow(x / 2 - (252 / 2), 400, 252, 74, 'Выход', 'image/knopka.png', 'image/knopka2.png',
                              'image/сlick.mp3')
    special_button = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, '52', 'image/4.png', 'image/104286.png',
                                 'image/52.mp3')
    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render('Меню', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for i in [first_button, second_button, trie_button, special_button]:
                i.handle_event(event)
            if trie_button.clicked:
                pygame.quit()
                sys.exit()
            if second_button.clicked:
                fade()
                setting_menu_night()
            if first_button.clicked:
                fade()
                game_night()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()

        for i in [first_button, second_button, trie_button, special_button]:
            i.check_hover(pygame.mouse.get_pos())

        for i in [first_button, second_button, trie_button, special_button]:
            i.draw(screen)
        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)
        pygame.display.flip()


def setting_menu():
    audio_button = FirstWindow(x / 2 - (252 / 2), 150, 252, 74, 'Звук', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    fon_button = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, 'Тема', 'image/knopka.png', 'image/knopka2.png',
                             'image/сlick.mp3')

    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Здесь можно увеличить/уменьшить звук', True, (255, 255, 255))
        text_surface2 = font.render('А также сменить тему', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        text_rect2 = text_surface2.get_rect(center=(x / 2, 100))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            for i in [audio_button, fon_button]:
                i.handle_event(event)
            if fon_button.clicked:
                fade()
                daynight()
            if audio_button.clicked:
                fade()
                audset()

        for btn in [audio_button, fon_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)

        pygame.display.flip()


def setting_menu_night():
    audio_button = FirstWindow(x / 2 - (252 / 2), 150, 252, 74, 'Звук', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    fon_button = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, 'Тема', 'image/knopka.png', 'image/knopka2.png',
                             'image/сlick.mp3')

    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Здесь можно увеличить/уменьшить звук', True, (255, 255, 255))
        text_surface2 = font.render('А также сменить тему', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        text_rect2 = text_surface2.get_rect(center=(x / 2, 100))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu_night()
            for i in [audio_button, fon_button]:
                i.handle_event(event)
            if fon_button.clicked:
                fade()
                daynight_night()
            if audio_button.clicked:
                fade()
                audset_night()

        for btn in [audio_button, fon_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)

        pygame.display.flip()


def daynight():
    day_background = FirstWindow(x / 2 - (252 / 2), 150, 252, 74, 'Светлая тема', 'image/knopka.png',
                                 'image/knopka2.png',
                                 'image/сlick.mp3')
    night_background = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, 'Тёмная тема', 'image/knopka.png',
                                   'image/knopka2.png',
                                   'image/сlick.mp3')
    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Настройки темы', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            for i in [day_background, night_background]:
                i.handle_event(event)
            if day_background.clicked:
                main_menu()
            if night_background.clicked:
                main_menu_night()

        for btn in [day_background, night_background]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)
        pygame.display.flip()


def daynight_night():
    day_background = FirstWindow(x / 2 - (252 / 2), 150, 252, 74, 'Светлая тема', 'image/knopka.png',
                                 'image/knopka2.png',
                                 'image/сlick.mp3')
    night_background = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, 'Тёмная тема', 'image/knopka.png',
                                   'image/knopka2.png',
                                   'image/сlick.mp3')
    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Настройки темы', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu_night()
            for i in [day_background, night_background]:
                i.handle_event(event)
            if day_background.clicked:
                fade()
                main_menu()
            if night_background.clicked:
                fade()
                main_menu_night()
        for btn in [day_background, night_background]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)

        pygame.display.flip()


def audset():
    on_music = FirstWindow(x / 2 - (252 / 2), 150, 252, 74, 'Включить звук', 'image/knopka.png', 'image/knopka2.png',
                           'image/сlick.mp3')
    off_music = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, 'Отключить звук', 'image/knopka.png', 'image/knopka2.png',
                            'image/сlick.mp3')
    volume_music = FirstWindow(x / 2 - (252 / 2), 450, 252, 74, 'Громкость звука', 'image/knopka.png',
                               'image/knopka2.png',
                               'image/сlick.mp3')
    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Настройки звука', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            for i in [on_music, off_music, volume_music]:
                i.handle_event(event)
            if on_music.clicked:
                fonesound.play(-1)
            if off_music.clicked:
                fonesound.stop()
            if volume_music.clicked:
                fade()
                volume_menu()
        for btn in [on_music, off_music, volume_music]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)

        pygame.display.flip()


def audset_night():
    on_music = FirstWindow(x / 2 - (252 / 2), 150, 252, 74, 'Включить звук', 'image/knopka.png', 'image/knopka2.png',
                           'image/сlick.mp3')
    off_music = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, 'Отключить звук', 'image/knopka.png', 'image/knopka2.png',
                            'image/сlick.mp3')
    volume_music = FirstWindow(x / 2 - (252 / 2), 450, 252, 74, 'Громкость звука', 'image/knopka.png',
                               'image/knopka2.png',
                               'image/сlick.mp3')
    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Настройки звука', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu_night()
            for i in [on_music, off_music, volume_music]:
                i.handle_event(event)
            if on_music.clicked:
                fonesound.play(-1)
            if off_music.clicked:
                fonesound.stop()
            if volume_music.clicked:
                fade()
                volume_menu_night()
        for btn in [on_music, off_music, volume_music]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)

        pygame.display.flip()


def volume_menu():
    z_two = FirstWindow(x / 2 - (252 / 2), 100, 252, 74, '20 %', 'image/knopka.png', 'image/knopka2.png',
                        'image/сlick.mp3')
    z_four = FirstWindow(x / 2 - (252 / 2), 200, 252, 74, '40 %', 'image/knopka.png', 'image/knopka2.png',
                         'image/сlick.mp3')
    z_six = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, '60 %', 'image/knopka.png', 'image/knopka2.png',
                        'image/сlick.mp3')
    z_eight = FirstWindow(x / 2 - (252 / 2), 400, 252, 74, '80 %', 'image/knopka.png', 'image/knopka2.png',
                          'image/сlick.mp3')
    z_ten = FirstWindow(x / 2 - (252 / 2), 500, 252, 74, '100 %', 'image/knopka.png', 'image/knopka2.png',
                        'image/сlick.mp3')
    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Громкость звука', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            for i in [z_two, z_four, z_six, z_eight, z_ten]:
                i.handle_event(event)
            if z_two.clicked:
                fonesound.set_volume(0.02)
            if z_four.clicked:
                fonesound.set_volume(0.04)
            if z_six.clicked:
                fonesound.set_volume(0.06)
            if z_eight.clicked:
                fonesound.set_volume(0.08)
            if z_ten.clicked:
                fonesound.set_volume(0.1)
        for btn in [z_two, z_four, z_six, z_eight, z_ten]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)

        pygame.display.flip()


def volume_menu_night():
    z_two = FirstWindow(x / 2 - (252 / 2), 100, 252, 74, '20 %', 'image/knopka.png', 'image/knopka2.png',
                        'image/сlick.mp3')
    z_four = FirstWindow(x / 2 - (252 / 2), 200, 252, 74, '40 %', 'image/knopka.png', 'image/knopka2.png',
                         'image/сlick.mp3')
    z_six = FirstWindow(x / 2 - (252 / 2), 300, 252, 74, '60 %', 'image/knopka.png', 'image/knopka2.png',
                        'image/сlick.mp3')
    z_eight = FirstWindow(x / 2 - (252 / 2), 400, 252, 74, '80 %', 'image/knopka.png', 'image/knopka2.png',
                          'image/сlick.mp3')
    z_ten = FirstWindow(x / 2 - (252 / 2), 500, 252, 74, '100 %', 'image/knopka.png', 'image/knopka2.png',
                        'image/сlick.mp3')
    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Громкость звука', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu_night()
            for i in [z_two, z_four, z_six, z_eight, z_ten]:
                i.handle_event(event)
            if z_two.clicked:
                fonesound.set_volume(0.02)
            if z_four.clicked:
                fonesound.set_volume(0.04)
            if z_six.clicked:
                fonesound.set_volume(0.06)
            if z_eight.clicked:
                fonesound.set_volume(0.08)
            if z_ten.clicked:
                fonesound.set_volume(0.1)
        for btn in [z_two, z_four, z_six, z_eight, z_ten]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)

        pygame.display.flip()


def game():
    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'Продолжить', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    running = True
    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100

    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
        font = pygame.font.Font(None, 50)
        text_surface = font.render('Игра заключается в том, что нужно угадать',
                                   True, (255, 255, 255))
        text_surface2 = font.render('пары кружочков. Угадывайте по максимуму.', True, (255, 255, 255))
        text_surface3 = font.render('В конце игры будут ваши результаты. Удачи!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        text_rect2 = text_surface2.get_rect(center=(x / 2, 120))
        text_rect3 = text_surface3.get_rect(center=(x / 2, 170))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)
        screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            for i in [first_button]:
                i.handle_event(event)
            if first_button.clicked:
                fade()
                lvl1_game_start()
        for btn in [first_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)
        pygame.display.flip()
        clock.tick(Max_fps)


rezultati = []
with open("first_lvl_res.txt", "r") as file:
    max_result1 = max(int(line) for line in file)
    rezultati.append(max_result1)

with open("second_lvl_res.txt", "r") as file:
    lines = (line.strip() for line in file)
    max_result2 = max(int(line) for line in lines if line)
    rezultati.append(max_result2)

with open("third_lvl_res.txt", "r") as file:
    max_result3 = max(int(line) for line in file)
    rezultati.append(max_result3)



def lvl1_game_start_night():
    pygame.init()
    x = 960
    y = 600
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Memory game")
    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'Продолжить', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
    green = (0, 255, 0)
    ne_black = (100, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    grey = (128, 128, 128)

    # формируем список цветов
    circle_radius = 50
    circle_colors = [red, blue, green, yellow]
    circle_pairs = circle_colors * 2
    # перемешивает функция
    shuffle(circle_pairs)

    # формируем список окружностей
    circle_positions = []
    for i in range(len(circle_colors)):
        for j in range(2):
            center_x = ((x / 4) * (i + 1)) - (x / 8)
            center_y = ((y / 3) * (j + 1)) - (y / 6)
            circle_positions.append([center_x, center_y])

    # запоминаем позиции и цвета окружностей в конечном списке
    konech_circle_positions = circle_positions.copy()
    konech_circle_colors = circle_pairs.copy()

    # рисуем цветные окружности
    for i in range(len(circle_pairs)):
        position = circle_positions[i]
        color = circle_pairs[i]
        pygame.draw.circle(screen, color, position, circle_radius)

    text_title = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.update()

    pygame.time.wait(3500)
    file = open("first_lvl_res.txt", "a")
    # закрываем цветные окружности серыми
    for i in range(len(circle_pairs)):
        pygame.draw.circle(screen, grey, konech_circle_positions[i], circle_radius)

    pygame.display.update()
    uncovered_circles = []
    last_uncovered_circle = None
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in range(len(konech_circle_positions)):
                    position = konech_circle_positions[i]
                    if ((position[0] - mouse_pos[0]) ** 2 + (position[1] - mouse_pos[1]) ** 2) ** 0.5 < circle_radius:
                        if i not in uncovered_circles:
                            uncovered_circles.append(i)
                            color = circle_pairs[i]
                            pygame.draw.circle(screen, color, position, circle_radius)
                            pygame.display.update()
                            if last_uncovered_circle is not None and konech_circle_colors[last_uncovered_circle] == \
                                    konech_circle_colors[i]:
                                score += 1
                            last_uncovered_circle = i

                if len(uncovered_circles) == len(circle_pairs):
                    final_score_text = text_title.render(f"Уровень памяти: {str(score)} из 4", True, white)
                    rezultati.append(score)
                    file.write(str(score) + '\n')
                    final_max_score_text = text_title.render(f"Максимальный результат: {max_result1}", True, white)
                    screen.blit(final_max_score_text, (x // 2, y // 2 + 160))
                    screen.blit(final_score_text, (x // 2, y // 2 + 125))
            for i in [first_button]:
                i.handle_event(event)
            if first_button.clicked:
                fade()
                lvl2_game_start_night()
            for i in [first_button]:
                i.check_hover(pygame.mouse.get_pos())
                i.draw(screen)
        pygame.display.flip()


def lvl2_game_start_night():
    pygame.init()
    x = 960
    y = 600
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Memory game")
    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'Продолжить', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
    green = (0, 255, 0)
    ne_black = (100, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    grey = (128, 128, 128)

    file = open("second_lvl_res.txt", "a")
    # формируем список цветов
    circle_radius = 50
    circle_colors = [red, blue, green, yellow, purple, white]
    circle_pairs = circle_colors * 2
    # перемешивает функция
    shuffle(circle_pairs)

    # формируем список окружностей
    circle_positions = []
    for i in range(len(circle_colors)):
        for j in range(2):
            center_x = ((x / 6) * (i + 1)) - (x / 12)
            center_y = ((y / 3) * (j + 1)) - (y / 6)
            circle_positions.append([center_x, center_y])

    # запоминаем позиции и цвета окружностей в конечном списке
    konech_circle_positions = circle_positions.copy()
    konech_circle_colors = circle_pairs.copy()

    # рисуем цветные окружности
    for i in range(len(circle_pairs)):
        position = circle_positions[i]
        color = circle_pairs[i]
        pygame.draw.circle(screen, color, position, circle_radius)

    text_title = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.update()

    pygame.time.wait(3500)

    # закрываем цветные окружности серыми
    for i in range(len(circle_pairs)):
        pygame.draw.circle(screen, grey, konech_circle_positions[i], circle_radius)

    pygame.display.update()
    uncovered_circles = []
    last_uncovered_circle = None
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in range(len(konech_circle_positions)):
                    position = konech_circle_positions[i]
                    if ((position[0] - mouse_pos[0]) ** 2 + (position[1] - mouse_pos[1]) ** 2) ** 0.5 < circle_radius:
                        if i not in uncovered_circles:
                            uncovered_circles.append(i)
                            color = circle_pairs[i]
                            pygame.draw.circle(screen, color, position, circle_radius)
                            pygame.display.update()
                            if last_uncovered_circle is not None and konech_circle_colors[last_uncovered_circle] == \
                                    konech_circle_colors[i]:
                                score += 1
                            last_uncovered_circle = i

                if len(uncovered_circles) == len(circle_pairs):
                    # вывод результата
                    final_score_text = text_title.render(f"Уровень памяти: {str(score)} из 6", True, white)
                    screen.blit(final_score_text, (x // 2, y // 2 + 125))
                    rezultati.append(score)
                    file.write(str(score)  + '\n')
                    final_max_score_text = text_title.render(f"Максимальный результат: {max_result2}", True, white)
                    screen.blit(final_max_score_text, (x // 2, y // 2 + 160))

            for i in [first_button]:
                i.handle_event(event)
            if first_button.clicked:
                fade()
                lvl3_game_start_night()
            for i in [first_button]:
                i.check_hover(pygame.mouse.get_pos())
                i.draw(screen)
            pygame.display.update()
            pygame.display.flip()


def lvl3_game_start_night():
    pygame.init()
    x = 960
    y = 600
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Memory game")

    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'Результаты', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
    green = (0, 255, 0)
    ne_black = (100, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    grey = (128, 128, 128)
    orange = (255, 165, 0)
    pink = (255, 192, 203)

    file = open('third_lvl_res.txt', 'a')
    # формируем список цветов
    circle_radius = 50
    circle_colors = [red, blue, green, yellow, white, purple, orange, pink]
    circle_pairs = circle_colors * 2
    # перемешивает функция
    shuffle(circle_pairs)

    # формируем список окружностей
    circle_positions = []
    for i in range(len(circle_colors)):
        for j in range(2):
            center_x = ((x / 8) * (i + 1)) - (x / 16)
            center_y = ((y / 3) * (j + 1)) - (y / 6)
            circle_positions.append([center_x, center_y])

    # запоминаем позиции и цвета окружностей в конечном списке
    konech_circle_positions = circle_positions.copy()
    konech_circle_colors = circle_pairs.copy()

    # рисуем цветные окружности
    for i in range(len(circle_pairs)):
        position = circle_positions[i]
        color = circle_pairs[i]
        pygame.draw.circle(screen, color, position, circle_radius)

    text_title = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.update()

    pygame.time.wait(3500)

    # закрываем цветные окружности серыми
    for i in range(len(circle_pairs)):
        pygame.draw.circle(screen, grey, konech_circle_positions[i], circle_radius)

    pygame.display.update()
    uncovered_circles = []
    last_uncovered_circle = None
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in range(len(konech_circle_positions)):
                    position = konech_circle_positions[i]
                    if ((position[0] - mouse_pos[0]) ** 2 + (position[1] - mouse_pos[1]) ** 2) ** 0.5 < circle_radius:
                        if i not in uncovered_circles:
                            uncovered_circles.append(i)
                            color = circle_pairs[i]
                            pygame.draw.circle(screen, color, position, circle_radius)
                            pygame.display.update()
                            if last_uncovered_circle is not None and konech_circle_colors[last_uncovered_circle] == \
                                    konech_circle_colors[i]:
                                score += 1
                            last_uncovered_circle = i

                if len(uncovered_circles) == len(circle_pairs):
                    # вывод результата
                    final_score_text = text_title.render(f"Уровень памяти: {str(score)} из 8", True, white)
                    screen.blit(final_score_text, (x // 2, y // 2 + 125))
                    rezultati.append(score)
                    file.write(str(score)  + '\n')
                    final_max_score_text = text_title.render(f"Максимальный результат: {max_result3}", True, white)
                    screen.blit(final_max_score_text, (x // 2, y // 2 + 160))
            for i in [first_button]:
                i.handle_event(event)
            for i in [first_button]:
                i.check_hover(pygame.mouse.get_pos())
                i.draw(screen)
            if first_button.clicked:
                fade()
                rezult_night()
            pygame.display.update()
            pygame.display.flip()


def rezult_night():
    pygame.init()
    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'В главное меню', 'image/knopka.png',
                               'image/knopka2.png',
                               'image/сlick.mp3')
    screen = pygame.display.set_mode((960, 600))  # Создание окна
    pygame.display.set_caption("Memory game")
    screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))
    slova = load_phrases_from_file('data.txt')
    if sum(rezultati) > 15:
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = slova[0]
        text2 = slova[1]
        text_surface = font.render(text, True, (255, 255, 255))
        text_surface2 = font.render(text2, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        text_rect2 = text_surface2.get_rect(center=(400, 350))
    elif sum(rezultati) > 12:
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = slova[2]
        text2 = slova[3]
        text_surface = font.render(text, True, (255, 255, 255))
        text_surface2 = font.render(text2, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        text_rect2 = text_surface2.get_rect(center=(400, 350))
    else:
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = slova[-2]
        text2 = slova[-1]
        text_surface = font.render(text, True, (255, 255, 255))
        text_surface2 = font.render(text2, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        text_rect2 = text_surface2.get_rect(center=(450, 350))
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for i in [first_button]:
                i.handle_event(event)
            for i in [first_button]:
                i.check_hover(pygame.mouse.get_pos())
                i.draw(screen)
            if first_button.clicked:
                fade()
                main_menu_night()
        pygame.display.update()
        pygame.display.flip()


def game_night():
    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'Продолжить', 'image/knopka.png',
                               'image/knopka2.png',
                               'image/сlick.mp3')
    running = True

    s1 = Snow()
    s2 = Snow()
    s3 = Snow()
    s4 = Snow()
    s5 = Snow()
    s6 = Snow()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    x1 = random.randrange(20, 800)
    x2 = random.randrange(20, 800)
    x3 = random.randrange(20, 800)
    x4 = random.randrange(20, 800)
    x5 = random.randrange(20, 800)
    x6 = random.randrange(20, 800)
    v1 = 100
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('image/msg772488480-12525 (1).png'), (0, 0))

        font = pygame.font.Font(None, 50)
        text_surface = font.render('Игра заключается в том, что нужно угадать',
                                   True, (255, 255, 255))
        text_surface2 = font.render('пары кружочков. Угадывайте по максимуму.', True, (255, 255, 255))
        text_surface3 = font.render('В конце игры будут ваши результаты. Удачи!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x / 2, 70))
        text_rect2 = text_surface2.get_rect(center=(x / 2, 120))
        text_rect3 = text_surface3.get_rect(center=(x / 2, 170))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)
        screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            for i in [first_button]:
                i.handle_event(event)
            if first_button.clicked:
                fade()
                lvl1_game_start_night()
        for i in [first_button]:
            i.check_hover(pygame.mouse.get_pos())
            i.draw(screen)

        screen.blit(s1.image, (x1, c1))
        c1 += v1 * clock.tick() / 1000
        screen.blit(s2.image, (x2, c2))
        # c2 += v2 * clock.tick() / 1000
        c2 = c1
        screen.blit(s3.image, (x3, c3))
        # c3 += v3 * clock.tick() / 1000
        c3 = c2
        screen.blit(s4.image, (x4, c4))
        c4 = c3
        screen.blit(s5.image, (x5, c5))
        c5 = c4
        screen.blit(s6.image, (x6, c6))
        c6 = c5
        if c1 > 490:
            c1 = 0
            x1 = random.randrange(20, 800)
        if c2 > 490:
            c2 = 0
            x2 = random.randrange(20, 800)
        if c3 > 490:
            c3 = 0
            x3 = random.randrange(20, 800)
        if c4 > 490:
            c4 = 0
            x4 = random.randrange(20, 800)
        if c5 > 490:
            c5 = 0
            x5 = random.randrange(20, 800)
        if c6 > 490:
            c6 = 0
            x6 = random.randrange(20, 800)
        pygame.display.flip()
        clock.tick(Max_fps)


def lvl1_game_start():
    pygame.init()
    x = 960
    y = 600
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Memory game")
    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'Продолжить', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
    green = (0, 255, 0)
    ne_black = (100, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    grey = (128, 128, 128)

    file = open('first_lvl_res.txt', 'a')
    # формируем список цветов
    circle_radius = 50
    circle_colors = [red, blue, green, yellow]
    circle_pairs = circle_colors * 2
    # перемешивает функция
    shuffle(circle_pairs)

    # формируем список окружностей
    circle_positions = []
    for i in range(len(circle_colors)):
        for j in range(2):
            center_x = ((x / 4) * (i + 1)) - (x / 8)
            center_y = ((y / 3) * (j + 1)) - (y / 6)
            circle_positions.append([center_x, center_y])

    # запоминаем позиции и цвета окружностей в конечном списке
    konech_circle_positions = circle_positions.copy()
    konech_circle_colors = circle_pairs.copy()

    # рисуем цветные окружности
    for i in range(len(circle_pairs)):
        position = circle_positions[i]
        color = circle_pairs[i]
        pygame.draw.circle(screen, color, position, circle_radius)

    text_title = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.update()

    pygame.time.wait(3500)

    # закрываем цветные окружности серыми
    for i in range(len(circle_pairs)):
        pygame.draw.circle(screen, grey, konech_circle_positions[i], circle_radius)

    pygame.display.update()
    uncovered_circles = []
    last_uncovered_circle = None
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in range(len(konech_circle_positions)):
                    position = konech_circle_positions[i]
                    if ((position[0] - mouse_pos[0]) ** 2 + (position[1] - mouse_pos[1]) ** 2) ** 0.5 < circle_radius:
                        if i not in uncovered_circles:
                            uncovered_circles.append(i)
                            color = circle_pairs[i]
                            pygame.draw.circle(screen, color, position, circle_radius)
                            pygame.display.update()
                            if last_uncovered_circle is not None and konech_circle_colors[last_uncovered_circle] == \
                                    konech_circle_colors[i]:
                                score += 1
                            last_uncovered_circle = i

                if len(uncovered_circles) == len(circle_pairs):
                    # вывод результата
                    final_score_text = text_title.render(f"Уровень памяти: {str(score)} из 4", True, white)
                    rezultati.append(score)
                    file.write(str(score)  + '\n')
                    final_max_score_text = text_title.render(f"Максимальный результат: {max_result1}", True, white)
                    screen.blit(final_max_score_text, (x // 2, y // 2 + 160))
                    screen.blit(final_score_text, (x // 2, y // 2 + 125))
            for i in [first_button]:
                i.handle_event(event)
            if first_button.clicked:
                fade()
                lvl2_game_start()
            for i in [first_button]:
                i.check_hover(pygame.mouse.get_pos())
                i.draw(screen)
            pygame.display.update()
        pygame.display.flip()


def lvl2_game_start():
    pygame.init()
    x = 960
    y = 600
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Memory game")
    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'Продолжить', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
    green = (0, 255, 0)
    ne_black = (100, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    grey = (128, 128, 128)

    file = open('second_lvl_res.txt', 'a')
    # формируем список цветов
    circle_radius = 50
    circle_colors = [red, blue, green, yellow, purple, white]
    circle_pairs = circle_colors * 2
    # перемешивает функция
    shuffle(circle_pairs)

    # формируем список окружностей
    circle_positions = []
    for i in range(len(circle_colors)):
        for j in range(2):
            center_x = ((x / 6) * (i + 1)) - (x / 12)
            center_y = ((y / 3) * (j + 1)) - (y / 6)
            circle_positions.append([center_x, center_y])

    # запоминаем позиции и цвета окружностей в конечном списке
    konech_circle_positions = circle_positions.copy()
    konech_circle_colors = circle_pairs.copy()

    # рисуем цветные окружности
    for i in range(len(circle_pairs)):
        position = circle_positions[i]
        color = circle_pairs[i]
        pygame.draw.circle(screen, color, position, circle_radius)

    text_title = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.update()

    pygame.time.wait(3500)

    # закрываем цветные окружности серыми
    for i in range(len(circle_pairs)):
        pygame.draw.circle(screen, grey, konech_circle_positions[i], circle_radius)

    pygame.display.update()
    uncovered_circles = []
    last_uncovered_circle = None
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in range(len(konech_circle_positions)):
                    position = konech_circle_positions[i]
                    if ((position[0] - mouse_pos[0]) ** 2 + (position[1] - mouse_pos[1]) ** 2) ** 0.5 < circle_radius:
                        if i not in uncovered_circles:
                            uncovered_circles.append(i)
                            color = circle_pairs[i]
                            pygame.draw.circle(screen, color, position, circle_radius)
                            pygame.display.update()
                            if last_uncovered_circle is not None and konech_circle_colors[last_uncovered_circle] == \
                                    konech_circle_colors[i]:
                                score += 1
                            last_uncovered_circle = i

                if len(uncovered_circles) == len(circle_pairs):
                    # вывод результата
                    final_score_text = text_title.render(f"Уровень памяти: {str(score)} из 6", True, white)
                    screen.blit(final_score_text, (x // 2, y // 2 + 125))
                    rezultati.append(score)
                    file.write(str(score)  + '\n')
                    final_max_score_text = text_title.render(f"Максимальный результат: {max_result2}", True, white)
                    screen.blit(final_max_score_text, (x // 2, y // 2 + 160))

            for i in [first_button]:
                i.handle_event(event)
            if first_button.clicked:
                fade()
                lvl3_game_start()
            for i in [first_button]:
                i.check_hover(pygame.mouse.get_pos())
                i.draw(screen)
            pygame.display.update()
            pygame.display.flip()


def lvl3_game_start():
    pygame.init()
    x = 960
    y = 600
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Memory game")

    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'Результаты', 'image/knopka.png', 'image/knopka2.png',
                               'image/сlick.mp3')
    screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
    green = (0, 255, 0)
    ne_black = (100, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    grey = (128, 128, 128)
    orange = (255, 165, 0)
    pink = (255, 192, 203)

    file = open('third_lvl_res.txt', 'a')
    # формируем список цветов
    circle_radius = 50
    circle_colors = [red, blue, green, yellow, white, purple, orange, pink]
    circle_pairs = circle_colors * 2
    # перемешивает функция
    shuffle(circle_pairs)

    # формируем список окружностей
    circle_positions = []
    for i in range(len(circle_colors)):
        for j in range(2):
            center_x = ((x / 8) * (i + 1)) - (x / 16)
            center_y = ((y / 3) * (j + 1)) - (y / 6)
            circle_positions.append([center_x, center_y])

    # запоминаем позиции и цвета окружностей в конечном списке
    konech_circle_positions = circle_positions.copy()
    konech_circle_colors = circle_pairs.copy()

    # рисуем цветные окружности
    for i in range(len(circle_pairs)):
        position = circle_positions[i]
        color = circle_pairs[i]
        pygame.draw.circle(screen, color, position, circle_radius)

    text_title = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.update()

    pygame.time.wait(3500)

    # закрываем цветные окружности серыми
    for i in range(len(circle_pairs)):
        pygame.draw.circle(screen, grey, konech_circle_positions[i], circle_radius)

    pygame.display.update()
    uncovered_circles = []
    last_uncovered_circle = None
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in range(len(konech_circle_positions)):
                    position = konech_circle_positions[i]
                    if ((position[0] - mouse_pos[0]) ** 2 + (position[1] - mouse_pos[1]) ** 2) ** 0.5 < circle_radius:
                        if i not in uncovered_circles:
                            uncovered_circles.append(i)
                            color = circle_pairs[i]
                            pygame.draw.circle(screen, color, position, circle_radius)
                            pygame.display.update()
                            if last_uncovered_circle is not None and konech_circle_colors[last_uncovered_circle] == \
                                    konech_circle_colors[i]:
                                score += 1
                            last_uncovered_circle = i

                if len(uncovered_circles) == len(circle_pairs):
                    # вывод результата
                    final_score_text = text_title.render(f"Уровень памяти: {str(score)} из 8", True, white)
                    screen.blit(final_score_text, (x // 2, y // 2 + 125))
                    rezultati.append(score)
                    file.write(str(score) + '\n')
                    final_max_score_text = text_title.render(f"Максимальный результат: {max_result3}", True, white)
                    screen.blit(final_max_score_text, (x // 2, y // 2 + 160))
            for i in [first_button]:
                i.handle_event(event)
            for i in [first_button]:
                i.check_hover(pygame.mouse.get_pos())
                i.draw(screen)
            if first_button.clicked:
                fade()
                rezult()
            pygame.display.update()
            pygame.display.flip()


def rezult():
    pygame.init()
    first_button = FirstWindow(x - (252 / 2 + 150), 500, 252, 74, 'В главное меню', 'image/knopka.png',
                               'image/knopka2.png',
                               'image/сlick.mp3')
    screen = pygame.display.set_mode((960, 600))  # Создание окна
    pygame.display.set_caption("Memory game")
    screen.blit(pygame.image.load('image/7baf29caafdc11ee9b01d6f07e64960d.png'), (0, 0))
    slova = load_phrases_from_file('data.txt')
    if sum(rezultati) > 15:
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = slova[0]
        text2 = slova[1]
        text_surface = font.render(text, True, (255, 255, 255))
        text_surface2 = font.render(text2, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        text_rect2 = text_surface2.get_rect(center=(400, 350))
    elif sum(rezultati) > 12:
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = slova[2]
        text2 = slova[3]
        text_surface = font.render(text, True, (255, 255, 255))
        text_surface2 = font.render(text2, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        text_rect2 = text_surface2.get_rect(center=(400, 350))
    else:
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = slova[-1]
        text2 = slova[-2]
        text_surface = font.render(text, True, (255, 255, 255))
        text_surface2 = font.render(text2, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        text_rect2 = text_surface2.get_rect(center=(450, 350))
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for i in [first_button]:
                i.handle_event(event)
            for i in [first_button]:
                i.check_hover(pygame.mouse.get_pos())
                i.draw(screen)
            if first_button.clicked:
                fade()
                main_menu()
        pygame.display.update()
        pygame.display.flip()


def fade():
    running = True
    fade_alpha = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((x, y))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False
        pygame.display.flip()
        pygame.time.delay(Max_fps)


main_menu()
