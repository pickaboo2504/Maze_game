import sqlite3, sys, pygame
from buttons import Exit_highscore_button



def insert_highscore(player_name, score):
    conn = sqlite3.connect('highscores.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO highscores (player_name, score) VALUES (?, ?)', (player_name, score))
    conn.commit()
    conn.close()




def get_highscores(limit=10):
    conn = sqlite3.connect('highscores.db')
    cursor = conn.cursor()
    cursor.execute('SELECT player_name, score FROM highscores ORDER BY score DESC LIMIT ?', (limit,))
    highscores = cursor.fetchall()
    conn.close()
    return highscores



def display_highscores(screen, settings):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 40)
    high_scores = get_highscores()  # Retrieving high scores from the database
    
    title_text = font.render("High Scores", True, (230, 230, 230))
    screen.blit(title_text, (settings.screen_width // 2 - title_text.get_width() // 2, 50))
    
    y_position = 150
    for i, score in enumerate(high_scores):
        name, score_value = score
        score_text = font.render(f"{i + 1}. {name} - {score_value}", True, (230, 230, 230))
        screen.blit(score_text, (settings.screen_width // 12, y_position))
        y_position += 50  # Adjusting the space
    
    button_exit = Exit_highscore_button(screen, settings)
    button_exit.draw_button(screen, settings)
    pygame.display.flip()
    
    settings.highscores_active = True
    while settings.highscores_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_exit.button_rect.collidepoint(event.pos):
                    settings.highscores_active = False
