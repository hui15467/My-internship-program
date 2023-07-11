import pygame


# import string
# import numpy
# import sys
# import xlrd
# import random
# from pygame.locals import *
# from openpyxl import Workbook
#
# from Annual_awards_main import pos_scan, winner, mode
def test():
    display_width = 1200
    display_height = 600
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    pygame.init()

    class Button(object):
        def __init__(self, text, color, heng=None, shu=None, **kwargs):
            self.surface = font1.render(text, True, color)

            self.WIDTH = self.surface.get_width()
            self.HEIGHT = self.surface.get_height()

            if 'centered_x' in kwargs and kwargs['centered_x']:
                self.heng = display_width // 2 - self.WIDTH // 2
            else:
                self.heng = heng
            if 'centered_y' in kwargs and kwargs['centered_y']:
                self.shu = display_height // 2 - self.HEIGHT // 2
            else:
                self.shu = shu

        def display(self):
            screen1.blit(self.surface, (self.heng, self.shu))

        def check_click(self, position):
            x_match = self.heng < position[0] < self.heng + self.WIDTH
            y_match = self.shu < position[1] < self.shu + self.HEIGHT
            if x_match and y_match:
                return True
            else:
                return False

    def starting_screen():
        pygame.init()
        screen1.blit(bg1, (0, 0))
        game_title = font1.render('Main Menu', True, WHITE)
        screen1.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))
        play_button = Button('Play', RED, None, 350, centered_x=True)
        exit_button = Button('Exit', WHITE, None, 400, centered_x=True)
        play_button.display()
        exit_button.display()
        pygame.display.update()

        while True:
            if play_button.check_click(pygame.mouse.get_pos()):
                play_button = Button('Play', RED, None, 350, centered_x=True)
            else:
                play_button = Button('Play', WHITE, None, 350, centered_x=True)
            if exit_button.check_click(pygame.mouse.get_pos()):
                exit_button = Button('Exit', RED, None, 400, centered_x=True)
            else:
                exit_button = Button('Exit', WHITE, None, 400, centered_x=True)
            play_button.display()
            exit_button.display()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen1.fill((250, 192, 203))
                pygame.display.flip()
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         pygame.display.update()
            #         raise SystemExit

            if pygame.mouse.get_pressed()[0]:
                if play_button.check_click(pygame.mouse.get_pos()):
                    # pygame.quit()
                    break
                if exit_button.check_click(pygame.mouse.get_pos()):
                    pygame.quit()
                    raise SystemExit

    # screen = pygame.display.set_mode((display_width, display_height))
    # bg1 = pygame.image.load(bg_location)
    #
    # font_addr = pygame.font.get_default_font()
    # font = pygame.font.Font(font_addr, 36)
    # font = pygame.font.Font("simhei.ttf", 36)
    screen1 = pygame.display.set_mode((display_width, display_height))
    bg1 = pygame.image.load("backup.jpg").convert_alpha()
    font_addr = pygame.font.get_default_font()
    font1 = pygame.font.Font(font_addr, 36)
    starting_screen()



