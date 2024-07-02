import pygame
from pygame.math import Vector2

class SNAKE:
    def __init__(self, cell_size):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.cell_size = cell_size  # Armazenar o tamanho da célula

        self.head_up = pygame.image.load('snake_game/gráficos/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('snake_game/gráficos/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('snake_game/gráficos/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('snake_game/gráficos/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('snake_game/gráficos/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('snake_game/gráficos/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('snake_game/gráficos/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('snake_game/gráficos/tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('snake_game/gráficos/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('snake_game/gráficos/body_horizontal.png').convert_alpha()
        
        self.body_topright = pygame.image.load('snake_game/gráficos/body_topright.png').convert_alpha()
        self.body_topleft = pygame.image.load('snake_game/gráficos/body_topleft.png').convert_alpha()
        self.body_bottomright = pygame.image.load('snake_game/gráficos/body_bottomright.png').convert_alpha()
        self.body_bottomleft = pygame.image.load('snake_game/gráficos/body_bottomleft.png').convert_alpha()
        
        self.crunch_sound = pygame.mixer.Sound('snake_game/som/plastic-crunch-83779.mp3')

    def draw_snake(self, screen):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            x_pos = int(block.x * self.cell_size)
            y_pos = int(block.y * self.cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
        
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_topleft, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bottomleft, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_topright, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_bottomright, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
