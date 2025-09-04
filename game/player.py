import pygame
import math

class Player:
    def __init__(self, x, y, width=50, height=50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.color = (255, 140, 0)  # Naranja para representar el zorro
        
        # Animación simple
        self.animation_timer = 0
        
        # Crear el rectángulo para el sprite
        self.rect = pygame.Rect(x, y, width, height)
    
    def update(self, keys_pressed, screen_width, screen_height):
        # Movimiento con las teclas de flecha
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.x += self.speed
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.y -= self.speed
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.y += self.speed
        
        # Mantener el jugador dentro de los límites de la pantalla
        self.x = max(0, min(self.x, screen_width - self.width))
        self.y = max(0, min(self.y, screen_height - self.height))
        
        # Actualizar la posición del rectángulo
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Actualizar animación
        self.animation_timer += 1
    
    def draw(self, screen):
        # Efecto de "respiración" para hacer el zorro más dinámico
        size_offset = int(2 * abs(math.cos(self.animation_timer * 0.1)))
        draw_rect = pygame.Rect(self.x - size_offset//2, self.y - size_offset//2, 
                               self.width + size_offset, self.height + size_offset)
        
        # Dibujar sombra
        shadow_rect = pygame.Rect(self.x + 3, self.y + 3, self.width, self.height)
        pygame.draw.rect(screen, (0, 0, 0, 100), shadow_rect)
        
        # Dibujar cuerpo principal
        pygame.draw.rect(screen, self.color, draw_rect)
        pygame.draw.rect(screen, (200, 100, 0), draw_rect, 3)  # Borde más oscuro
        
        # Dibujar ojos que parpadean ocasionalmente
        eye_size = 5 if (self.animation_timer // 60) % 10 != 0 else 2  # Parpadeo cada 10 ciclos
        pygame.draw.circle(screen, (0, 0, 0), (self.x + 15, self.y + 15), eye_size)
        pygame.draw.circle(screen, (0, 0, 0), (self.x + 35, self.y + 15), eye_size)
        
        # Dibujar nariz
        nose_color = (139, 69, 19)  # Marrón
        pygame.draw.circle(screen, nose_color, (self.x + 25, self.y + 25), 3)