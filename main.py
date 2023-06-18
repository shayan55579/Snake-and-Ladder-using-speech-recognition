import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snakes and Ladders")

# Set the font
font = pygame.font.SysFont("comicsansms", 30)

# Define the board
board = {
    1: 38, # it's a ladder if a player lands on position 1, they will be moved to position 38. 
    4: 14,
    9: 31,
    16: 6,
    21: 42,
    28: 84,
    36: 44,
    48: 26,
    49: 11,
    51: 67,
    56: 53,
    62: 19,
    64: 60,
    71: 91,
    80: 100,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

# Set the player positions
player_positions = {
    1: 0,
    2: 0
}

# Define the player colors
player_colors = {
    1: (255, 0, 0),
    2: (0, 0, 255)
}

# Define the player tokens
player_tokens = {
    1: pygame.transform.scale(pygame.image.load(r"E:\Univecity\Snakes and ladders\red_token.png"), (screen_width- 10, screen_height - 10)),
    2: pygame.transform.scale(pygame.image.load(r"E:\Univecity\Snakes and ladders\blue_token.png"), (screen_width - 10, screen_height - 10))
}

# Set the initial player turn
player_turn = 1

# Define the function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Define the function to move the player
def move_player(player, roll):
    player_positions[player] += roll
    if player_positions[player] in board:
        player_positions[player] = board[player_positions[player]]

# Define constants for drawing the board
ROWS = 10
COLUMNS = 10
CELL_TOP_LEFT_X = 50
CELL_TOP_LEFT_Y = 50
CELL_WIDTH = 50
CELL_HEIGHT = 50
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the function to draw the board
def draw_board():
    # Draw the cells
    for row in range(ROWS):
        for col in range(COLUMNS):
            x = CELL_TOP_LEFT_X + col * CELL_WIDTH
            y = CELL_TOP_LEFT_Y + row * CELL_HEIGHT
            pygame.draw.rect(screen, BLACK, (x, y, CELL_WIDTH, CELL_HEIGHT), 1)

    # Draw the snakes and ladders
    for start, end in board.items():
        start_row = (start - 1) // ROWS
        start_col = (start - 1) % COLUMNS
        end_row = (end - 1) // ROWS
        end_col = (end - 1) % COLUMNS

        start_x = CELL_TOP_LEFT_X + start_col * CELL_WIDTH
        start_y = CELL_TOP_LEFT_Y + start_row * CELL_HEIGHT
        end_x = CELL_TOP_LEFT_X + end_col * CELL_WIDTH
        end_y = CELL_TOP_LEFT_Y + end_row * CELL_HEIGHT

        pygame.draw.line(screen, RED, (start_x + CELL_WIDTH // 2, start_y + CELL_HEIGHT // 2), (end_x + CELL_WIDTH // 2, end_y + CELL_HEIGHT // 2), 5)

# Define the function to draw the players
def draw_players():
    for player, position in player_positions.items():
        if player == 1:
            x = 20
            y = screen_height - 70
            color = player_colors[1]
        else:
            x = screen_width - 70
            y = screen_height - 70
            color = player_colors[2]

        pygame.draw.circle(screen, color, (x, y), 20)
        text = font.render(str(position), True, (255, 255, 255))
        screen.blit(text, (x - 5, y - 5))

# Define the function to draw the turn indicator
def draw_turn_indicator():
    text = font.render("Player " + str(player_turn) + "'s Turn", True, player_colors[player_turn])
    screen.blit(text, (10, 10))

# Define the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Roll the dice and move the player
                roll = roll_dice()
                move_player(player_turn, roll)
                # Switch the player turn
                player_turn = 2 if player_turn == 1 else 1

    # Draw the board, players, and turn indicator
    screen.fill((255, 255, 255))
    draw_board()
    draw_players()
    draw_turn_indicator()

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
