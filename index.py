import pygame
import random
import speech_recognition as sr

pygame.init()
WIDTH, HEIGHT = 800, 600  # Set your desired window dimensions
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladder Game")

board_image = pygame.image.load('Snakes-And-Ladders-Problem.jpg')
board_rect = board_image.get_rect()
board_x = (WIDTH - board_rect.width) // 2
board_y = (HEIGHT - board_rect.height) // 2

window.blit(board_image, (board_x, board_y))  # Render the board image at the calculated position

image_width = board_rect.width
image_height = board_rect.height

# Player positions
player1_position = 0
player2_position = 0

# Dice value
dice_value = 0

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        draw_text(self.text, self.rect.x + self.rect.width // 2 - 25, self.rect.y + self.rect.height // 2 - 10, (255, 255, 255))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
            else:
                self.color = (0, 0, 255)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

# Function to handle dice roll button click
def roll_dice_button_action():
    global player1_position, player2_position, dice_value
    dice_value = random.randint(1, 6)
    player1_position += dice_value
    player2_position += dice_value
    update_player_position()

# Create the dice roll button
dice_roll_button = Button(350, 500, 100, 50, "Roll Dice", (0, 0, 255), (0, 0, 200), roll_dice_button_action)

# Function to update player positions based on special rules (if any)
def update_player_position():
    # Add any special rules for snakes and ladders here
    pass

# Function to draw text on the screen
def draw_text(text, x, y, color, size=30):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y))

# Function to draw the board
def draw_board():
    window.blit(board_image, (board_x, board_y))

# Function to draw the player circles
def draw_players():
    if player1_position > 0:
        start_x, start_y = board_x + 25, board_y + image_height - 25
        x = start_x + ((player1_position - 1) % 10) * 70 + 30
        y = start_y - ((player1_position - 1) // 10) * 70

        if board_x <= x < board_x + board_rect.width and board_y <= y < board_y + board_rect.height:
            pygame.draw.circle(window, (255, 0, 0), (x, y), 13)

    if player2_position > 0:
        start_x, start_y = board_x + 25, board_y + image_height - 25
        x = start_x + ((player2_position - 1) % 10) * 70 + 50
        y = start_y - ((player2_position - 1) // 10) * 70 + 40

        if board_x <= x < board_x + board_rect.width and board_y <= y < board_y + board_rect.height:
            pygame.draw.circle(window, (0, 255, 0), (x, y), 10)

# Function to draw game information
def draw_game_info():
    player1_info = f"Player 1 Position: {player1_position}"
    player2_info = f"Player 2 Position: {player2_position}"
    dice_info = f"Dice Value: {dice_value}"
    draw_text(player1_info, 10, 10, (0, 0, 0))
    draw_text(player2_info, 10, 50, (0, 0, 0))
    draw_text(dice_info, 10, 90, (0, 0, 0))

# Initialize speech recognition
r = sr.Recognizer()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        dice_roll_button.handle_event(event)

    # Listen for the word "تاس بنداز" (roll the dice)
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=2, phrase_time_limit=2)

        try:
            recognized_text = r.recognize_google(audio, language='fa')
            if recognized_text == "سلام":
                roll_dice_button_action()
                print("Dice rolled!")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand audio.")
        except sr.RequestError as e:
            print("Sorry, I couldn't request results from the speech recognition service. Error:", str(e))

    window.fill((255, 255, 255))
    draw_board()
    draw_players()
    dice_roll_button.draw()
    draw_game_info()

    pygame.display.flip()

pygame.quit()
