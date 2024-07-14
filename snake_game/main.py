import pygame, sys
from pygame.math import Vector2
from main_game import MAIN

pygame.mixer.pre_init(44100, -16, 2, 512) # Inicializa o mixer do Pygame 
pygame.init() # Iniciliza os módulos do pygame
cell_size = 40 # Tam de cada célula na tela do jogo como 40 pixels
cell_number = 18 # Número de células por lado na tela do jogo 18 
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) # Tamanho da tela --> 720 x 720
clock = pygame.time.Clock() # Controla a taxa de quadros por segundo
apple = pygame.image.load('snake_game/gráficos/apple.png').convert_alpha() # Imagem da maçã
game_font = pygame.font.Font('snake_game/fonte/PoetsenOne-Regular.ttf', 25) # Fonte do jogo

SCREEN_UPDATE = pygame.USEREVENT # Define um evento personalizado
pygame.time.set_timer(SCREEN_UPDATE, 150) # Configura um temporizador para o evento 

main_game = MAIN(cell_size, cell_number) # Inicializa o jogo com as config de células e tela

def show_menu():
    while True: # Garante que o menu seja exibido até que o jogador pressione enter
        for event in pygame.event.get(): # Itera sobre os eventos capturados do Pygame
            if event.type == pygame.QUIT: # verifica se o evento é do tipo QUIT
                pygame.quit() # Fecha a janela do jogo
                sys.exit() # progama encerrado 
            if event.type == pygame.KEYDOWN: # Verifica se uam tecla é pressioanda
                if event.key == pygame.K_RETURN: # Verifica se a tecla pressionada é enter
                    return

        # Desenho do menu na tela
        screen.fill((175, 215, 70))
        menu_text = game_font.render("Snake Game", True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(cell_number * cell_size // 2, cell_number * cell_size // 2 - 50))
        screen.blit(menu_text, menu_rect)

        start_text = game_font.render("Pressione Enter para iniciar", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(cell_number * cell_size // 2, cell_number * cell_size // 2))
        screen.blit(start_text, start_rect)

        instruction_text = game_font.render("Instruções: Use as setas para mover", True, (255, 255, 255))
        instruction_rect = instruction_text.get_rect(center=(cell_number * cell_size // 2, cell_number * cell_size // 2 + 50))
        screen.blit(instruction_text, instruction_rect)

        pygame.display.update()
        clock.tick(60)

show_menu()

while True: # Executa até que o jogo seja encerrado
    for event in pygame.event.get(): # Itera sobre os eventos capturados pelo pygame
        if event.type == pygame.QUIT: # Se o evento for do tipo QUIT
            pygame.quit() # Pygame encerrado
            sys.exit() # programa finalizado
        if event.type == SCREEN_UPDATE: # Verfica se o evento eh do tipo SCREEN_UPDATE
            main_game.update(screen, game_font, cell_number, clock)  # Atualiza a lógica do jogo
        if event.type == pygame.KEYDOWN: # Verfica se o evento eh do tipo KEYDOWN --> tecla pressionada
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

    # Desenha os elementos da tela/atualiza a tela e controla o FPS
    screen.fill((175, 215, 70))
    main_game.draw_elements(screen, apple, game_font)
    pygame.display.update()
    clock.tick(60)
