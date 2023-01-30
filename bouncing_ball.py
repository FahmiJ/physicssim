import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (400, 300)
screen = pygame.display.set_mode(screen_size)

# Set clock
clock = pygame.time.Clock()

# Set font for text display
font = pygame.font.Font(None, 30)

# Set ball parameters
ball_size = 30
ball_x = screen_size[0] // 2
ball_y = ball_size // 2
ball_velocity_y = 0

# Set coefficient of restitution
e = 0.8

# Set acceleration due to gravity 100 px = 10 m
g = 100

# Set button parameters
restart_button = pygame.Rect(10, 270, 80, 20)
add_button = pygame.Rect(300, 250, 80, 20)
decrease_button = pygame.Rect(300, 270, 80, 20)
play_pause_button = pygame.Rect(10, 250, 80, 20)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button.collidepoint(event.pos):
                ball_y = ball_size // 2
                ball_velocity_y = 0
            elif play_pause_button.collidepoint(event.pos):
                if ball_velocity_y > 0:
                    ball_velocity_y = 0
                    g = 0
                else:
                    g = 100
        if event.type == pygame.MOUSEBUTTONDOWN and add_button.collidepoint(event.pos):
            e += 0.1
            if e >1.0:
                e = 1.0
        if event.type == pygame.MOUSEBUTTONDOWN and decrease_button.collidepoint(event.pos):
            e -= 0.1
            if e < 0.05:
                e = 0.0
    # Get elapsed time since last update
    dt = clock.tick(60) / 1000

    # Update velocity
    ball_velocity_y += g * dt

    # Update position
    ball_y += ball_velocity_y * dt

    # Bounce the ball if it hits the bottom of the screen
    if ball_y > 300 - ball_size:
        ball_y = 300 - ball_size
        ball_velocity_y = -ball_velocity_y * e

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, (0, 0, 255), (int(ball_x), int(ball_y)), ball_size)

    # Display height of ball
    ball_height_text = font.render("Height: " + str(round(((270 - ball_y)/10),2))+"m", True, (0, 0, 0))
    screen.blit(ball_height_text, (10, 10))

    # Display velocity of ball
    if ball_y == 300 - ball_size:
        ball_velocity_text = font.render("Velocity: 0", True, (0, 0, 0))
    else:
        ball_velocity_text = font.render("Velocity: " + str(round(((ball_velocity_y)/10),2)), True, (0, 0, 0))
    screen.blit(ball_velocity_text, (10, 30))
    
    #Tulisan koefisien restitusi
    e_text = font.render("e= " + str(round(e,2)),True, (0, 0, 0))
    screen.blit(e_text, (300,230))
    
    # Draw the play/pause button
    pygame.draw.rect(screen, (0, 255, 0), play_pause_button)
    play_pause_button_text = font.render("Play/pause", True, (255, 255, 255))
    screen.blit(play_pause_button_text, (15, 250))
    
    # Draw the restart button
    pygame.draw.rect(screen, (100, 0, 0), restart_button)
    restart_button_text = font.render("Restart", True, (255, 255, 255))
    screen.blit(restart_button_text, (15, 270))
    
    # Draw the add button
    pygame.draw.rect(screen, (0, 0, 255), add_button)
    add_button_text = font.render("+0.1", True, (255, 255, 255))
    screen.blit(add_button_text, (300, 250))
    
    # Draw the decrease button
    pygame.draw.rect(screen, (255, 0, 0), decrease_button)
    decrease_button_text = font.render("-0.1", True, (255, 255, 255))
    screen.blit(decrease_button_text, (300, 270))

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
