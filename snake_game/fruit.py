import pygame
import random
from pygame.math import Vector2

class FRUIT:
    def __init__(self, cell_size, cell_number): 
        self.cell_size = cell_size # Tamanho da célula
        self.cell_number = cell_number # Número de células
        self.randomize() # Posicionar a fruta

    def draw_fruit(self, screen, apple): # Desenha a fruta na tela
        self.screen = screen
        self.apple = apple
        fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size) # Calcula a pos da fruta, coordenadas x e y
        screen.blit(apple, fruit_rect) # Desenha a imagem da fruta na pos calculada

    def randomize(self): # Gera novas frutas em locais aleátorios dentro do jogo
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)