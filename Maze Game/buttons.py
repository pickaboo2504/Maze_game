import pygame

class Description_button:
    
    def __init__(self, screen, settings):
        self.button_pressed = False
        self.font = pygame.font.Font(None, 72)
        self.button_text = self.font.render('How to play', True, (0, 250, 0))
        self.button_rect = self.button_text.get_rect()
        screen_rect = screen.get_rect()
        self.button_rect.center = (screen_rect.centerx, screen_rect.centery + 75)
        
        self.button_color = (230, 230, 230)

    
    def draw_button(self, screen, settings):
        pygame.draw.rect(screen, self.button_color, self.button_rect)
        screen.blit(self.button_text, self.button_rect)
            
class Exit_description_button:
    
    def __init__(self, screen, settings):
        
        self.font = pygame.font.Font(None, 72)
        self.button_text = self.font.render('Exit', True, (0, 0, 0))
        self.button_rect = self.button_text.get_rect()
        screen_rect = screen.get_rect()
        self.button_rect.center = (settings.screen_width/12 + 50, screen_rect.centery + 160)

    
    def draw_button(self, screen, settings):
        pygame.draw.rect(screen, (239, 230, 230), self.button_rect)
        screen.blit(self.button_text, self.button_rect)
        
class Start_the_game_button:
    
    def __init__(self, screen, settings):
        
        self.button_color = (0, 250, 0)
        
        self.font = pygame.font.Font(None, 72)
        self.button_text = self.font.render('Start the game', True, (0, 0, 0))
        self.button_rect = self.button_text.get_rect()
        screen_rect = screen.get_rect()
        self.button_rect.center = screen_rect.center

    
    def draw_button(self, screen, settings):
        pygame.draw.rect(screen, self.button_color, self.button_rect)
        screen.blit(self.button_text, self.button_rect)


class HighScoresButton:
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 48)
        
        self.button_rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_rect.centerx = self.screen_rect.centerx
        self.button_rect.centery = self.screen_rect.centery + 150  # Position below the other buttons

        self.button_pressed = False
        
        self.prep_msg("High Scores")

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center

    def draw_button(self, screen, settings):
        screen.fill(self.button_color, self.button_rect)
        screen.blit(self.msg_image, self.msg_image_rect)


class Exit_highscore_button:
    
    def __init__(self, screen, settings):
        
        self.font = pygame.font.Font(None, 72)
        self.button_text = self.font.render('Exit', True, (0, 0, 0))
        self.button_rect = self.button_text.get_rect()
        screen_rect = screen.get_rect()
        self.button_rect.center = (settings.screen_width/5 + 100, screen_rect.centery + 100)

    
    def draw_button(self, screen, settings):
        pygame.draw.rect(screen, (239, 230, 230), self.button_rect)
        screen.blit(self.button_text, self.button_rect)

class ExitButton:
    
    def __init__(self, screen, settings):
        self.button_pressed = False
        self.font = pygame.font.Font(None, 72)
        self.button_text = self.font.render('Exit', True, (0, 0, 0))
        self.button_rect = self.button_text.get_rect()
        screen_rect = screen.get_rect()
        self.button_rect.center = (settings.screen_width/12 + 50, screen_rect.centery + 160)

    
    def draw_button(self, screen, settings):
        pygame.draw.rect(screen, (239, 230, 230), self.button_rect)
        screen.blit(self.button_text, self.button_rect)