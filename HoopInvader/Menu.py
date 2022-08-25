import pygame
class menu():
    def __init__(self):
        self.run_display =True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100

    def draw_cursor(self):
        