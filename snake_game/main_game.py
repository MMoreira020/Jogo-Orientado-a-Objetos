from snake import SNAKE
from snake import MAIN
import pygame

class MAIN:
    def __init__(self, cell_size, cell_number, screen, apple, heart, game_font):
        self.snake = SNAKE(cell_size)  # Passando cell_size para o construtor de SNAKE
        self.main = MAIN(cell_size)
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen
        self.apple = apple
        self.heart = heart  # Adicione a imagem do coração
        self.game_font = game_font
        self.lives = 3  # Adicione uma variável para armazenar as vidas
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake(self.screen)
        self.draw_score()
        self.draw_lives()
        
    def check_collision(self):
        # Adicione sua lógica de colisão aqui, se necessário
        pass
        
    def check_fail(self):
        # Adicione sua lógica de falha aqui, se necessário
        pass
    
    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * self.cell_size,row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen,grass_color, grass_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text,True,(56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = self.apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)
        
        pygame.draw.rect(self.screen,(167, 209, 61), bg_rect)
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.apple, apple_rect)
        pygame.draw.rect(self.screen,(167, 209, 61),bg_rect, 2)
        
    def draw_lives(self):
        for i in range(self.lives):
            heart_x = 10 + i * (self.heart.get_width() + 10)  # Espaçamento entre corações
            heart_y = 10
            self.screen.blit(self.heart, (heart_x, heart_y))
