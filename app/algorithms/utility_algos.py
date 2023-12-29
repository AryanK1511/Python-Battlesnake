# ========== RETURNS SAFE MOVES ==========
def get_safe_moves(game_state, is_move_safe):
    my_snake_head = game_state['you']['body'][0]
    possible_moves = {
        "left": (my_snake_head['x'] - 1, my_snake_head['y']),
        "right": (my_snake_head['x'] + 1, my_snake_head['y']),
        "up": (my_snake_head['x'], my_snake_head['y'] + 1),
        "down": (my_snake_head['x'], my_snake_head['y'] - 1)
    }

    for move, coordinate in possible_moves.items():
        is_move_safe[move] = is_move_possible(game_state, coordinate)

    return is_move_safe

# ========== CHECKS TO SEE IF THE GIVEN MOVE IS NOT RESULTING IN COLLISION OR OUT FO BOUNDS SCENARIO ==========
def is_move_possible(game_state, coordinate):
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']
    x, y = coordinate

    # Check if the move is out of bounds
    if x < 0 or x >= board_width or y < 0 or y >= board_height:
        return False

    # Check for collisions with self and other snakes
    for snake in game_state["board"]["snakes"]:
        for body_part in snake["body"]:
            if body_part["x"] == x and body_part["y"] == y:
                return False

    # If the function hasn't returned False by now, the move is possible
    return True

# Normalize a value to the range [-1, 1]
def normalize(value, min_value, max_value):
    # Avoid division by zero
    if max_value - min_value == 0:
        return 0
    # First it divides to make the value between 0 and 1, then it multiplies by 2 and subtracts 1 to make it between -1 and 1
    return 2 * ((value - min_value) / (max_value - min_value)) - 1