def draw_players():
    if player1_position > 0:
        start_x, start_y = board_x + 25, board_y + image_height - 25
        x_key = f'x{player1_position}_1'
        y_key = f'y{player1_position}_1'
        player1_x = get_Positions().get(x_key)
        player1_y = get_Positions().get(y_key)
        pygame.draw.circle(window, (255, 0, 0), (player1_x, player1_y), 13)

    if player2_position > 0:
        start_x, start_y = board_x + 25, board_y + image_height - 25
        x_key = f'x{player2_position}_1'
        y_key = f'y{player2_position}_1'
        player2_x = get_Positions().get(x_key)
        player2_y = get_Positions().get(y_key)
        pygame.draw.circle(window, (0, 255, 0), (player2_x, player2_y), 13)