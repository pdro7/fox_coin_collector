import pygame

class Timer:
    def __init__(self, duration_seconds=60):
        self.duration = duration_seconds * 1000  # Convertir a milisegundos
        self.time_remaining = self.duration
        self.start_time = pygame.time.get_ticks()
        
    def update(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        self.time_remaining = max(0, self.duration - elapsed_time)
        
    def get_time_remaining_seconds(self):
        return self.time_remaining // 1000
    
    def is_time_up(self):
        return self.time_remaining <= 0
    
    def format_time(self):
        seconds = self.get_time_remaining_seconds()
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"