import random,pygame,sys
from colorama import init, Fore
from wallsANDroads import Wall, Road, Treasure
import time
from buttons import *
from highscore_functions import *


def count_walls(maze, position):
    x, y = position
    walls = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return sum(1 for nx, ny in walls if maze[nx][ny] == 'a')

def generatemaze(height, width):
    maze = [['s' for _ in range(width)] for _ in range(height)]

    start_row, start_col = random.randint(1, height - 2), random.randint(1, width - 2)
    maze[start_row][start_col] = 'a'

    walls = [(start_row - 1, start_col),(start_row, start_col - 1),(start_row, start_col + 1),(start_row + 1, start_col)]

    for i in walls:
        x, y = i
        maze[x][y] = 's'

    while walls:
        rand_wall = random.choice(walls)
        walls.remove(rand_wall)

        x, y = rand_wall
        if 0 < x < height - 1 and 0 < y < width - 1 and maze[x][y] == 's':
            wallsy = count_walls(maze, rand_wall)
            if wallsy < 2:
                maze[x][y] = 'a'
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if maze[nx][ny] != 'a':
                        maze[nx][ny] = 's'
                        walls.append((nx, ny))

    for i in range(width):
        if maze[1][i] == 'a':
            maze[0][i] = 'a'
            break

    for i in range(height - 1, 0, -1):
        if maze[height - 2][i] == 'a':
            maze[height - 1][i] = 'a'
            break

    return maze

def minimum_steps(maze, width, height):
    starty = [(i, j) for i, r in enumerate(maze) for j, c in enumerate(r) if c == 'a' and i == height - 1]
    endy = [(i, j) for i, r in enumerate(maze) for j, c in enumerate(r) if c == 'a' and i == 0]

    starty = starty[0]
    endy = endy[0]

    visited = set()
    q = [(starty, 0)]

    while q:
        c_pos, steps = q.pop(0)
        if c_pos == endy:
            return steps
        visited.add(c_pos)

        x, y = c_pos
        ns = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for nx, ny in ns:
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 's' and (nx, ny) not in visited:
                q.append(((nx, ny), steps + 1))

    return None

def create_maze(maze, settings, screen, walls, roads, treasures, x=0, y=0):
    wall_pic = random.randint(1, 3)
    road_pic = random.randint(1, 3)
    
    # Find all 'a' positions for possible treasure placement
    possible_treasures = [(i, j) for i, row in enumerate(maze) for j, cell in enumerate(row) if cell == 'a']
    
    # Randomly select 5 positions for treasures
    if len(possible_treasures) >= 10:
        treasure_positions = random.sample(possible_treasures, 10)
    else:
        treasure_positions = possible_treasures

    for i, row in enumerate(maze):
        x = 0
        for j, cell in enumerate(row):
            if cell == 'a':
                new_road = Road(x, y, settings, screen, road_pic)
                roads.add(new_road)
                if (i, j) in treasure_positions:
                    new_treasure = Treasure(x, y, settings, screen)
                    treasures.add(new_treasure)
            else:
                new_wall = Wall(x, y, settings, screen, wall_pic)
                walls.add(new_wall)
            x += 30
        y += 40

def draw_maze(walls, roads, treasures):
    for wall in walls.sprites():
        wall.draw_wall()
    for road in roads.sprites():
        road.draw_road()
    for treasure in treasures.sprites():
        treasure.draw_treasure()

    
        
def check_events(player, walls, treasures, settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player, walls, treasures, settings, screen)


            
def check_keydown_events(event, player, walls, treasures, settings, screen):
    initial_x = player.rect.left
    initial_y = player.rect.top

    if event.key == pygame.K_RIGHT:
        player.rect.left += settings.wall_width
        player.step_counter += 1
    elif event.key == pygame.K_LEFT:
        player.rect.left -= settings.wall_width
        player.step_counter += 1
    elif event.key == pygame.K_UP:
        player.rect.top -= settings.wall_height
        player.step_counter += 1
    elif event.key == pygame.K_DOWN and player.rect.top <= settings.screen_height - 40:
        player.rect.top += settings.wall_height
        player.step_counter += 1
    elif event.key == pygame.K_ESCAPE:
        pause_menu(screen, settings)
    player.update_score(-2)
    # Check for collision with walls
    for wall in walls.sprites():
        if player.rect.colliderect(wall):
            player.rect.left = initial_x
            player.rect.top = initial_y
            player.step_counter -= 1
            player.update_score(2)
            break

    # Check for collision with treasures
    for treasure in treasures.sprites():
        if player.rect.colliderect(treasure):
            treasures.remove(treasure)
            player.update_score(7)
            break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player, walls, treasures, settings, screen)

        
def calculate_points(player, minimum_steps):
    minimum_steps=100
    if (player.step_counter - 1) <= minimum_steps:
        return 100
    else:
        excessive_steps = player.step_counter - 1 - minimum_steps
        if excessive_steps < 100:
            return 100 - excessive_steps
        else:
            return 0       
          
