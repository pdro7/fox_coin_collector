import pygame
import math

class Player:
    def __init__(self, x, y, width=50, height=50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        
        # Animación simple
        self.animation_timer = 0
        
        # Cargar sprite del zorro
        try:
            self.sprite = pygame.image.load("assets/images/fox.png").convert_alpha()
            # Escalar la imagen al tamaño deseado
            self.sprite = pygame.transform.scale(self.sprite, (width, height))
            self.use_sprite = True
        except (pygame.error, FileNotFoundError):
            # Fallback: usar color si no se puede cargar la imagen
            self.color = (255, 140, 0)  # Naranja para representar el zorro
            self.use_sprite = False
            print("No se pudo cargar fox.png, usando dibujo programático")
        
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
        if self.use_sprite:
            # Usar sprite de imagen
            # Efecto de "respiración" muy sutil
            size_offset = int(1 * abs(math.cos(self.animation_timer * 0.05)))
            
            # Dibujar sombra
            shadow_offset = 2
            pygame.draw.ellipse(screen, (0, 0, 0, 80), 
                               (self.x + shadow_offset, self.y + self.height + shadow_offset - 5, 
                                self.width, 8))
            
            # Aplicar efecto de respiración escalando ligeramente
            if size_offset > 0:
                scaled_sprite = pygame.transform.scale(self.sprite, 
                                                     (self.width + size_offset, self.height + size_offset))
                screen.blit(scaled_sprite, (self.x - size_offset//2, self.y - size_offset//2))
            else:
                screen.blit(self.sprite, (self.x, self.y))
        else:
            # Fallback al dibujo programático anterior
            # Efecto de "respiración" sutil
            size_offset = int(1 * abs(math.cos(self.animation_timer * 0.05)))
            
            # Colores del zorro
            orange = (255, 140, 0)
            dark_orange = (200, 100, 0)
            white = (255, 255, 255)
            black = (0, 0, 0)
            pink = (255, 182, 193)
            
            # Posición base con efecto de respiración
            base_x = self.x - size_offset
            base_y = self.y - size_offset
            
            # Dibujar sombra
            shadow_offset = 2
            pygame.draw.ellipse(screen, (0, 0, 0, 50), 
                               (self.x + shadow_offset, self.y + self.height + shadow_offset - 5, 
                                self.width, 8))
            
            # Cuerpo principal (óvalo)
            body_rect = (base_x + 5, base_y + 15, self.width - 10, self.height - 15)
            pygame.draw.ellipse(screen, orange, body_rect)
            pygame.draw.ellipse(screen, dark_orange, body_rect, 2)
            
            # Cabeza (círculo)
            head_center = (base_x + self.width // 2, base_y + 15)
            head_radius = 15 + size_offset
            pygame.draw.circle(screen, orange, head_center, head_radius)
            pygame.draw.circle(screen, dark_orange, head_center, head_radius, 2)