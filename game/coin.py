import pygame
import random

class Coin:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 20
        self.height = 20
        self.color = (255, 215, 0)  # Oro
        self.outline_color = (255, 165, 0)  # Naranja dorado
        
        # Animación de rotación
        self.rotation = 0
        self.pulse_timer = 0
        
        # Generar posición aleatoria
        self.generate_random_position()
        
        # Crear el rectángulo para colisiones
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def generate_random_position(self):
        # Generar posición aleatoria pero con margen desde los bordes
        margin = 30
        self.x = random.randint(margin, self.screen_width - self.width - margin)
        self.y = random.randint(margin, self.screen_height - self.height - margin)
        
        # Actualizar rectángulo
        if hasattr(self, 'rect'):
            self.rect.x = self.x
            self.rect.y = self.y
    
    def update(self):
        # Actualizar animaciones
        self.rotation += 5
        self.pulse_timer += 1
        
    def draw(self, screen):
        # Actualizar animaciones
        self.update()
        
        # Efecto de pulsación
        pulse_offset = int(3 * abs(pygame.math.sin(self.pulse_timer * 0.1)))
        
        # Dibujar círculo dorado con borde
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        radius = self.width // 2 + pulse_offset
        
        # Efecto de brillo giratorio
        for i in range(3):
            alpha_color = (255, 255, 100, 50 - i * 15)
            glow_radius = radius + i * 3
            # Simular brillo con múltiples círculos
            pygame.draw.circle(screen, (255, 255, 150), (center_x, center_y), glow_radius + 2)
        
        # Círculo exterior (borde)
        pygame.draw.circle(screen, self.outline_color, (center_x, center_y), radius + 2)
        # Círculo interior (moneda)
        pygame.draw.circle(screen, self.color, (center_x, center_y), radius)
        
        # Brillo dinámico que se mueve
        shine_x = center_x + int(3 * pygame.math.cos(self.rotation * 0.1))
        shine_y = center_y + int(3 * pygame.math.sin(self.rotation * 0.1))
        pygame.draw.circle(screen, (255, 255, 255), (shine_x, shine_y), 2)
        
        # Símbolo de moneda opcional
        font = pygame.font.Font(None, 16)
        dollar_text = font.render("$", True, (200, 150, 0))
        text_rect = dollar_text.get_rect(center=(center_x, center_y))
        screen.blit(dollar_text, text_rect)