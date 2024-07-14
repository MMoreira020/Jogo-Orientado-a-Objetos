import pygame
from pygame.math import Vector2

class SNAKE: # Gerencia a cobra no jogo
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)] # Corpo inicial da cobra
        self.direction = Vector2(1, 0) # Direção inicial da cobra --> direita
        self.new_block = False # Indica se uma nova parte do corpo deve ser adicionada
        self.lives = 3 # Vidas iniciais

        # Imagens da cabeça da cobra
        self.head_up = pygame.image.load('snake_game/gráficos/head_up.png').convert_alpha() # Para cima
        self.head_down = pygame.image.load('snake_game/gráficos/head_down.png').convert_alpha() # Para baixo
        self.head_right = pygame.image.load('snake_game/gráficos/head_right.png').convert_alpha() # Para direita
        self.head_left = pygame.image.load('snake_game/gráficos/head_left.png').convert_alpha() # Para esquerda
        
        # Imagens da cauda da cobra
        self.tail_up = pygame.image.load('snake_game/gráficos/tail_up.png').convert_alpha() # Para cima
        self.tail_down = pygame.image.load('snake_game/gráficos/tail_down.png').convert_alpha() # Para baixo
        self.tail_right = pygame.image.load('snake_game/gráficos/tail_right.png').convert_alpha() # Para direita
        self.tail_left = pygame.image.load('snake_game/gráficos/tail_left.png').convert_alpha() # Para esquerda

        # Imagens do corpo da cobra 
        self.body_vertical = pygame.image.load('snake_game/gráficos/body_vertical.png').convert_alpha() # Corpo vertical
        self.body_horizontal = pygame.image.load('snake_game/gráficos/body_horizontal.png').convert_alpha() # Corpo horizontal
        
        self.body_tr = pygame.image.load('snake_game/gráficos/body_topright.png').convert_alpha() # Superior direito
        self.body_tl = pygame.image.load('snake_game/gráficos/body_topleft.png').convert_alpha() # Superior esquerdo
        self.body_br = pygame.image.load('snake_game/gráficos/body_bottomright.png').convert_alpha() # Inferior direito
        self.body_bl = pygame.image.load('snake_game/gráficos/body_bottomleft.png').convert_alpha() # Inferior esquerdo

        self.crunch_sound = pygame.mixer.Sound('snake_game/som/plastic-crunch-83779.mp3') # Som da maçã

    def draw_snake(self, screen): # Desenha a cobra na tela
        self.screen = screen
        self.update_head_graphics() # Atualiza a cabeça da cobra
        self.update_tail_graphics() # Atualiza a cauda da cobra

        for index, block in enumerate(self.body): # Itera sobre cada bloco do corpo da cobra
            x_pos = int(block.x * self.cell_size) # Bloco atual * tam da célula
            y_pos = int(block.y * self.cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size) # define um retângulo que representa a pos e o tam do bloco

            if index == 0: 
                screen.blit(self.head, block_rect) # Desenha a imagem da cabeã na pos block_rect
            elif index == len(self.body) - 1: # Se for o ultimo bloco da cobra
                screen.blit(self.tail, block_rect) # Desenha a imagem da cauda 
            else:
                previous_block = self.body[index + 1] - block # Diferença entre o bloco atual e o anterior
                next_block = self.body[index - 1] - block # Diferença entre o bloco atual e o seguinte
                if previous_block.x == next_block.x: # Verifica se os blocos estão na col vertical
                    screen.blit(self.body_vertical, block_rect) # Desenha
                elif previous_block.y == next_block.y: # Verifica se os blocos estão na linha horizontal
                    screen.blit(self.body_horizontal, block_rect) # Desenha 
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: # Curva superior a esquerda
                        screen.blit(self.body_tl, block_rect) # Desenha
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: # Curva superior a direita
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1: # Curva Inferior a esquerda
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1: # Curva inferior a direita
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self): # Atualiza a imagem da cabeça da cobra 
        head_relation = self.body[1] - self.body[0] # Pos atual da cabeça da cobra
        if head_relation == Vector2(1, 0): # A cobra está indo para direita
            self.head = self.head_left # Imagem da cabeça virada para esquerda 
        elif head_relation == Vector2(-1, 0): # A cobra está indo para esquerda
            self.head = self.head_right # Imagem da cabeça virada para direita
        elif head_relation == Vector2(0, 1): # A cobra está indo para cima
            self.head = self.head_up 
        elif head_relation == Vector2(0, -1): # A cobra está indo para baixo
            self.head = self.head_down

    def update_tail_graphics(self): # Atualiza a imagem da cauda da cobra
        tail_relation = self.body[-2] - self.body[-1] # Pos atual da cauda - pos anterios à cauda
        if tail_relation == Vector2(1, 0): 
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): 
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): 
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): 
            self.tail = self.tail_down

    def move_snake(self): # Mover a cobra
        if self.new_block == True: # Verifica se a cobra deve crescer
            body_copy = self.body[:] # Cria uma cópia da lista self_body
            body_copy.insert(0, body_copy[0] + self.direction) # Insere um novo bloco no corpo da cobra
            self.body = body_copy[:] # Atualiza o atributo self.body com a cópia modificada
            self.new_block = False # reseta a flag, indicando que a cobra não está mais em processo de crescimento
        else:
            body_copy = self.body[:-1] # Cria uma cópia do corpo da cobra exluindo o último bloco --> a cauda
            body_copy.insert(0, body_copy[0] + self.direction) # Insere um novo bloco na frente da cabeça da cobra
            self.body = body_copy[:] # Atualiza com a cópia modificada

    def add_block(self): # Aumenta o comprimento da cobra
        self.new_block = True

    def play_crunch_sound(self): # Gera o som quando a cobra comea maçã
        self.crunch_sound.play()

    def reset(self): # Garante que a cobra resete para pos inicial do jogo
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)

    def draw_lives(self, screen): # Sistema de vidas do jogo
        self.screen = screen
        heart_image = pygame.image.load('snake_game/gráficos/Cuore1.png').convert_alpha()
        heart_image = pygame.image.load('snake_game/gráficos/Cuore4.png').convert_alpha()
        heart_size = 30  # Tamanho do coração
        for i in range(self.lives):
            heart_rect = pygame.Rect(10 + i * (heart_size + 10), 10, heart_size, heart_size)
            screen.blit(heart_image, heart_rect)
