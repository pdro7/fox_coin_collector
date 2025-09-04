import pygame
import sys
from game.player import Player
from game.coin import Coin
from game.timer import Timer
from game.ui import UI

# Configuración
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (50, 150, 50)  # Verde

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Fox Coin Collector")
    clock = pygame.time.Clock()
    
    # Crear el jugador (zorro) en el centro de la pantalla
    player = Player(WINDOW_WIDTH // 2 - 25, WINDOW_HEIGHT // 2 - 25)
    
    # Crear la primera moneda
    coin = Coin(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    # Variables del juego
    score = 0
    timer = Timer(60)  # 60 segundos
    ui = UI(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    # Estados del juego
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2
    game_state = MENU
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_state == MENU and event.key == pygame.K_SPACE:
                    # Comenzar juego
                    game_state = PLAYING
                    score = 0
                    timer = Timer(60)
                    player = Player(WINDOW_WIDTH // 2 - 25, WINDOW_HEIGHT // 2 - 25)
                    coin.generate_random_position()
                elif game_state == GAME_OVER:
                    if event.key == pygame.K_r:
                        # Reiniciar juego
                        game_state = PLAYING
                        score = 0
                        timer = Timer(60)
                        player = Player(WINDOW_WIDTH // 2 - 25, WINDOW_HEIGHT // 2 - 25)
                        coin.generate_random_position()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
        
        # Lógica del juego según el estado
        if game_state == PLAYING:
            # Obtener teclas presionadas
            keys_pressed = pygame.key.get_pressed()
            
            # Actualizar el timer
            timer.update()
            
            # Verificar si se acabó el tiempo
            if timer.is_time_up():
                game_state = GAME_OVER
            else:
                # Actualizar el jugador
                player.update(keys_pressed, WINDOW_WIDTH, WINDOW_HEIGHT)
                
                # Verificar colisión entre jugador y moneda
                if player.rect.colliderect(coin.rect):
                    score += 1
                    # Generar nueva moneda en posición aleatoria
                    coin.generate_random_position()
        
        # Dibujar todo según el estado
        screen.fill(BACKGROUND_COLOR)
        
        if game_state == MENU:
            # Mostrar algunos elementos de fondo
            player.draw(screen)
            coin.draw(screen)
            ui.draw_start_screen(screen)
        elif game_state == PLAYING:
            player.draw(screen)
            coin.draw(screen)
            ui.draw_hud(screen, score, timer)
        elif game_state == GAME_OVER:
            # Dibujar pantalla de fin del juego
            player.draw(screen)
            coin.draw(screen)
            ui.draw_game_over_screen(screen, score)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()