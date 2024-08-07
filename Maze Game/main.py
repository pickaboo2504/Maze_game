import pygame
from pygame.sprite import Group
from wallsANDroads import Wall, Road
from mazesettings import Settings
import functions as f
from player import Player
from player_name import *
from highscore_functions import insert_highscore, get_highscores

def run_maze():
    pygame.init()
    
    settings = Settings()
    pygame.display.set_caption("Maze")
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    f.start_menu(screen, settings)
    player_name = get_player_name(screen, settings)  # Get player name
    player = Player(settings, screen, player_name)  # Pass player name to Player object
    
    maze_number = 1
    
    while True:
        
        maze = f.generatemaze(settings.maze_height, settings.maze_width)
        minimum_steps = f.minimum_steps(maze, settings.maze_width, settings.maze_height)
        
        start_x = maze[-1].index('a') * settings.wall_width
        player.rect.topleft = (start_x, settings.screen_height - settings.wall_height)
        
        walls = Group()
        roads = Group()
        treasures = Group()
        
        f.create_maze(maze, settings, screen, walls, roads, treasures)
        
        while True:
            f.draw_maze(walls, roads, treasures)
            f.check_events(player, walls, treasures, settings, screen)
            
            player.draw_player()
            f.show_number_of_steps(screen, settings, player)
            f.to_pause(screen, settings)
            f.show_points(screen, settings, player)
            
            if player.rect.top < 0:
                additional_points = f.calculate_points(player, minimum_steps)
                player.score += additional_points
                insert_highscore(player.name, player.score)  # Insert high score
                f.maze_finished(screen, settings, player, additional_points, maze_number)
                maze_number += 1
                break

            if player.score <= 0:
                f.game_over(screen, settings)
                break
        
            pygame.display.flip()
        

run_maze()

