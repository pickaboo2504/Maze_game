import pygame
import sys

def get_player_name(screen, settings):
    font = pygame.font.Font(None, 36)
    prompt_font = pygame.font.Font(None, 48)
    input_box = pygame.Rect(500, 350, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    player_name = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode

        screen.fill((30, 30, 30))
        # Render the prompt text
        prompt_text = prompt_font.render("Enter your name:", True, pygame.Color('white'))
        prompt_rect = prompt_text.get_rect(center=(screen.get_width() // 2, 300))
        screen.blit(prompt_text, prompt_rect)

        # Render the player's input
        txt_surface = font.render(player_name, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    return player_name
