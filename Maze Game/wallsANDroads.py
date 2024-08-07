import pygame
from pygame.sprite import Sprite



class Wall(Sprite):
    
    def __init__(self, x, y, settings, screen, wall_pic):
        
        super(Wall, self).__init__()
        
        walls_pictures = {1: 'images/Castle_Wall.jpg', 2: 'images/blue_wall.png', 3: 'images/Dungeon_Wall.png'}
        
        
        self.x = x
        self.y = y
        
        self.image = pygame.image.load(walls_pictures[wall_pic])
        self.image = pygame.transform.scale(self.image, settings.cell_size)
        
        
        
        self.screen = screen
        
        self.rect = pygame.Rect(x, y, settings.wall_width, settings.wall_height)
        
    def draw_wall(self):
        
        self.screen.blit(self.image, self.rect)
        
        
        
class Road(Sprite):
    
    def __init__(self, x, y, settings, screen, road_pic):
        
        super(Road, self).__init__()
        
        roads_pictures = {1: 'images/pink.png', 2: 'images/pastelgreen.png', 3: 'images/grass.jpg' }
        
        self.x = x
        self.y = y
        
        self.image = pygame.image.load(roads_pictures[road_pic])
        self.image = pygame.transform.scale(self.image, settings.cell_size)
        
        
        
        self.screen = screen
        
        self.rect = pygame.Rect(x, y, settings.wall_width, settings.wall_height)
        
    def draw_road(self):
        
        self.screen.blit(self.image, self.rect)



class Treasure(Sprite):
    
    def __init__(self, x, y, settings, screen):
        
        super(Treasure, self).__init__()
        
        treasures = 'images/treasure.png'
        
        self.x = x
        self.y = y
        
        self.image = pygame.image.load(treasures)
        self.image = pygame.transform.scale(self.image, settings.cell_size)
        
        
        
        self.screen = screen
        
        self.rect = pygame.Rect(x, y, settings.wall_width, settings.wall_height)
        
    def draw_treasure(self):
        
        self.screen.blit(self.image, self.rect)
