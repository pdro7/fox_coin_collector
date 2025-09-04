import pygame

class UI:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Configurar fuentes
        pygame.font.init()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        # Colores
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.gold = (255, 215, 0)
        
    def draw_hud(self, screen, score, timer):
        # Fondo semi-transparente para el HUD
        hud_bg = pygame.Surface((self.screen_width, 60))
        hud_bg.set_alpha(100)
        hud_bg.fill((0, 0, 0))
        screen.blit(hud_bg, (0, 0))
        
        # Dibujar puntuación con icono de moneda
        score_text = self.font_medium.render(f"💰 Monedas: {score}", True, self.gold)
        screen.blit(score_text, (10, 15))
        
        # Dibujar tiempo con color que cambia según el tiempo restante
        time_remaining = timer.get_time_remaining_seconds()
        if time_remaining > 30:
            time_color = self.white
        elif time_remaining > 10:
            time_color = (255, 255, 0)  # Amarillo
        else:
            time_color = self.red  # Rojo para urgencia
            
        time_text = self.font_medium.render(f"⏰ Tiempo: {timer.format_time()}", True, time_color)
        time_rect = time_text.get_rect()
        screen.blit(time_text, (self.screen_width - time_rect.width - 10, 15))
        
    def draw_game_over_screen(self, screen, final_score):
        # Crear superficie semi-transparente
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill(self.black)
        screen.blit(overlay, (0, 0))
        
        # Título de fin del juego
        game_over_text = self.font_large.render("¡TIEMPO AGOTADO!", True, self.red)
        game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 60))
        screen.blit(game_over_text, game_over_rect)
        
        # Puntuación final
        score_text = self.font_medium.render(f"Monedas recolectadas: {final_score}", True, self.gold)
        score_rect = score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        screen.blit(score_text, score_rect)
        
        # Instrucciones para reiniciar
        restart_text = self.font_small.render("Presiona R para jugar de nuevo o ESC para salir", True, self.white)
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 60))
        screen.blit(restart_text, restart_rect)
    
    def draw_start_screen(self, screen):
        # Fondo semi-transparente
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(200)
        overlay.fill((0, 50, 0))  # Verde oscuro
        screen.blit(overlay, (0, 0))
        
        # Título del juego
        title_text = self.font_large.render("FOX COIN COLLECTOR", True, self.gold)
        title_rect = title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 100))
        screen.blit(title_text, title_rect)
        
        # Instrucciones
        instructions = [
            "¡Ayuda al zorro a recoger todas las monedas que puedas!",
            "",
            "CONTROLES:",
            "Flechas o WASD - Mover al zorro",
            "",
            "OBJETIVO:",
            "Recoger el mayor número de monedas en 60 segundos",
            "",
            "Presiona ESPACIO para comenzar"
        ]
        
        y_offset = self.screen_height // 2 - 20
        for line in instructions:
            if line == "":
                y_offset += 15
                continue
            if line.startswith("CONTROLES:") or line.startswith("OBJETIVO:"):
                text = self.font_medium.render(line, True, self.gold)
            else:
                text = self.font_small.render(line, True, self.white)
            
            text_rect = text.get_rect(center=(self.screen_width // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 25