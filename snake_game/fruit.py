import pygame
import random
from pygame.math import Vector2

class FRUIT:
    def __init__(self, cell_size, cell_number, screen):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen
        self.randomize()
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size)
        self.screen.blit(pygame.image.load('snake_game/gráficos/apple.png').convert_alpha(), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)
