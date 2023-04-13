import pygame

pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the player
player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10
player_x_speed = 0

# Set up the game loop
clock = pygame.time.Clock()
game_over = False
score = 0
font = pygame.font.SysFont(None, 40)

def show_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [10, 10])

while not game_over:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_speed = -5
            elif event.key == pygame.K_RIGHT:
                player_x_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_speed = 0

    # Move the player
    player_x += player_x_speed
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

    # Fill the screen with white
    screen.fill(white)

    # Draw the player
    pygame.draw.rect(screen, black, [player_x, player_y, player_width, player_height])

    # Show the score
    show_score(score)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
quit()
