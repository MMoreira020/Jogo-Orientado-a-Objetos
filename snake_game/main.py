import pygame, sys, random
from pygame.math import Vector2

# Snake (Cobra)
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)] # Blocos iniciais, corpo da cobra
        self.direction = Vector2(1,0)
        self.new_block = False
        
        self.head_up = pygame.image.load('snake_game/gráficos/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('snake_game/gráficos/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('snake_game/gráficos/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('snake_game/gráficos/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('snake_game/gráficos/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('snake_game/gráficos/tail_down.png').convert_alpha()
        self.tail_rigth = pygame.image.load('snake_game/gráficos/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('snake_game/gráficos/tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('snake_game/gráficos/body_vertical.png').convert_alpha()
        self.body_orizontal = pygame.image.load('snake_game/gráficos/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('snake_game/gráficos/body_topright.png').convert_alpha()
        self.body_tl = pygame.image.load('snake_game/gráficos/body_topleft.png').convert_alpha()
        self.body_br = pygame.image.load('snake_game/gráficos/body_bottomright.png').convert_alpha()
        self.body_bl = pygame.image.load('snake_game/gráficos/body_bottomleft.png').convert_alpha()
        
        
    # Desenhar a cobra    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        
        # Direção que o rosto da cobra está indo
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
                    screen.blit(self.body_orizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
        
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_rigth
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down       
        
       
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True
        
# Fruta do jogo
class FRUIT:
    def __init__(self):
        self.randomize()
    
    # Desenhar a fruta
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen,(126,166, 114), fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y) 
        
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #reposicionar a fruta
            self.fruit.randomize()
            
            # adicionar novo bloco a cobra
            self.snake.add_block()
            
    def check_fail(self):
        #Verificar se a cobra está fora da tela
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        #Verificar se a cobra bate nela mesma
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    def game_over(self):
        pygame.quit()
        sys.exit()
    
pygame.init()
cell_size = 40
cell_number = 18
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) #Tamanho da tela
clock = pygame.time.Clock()
apple = pygame.image.load('snake_game/gráficos/apple.png').convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()


#Mater o loop do jogo em execução
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
    