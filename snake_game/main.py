import pygame, sys, random
from pygame.math import Vector2

# Snake (Cobra)
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)] # Blocos iniciais, corpo da cobra
        self.direction = Vector2(1,0)
        self.new_block = False
        
    # Desenhar a cobra    
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,(183,111,122), block_rect)
    
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
apple = pygame.image.load('snake_game/recursos/apple.jpg').convert_alpha()

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
    