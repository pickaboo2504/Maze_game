import pygame

class Player():
    
    def __init__(self, settings, screen,name):
        
        self.screen = screen
        self.settings = settings
        
        self.image = pygame.image.load('images/bunny.png')
        self.image = pygame.transform.scale(self.image, settings.cell_size)
        
        
        self.rect = self.image.get_rect()
        
        self.screen_rect = screen.get_rect()
        
        self.name = name
        self.step_counter = 0
        self.score = 100

        
        
    def draw_player(self):
        
        self.screen.blit(self.image, self.rect)
    
    def update_score(self, points):
        self.score += points