def pause_menu(screen, settings):
    image = pygame.image.load('images/211129_r39422web-tout.png')
    image = pygame.transform.scale(image, (settings.screen_width, settings.screen_height))
    screen_rect = screen.get_rect()
    font = pygame.font.Font(None, 70)
    text_surface = font.render("Game is paused", True, settings.pause_menu_text_color)
    text_surface_press_to_continue = font.render("Press spacebar to continue", True, settings.pause_menu_text_color)
    text_rect = text_surface.get_rect()
    text_surface_press_to_continue_rect = text_surface_press_to_continue.get_rect()
    text_rect.center = (screen_rect.centerx, screen_rect.centery + 20)
    text_surface_press_to_continue_rect.center = (screen_rect.centerx, text_rect.centery + 55)
    screen.blit(image, screen_rect)
    screen.blit(text_surface_press_to_continue, text_surface_press_to_continue_rect)
    screen.blit(text_surface, text_rect)
    exit_button=ExitButton(screen,settings)
    exit_button.draw_button(screen,settings)
    pygame.display.flip()
    
    k = True
    while k:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    k = False
            elif event.type == pygame.QUIT:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.button_rect.collidepoint(event.pos):
                    exit.button_pressed = not exit_button.button_pressed
            
        if exit_button.button_pressed:
                    start_menu(screen, settings)
                    exit_button.button_pressed = False

        pygame.display.flip()
          
def maze_finished(screen, settings, player, additional_points, maze_number):
    player.step_counter = 0
    screen_rect = screen.get_rect()
    screen.fill(settings.bg_color)
    font = pygame.font.Font(None, 65)
    text_surface = font.render(f"Maze number {maze_number} finished", True, (0, 0, 0))
    text_surface_gained_points = font.render(f"Points scored: {additional_points}", True, (0, 0, 0))
    text_surface_total_points = font.render(f"Total points: {player.score}", True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect_gained_points = text_surface_gained_points.get_rect()
    text_rect_total_points = text_surface_total_points.get_rect()
    text_rect.center = (screen_rect.centerx, 260)
    text_rect_gained_points.center = (screen_rect.centerx, 315)
    text_rect_total_points.center = (screen_rect.centerx, 370)
    screen.blit(text_surface_gained_points, text_rect_gained_points)
    screen.blit(text_surface_total_points, text_rect_total_points)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    time.sleep(2)
    

        
   
    
def start_menu(screen, settings):
    button_description = Description_button(screen, settings)
    start_game = Start_the_game_button(screen, settings)
    high_scores = HighScoresButton(screen, settings)
    
    screen_rect = screen.get_rect()
    wallpaper = pygame.image.load('images/maze32.png')
    wallpaper = pygame.transform.scale(wallpaper, (settings.screen_width, settings.screen_height))
    
    while settings.start_menu_active:
        screen.blit(wallpaper, screen_rect)
        
        button_description.draw_button(screen, settings)
        start_game.draw_button(screen, settings)
        high_scores.draw_button(screen, settings)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    settings.start_menu_active = False
                elif event.key == pygame.K_d:
                    game_description(screen, settings)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_description.button_rect.collidepoint(event.pos):
                    button_description.button_pressed = not button_description.button_pressed
                elif start_game.button_rect.collidepoint(event.pos):
                    start_game.button_color = (128, 128, 128)
                    start_game.draw_button(screen, settings)
                    settings.start_menu_active = False
                elif high_scores.button_rect.collidepoint(event.pos):
                    high_scores.button_color = (128, 128, 128)
                    high_scores.draw_button(screen, settings)
                    display_highscores(screen, settings)  # Call the function to display high scores

        if button_description.button_pressed:
            game_description(screen, settings)
            button_description.button_pressed = False

        pygame.display.flip()

    
def show_number_of_steps(screen, settings, player):
    screen_rect = screen.get_rect()
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Steps made: {player.step_counter}", True, (230, 230, 230))
    text_rect = text_surface.get_rect()
    text_rect.topright = screen_rect.topright
    text_rect.x -= 5
    text_rect.y += 2
    screen.blit(text_surface, text_rect)
    
def to_pause(screen, settings):
    screen_rect = screen.get_rect()
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Press esc to pause the game", True, (230, 230, 230))
    text_rect = text_surface.get_rect()
    text_rect.bottomright = screen_rect.bottomright
    text_rect.x -= 5
    screen.blit(text_surface, text_rect)
    
def game_description(screen, settings):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 40)
    texts = ['In this game, you have to navigate through various mazes.', 'A player needs to finish the maze before the energy gets to 0.', 'For each step taken energy is reduced by 2 and for each treasure collected energy increases by 5.', 'if the player completes the maze within the minimum steps, ', 'he or she receives 100 points. And for each extra step 1', 'The player cannot receive a negative score.']
    for i, text in enumerate(texts):
        text_surface = font.render(text, True, (230, 230, 230))
        y_position = i * 50 + settings.screen_height/4  # Adjust the spacing here
        screen.blit(text_surface, (settings.screen_width/12, y_position))
    
    button_exit = Exit_description_button(screen, settings)
    button_exit.draw_button(screen, settings)
    pygame.display.flip()
    settings.description_active = True
    while settings.description_active:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    sys.exit()   
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_exit.button_rect.collidepoint(event.pos):
                    settings.description_active = False
                    
def show_points(screen, settings, player):
    screen_rect = screen.get_rect()
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Energy: {player.score}", True, (230, 230, 230))
    text_rect = text_surface.get_rect()
    text_rect.midtop = screen_rect.midtop
    text_rect.y += 2
    screen.blit(text_surface, text_rect)

    
def game_over(screen, settings):
    screen.fill(settings.bg_color)
    font = pygame.font.Font(None, 74)
    text_surface = font.render("Game Over", True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = screen.get_rect().center
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    
    pygame.time.wait(3000)  
    return "game_over"


        

    
        
        

