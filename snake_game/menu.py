import pygame, sys

def show_menu(screen, game_font, cell_size, cell_number, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Retorna para sair do loop e iniciar o jogo

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
