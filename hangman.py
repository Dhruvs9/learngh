import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle settings
paddle_width = 15
paddle_height = 100
player_paddle_y = window_height // 2 - paddle_height // 2
opponent_paddle_y = window_height // 2 - paddle_height // 2
paddle_speed = 6

# Ball settings
ball_size = 15
ball_speed_x = 6
ball_speed_y = 6

# Game loop variables
clock = pygame.time.Clock()
game_over = False

# Initialize ball_rect
ball_rect = pygame.Rect(window_width // 2 - ball_size // 2, window_height // 2 - ball_size // 2, ball_size, ball_size)

# Reset the ball to the center with a random direction
def reset_ball():
    ball_rect.centerx = window_width // 2
    ball_rect.centery = window_height // 2
    return random.choice([1, -1]), random.choice([1, -1])

# Draw paddles and ball
def draw_objects():
    window.fill(black)
    pygame.draw.rect(window, white, player_paddle)
    pygame.draw.rect(window, white, opponent_paddle)
    pygame.draw.ellipse(window, white, ball_rect)

# Move paddles and ball
def move_objects():
    player_paddle.y += player_paddle_speed
    opponent_paddle.y += opponent_paddle_speed
    ball_rect.x += ball_speed_x * ball_direction[0]
    ball_rect.y += ball_speed_y * ball_direction[1]

# Check collisions with window boundaries
def check_collisions():
    if player_paddle.top < 0:
        player_paddle.top = 0
    elif player_paddle.bottom > window_height:
        player_paddle.bottom = window_height

    if opponent_paddle.top < 0:
        opponent_paddle.top = 0
    elif opponent_paddle.bottom > window_height:
        opponent_paddle.bottom = window_height

    if ball_rect.top < 0 or ball_rect.bottom > window_height:
        ball_direction[1] = -ball_direction[1]

# Check collisions with paddles
def check_paddle_collisions():
    if ball_rect.colliderect(player_paddle) or ball_rect.colliderect(opponent_paddle):
        ball_direction[0] = -ball_direction[0]

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Get user input for player paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_paddle_speed = -paddle_speed
    elif keys[pygame.K_s]:
        player_paddle_speed = paddle_speed
    else:
        player_paddle_speed = 0

    # AI for opponent paddle movement
    if ball_rect.centery < opponent_paddle.centery:
        opponent_paddle_speed = -paddle_speed
    elif ball_rect.centery > opponent_paddle.centery:
        opponent_paddle_speed = paddle_speed
    else:
        opponent_paddle_speed = 0

    # Create paddles
    player_paddle = pygame.Rect(30, player_paddle_y, paddle_width, paddle_height)
    opponent_paddle = pygame.Rect(window_width - 30 - paddle_width, opponent_paddle_y, paddle_width, paddle_height)

    # Check for collisions and move objects
    check_collisions()
    check_paddle_collisions()
    move_objects()

    # Draw objects on the screen
    draw_objects()

    # Update the display
    pygame.display.update()

    # Set the frames per second (FPS)
    clock.tick(60)

# Quit Pygame and the program
pygame.quit()
