import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600  # Set your desired window dimensions
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladder Game")

board_image = pygame.image.load('Snakes-And-Ladders-Problem.jpg')
board_rect = board_image.get_rect()
board_x = (WIDTH - board_rect.width) // 2
board_y = (HEIGHT - board_rect.height) // 2

image_width = board_rect.width
image_height = board_rect.height


positions = {}
# Function to draw 100 circles on the board
def draw_circles_on_board():
    start_x, start_y = board_x + 25, board_y + image_height - 25
    circle_count = 10
    circle_radius = 13
    circle_spacing = 40

     

    for j in range(10):  # Loop for different y positions
        for i in range(circle_count):  # Loop for x positions
            x_key = f'x{i+1}_{j+1}'
            y_key = f'y{i+1}_{j+1}'

            x = start_x + i * circle_spacing
            y = start_y - j * circle_spacing

            pygame.draw.circle(window, (22, 0, 0), (x, y), circle_radius)

            positions[x_key] = x
            positions[y_key] = y

    return positions
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))
    window.blit(board_image, (board_x, board_y))
    draw_circles_on_board()
    pygame.display.flip()

pygame.quit()
