import pygame
import random
import sys
from pygame.math import Vector2
from snake import SNAKE
from fruit import FRUIT

class MAIN:
    def __init__(self, cell_size, cell_number): # Inicializa atributos necessários para o jogo
        self.cell_size = cell_size # Tamanho das células na grade do jogo
        self.cell_number = cell_number # Número de células na grade do jogo
        self.snake = SNAKE(cell_size) # Instância da classe snake
        self.fruit = FRUIT(cell_size, cell_number) # Instância da classe fruta

    def update(self, screen, game_font, cell_number, clock): # Atualiza o estado do jogo a cada frame
        self.snake.move_snake() # Atualiza a pos da cobra na direção que ela se move
        self.check_collision() # Verifica se a cobra colidiu com a fruta ou consigo mesma
        self.check_fail(screen, game_font, cell_number, clock) # Verifica se o jogo terminou --> cobra colidiu com uma parede ou consigo mesma

    def draw_elements(self, screen, apple, game_font): # Desenha os elementos principais do jogo na tela
        self.draw_grass(screen) # Cenário do jogo 
        self.fruit.draw_fruit(screen, apple) # Desenha a fruta do jogo 
        self.snake.draw_snake(screen) # Desenha a cobra na tela em sua pos atual
        self.draw_score(screen, game_font, apple) # Desenha a pontuação do jogador
        self.snake.draw_lives(screen) # Desenha as vidas da cobra

    def check_collision(self): # verificar colisão entre a cobra e a fruta
        if self.fruit.pos == self.snake.body[0]: # Verifica se a cabeça da cobra está na mesma pos que a fruta
            self.fruit.randomize() # Reposiciona a fruta aleatoriamente
            self.snake.add_block() # Add um novo bloco na cobra 
            self.snake.play_crunch_sound() # Executa o som quanto a cobra come a maça

        for block in self.snake.body[1:]: # Itera sobre os blocos do corpo da cobra, excluindo a cabeça
            if block == self.fruit.pos: # Se algum bloco estiver namesma pos que a fruta
                self.fruit.randomize() # Reposiciona a fruta aleatoriamente

    def check_fail(self, screen, game_font, cell_number, clock): # Verifica condições de falha --> game_over
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number: # Verifica se a cabeça da cobra está fora dos limites da tela
            self.snake.lives -= 1 # Reduz uma vida da cobra
            if self.snake.lives == 0: 
                self.game_over(screen, game_font, cell_number, clock) # Encerra o jogo
            else:
                self.snake.reset() # Reinicia na pos da cobra e continua o jogo

        for block in self.snake.body[1:]: 
            if block == self.snake.body[0]: # Se o bloco do corpo estiver na mesma pos que a cabeça da cobra
                self.snake.lives -= 1 # Reduz uma vida
                if self.snake.lives == 0:
                    self.game_over(screen, game_font, cell_number, clock) # Encerra o jogo

    def game_over(self, screen, game_font, cell_number, clock): # Indica que o jogo chegou ao fim quando as condições de falha são atendidas
        self.screen = screen
        self.game_font = game_font
        self.cell_number = cell_number
        self.clock = clock
        self.snake.lives = 3 # Garante que a cobra recomece com o número padrão de vidas
        self.snake.reset() # Reinicia na pos inicial da cobra
        self.game_over_screen(screen, game_font, clock) # Exibe a tela de game_over no jogo

    def draw_grass(self, screen): # Tela do jogo 
        grass_color = (167, 209, 61) # Cor da grama --> verde
        
        # Loop pelas linhas da Tela
        for row in range(self.cell_number): 
            if row % 2 == 0: # Se as linhas forem pares
                for col in range(self.cell_number): # Loog pelas colunas da Tela
                    if col % 2 == 0: # Se as colunas forem pares
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size) # Cria um retângulo para grama
                        pygame.draw.rect(screen, grass_color, grass_rect) # Desenha um retângulo com a cor da grama
            else:
                for col in range(self.cell_number): # Colunas da Tela
                    if col % 2 != 0: # Se for ímpar
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size) # Cria um retângulo para grama
                        pygame.draw.rect(screen, grass_color, grass_rect) # Desenha o retângulo com a cor da grama

    def draw_score(self, screen, game_font, apple): # Desenha a pontuação atual do jogador 
        score_text = str(len(self.snake.body) - 3) # Calcula a pontuação subtraindo o comp inicial da cobra
        score_surface = game_font.render(score_text, True, (56, 74, 12)) # Cria o texto de pontuação 
        score_x = int(self.cell_size * self.cell_number - 60) # pos x da pontuação na tela 
        score_y = int(self.cell_size * self.cell_number - 40) # pos y da pontuação na tela
        score_rect = score_surface.get_rect(center=(score_x, score_y)) # Retângulo de pontuação
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery)) # Obtém o retângulo que envolve a imagem da maçã
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height) # Maçã e superfície de pontuação

        pygame.draw.rect(screen, (167, 209, 61), bg_rect) # Retângulo de fundo com acor da grama
        screen.blit(score_surface, score_rect) # Superfície de pontuação na tela dentro do retângulo
        screen.blit(apple, apple_rect) # Desenha a imagem da maçã, dentro do retângulo
        pygame.draw.rect(screen, (167, 209, 61), bg_rect, 2) # Destaca o retângulo visualmente

    def game_over_screen(self, screen, game_font, clock): # Exibe a tela de game_over quando o jogo chega ao fim
        self.screen = screen
        self.game_font = game_font
        self.clock = clock
        while True: 
            for event in pygame.event.get(): # Itera sobre todos eventos capturados pelo pygame
                if event.type == pygame.QUIT: # # Se o evento for do tipo QUIT 
                    pygame.quit() # Pygame é encerrado
                    sys.exit() # Progama é finalizado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: # Verifica se a tecla pressionada é Enter
                        self.snake.reset() # Reinicia na pos da cobra
                        self.snake.lives = 3 # retorna o número padrão de vidas
                        return

            # Desenho da tela de game_over
            screen.fill((175, 215, 70))
            game_over_text = game_font.render("Game Over", True, (255, 255, 255))
            game_over_rect = game_over_text.get_rect(center=(self.cell_number * self.cell_size // 2, self.cell_number * self.cell_size // 2 - 50))
            screen.blit(game_over_text, game_over_rect)

            retry_text = game_font.render("Pressione Enter para reiniciar", True, (255, 255, 255))
            retry_rect = retry_text.get_rect(center=(self.cell_number * self.cell_size // 2, self.cell_number * self.cell_size // 2))
            screen.blit(retry_text, retry_rect)

            pygame.display.update() # Atualiza a tela para exibir mudanças feitas no loop
            clock.tick(60) # Limita a taxa de quadros por segundo a 60fps
