from algorithms.utility_algos import get_safe_moves
from algorithms.score_calculator import calculate_game_state_score

# ===== STOPS SNAKE FROM GOING OUT OF BOUNDS AND COLLIDING INTO OTHER SNAKES =====
def prevent_out_of_bounds_movements_and_collisions(game_state, is_move_safe):
    return get_safe_moves(game_state, is_move_safe)

# ===== FINDS THE BEST MOVE BASED ON THE GAME STATE =====
def find_best_move(game_state, is_move_safe):
    my_snake_head = game_state['you']['body'][0]
    safe_moves = [move for move, isSafe in is_move_safe.items() if isSafe]

    # Make a dictionary of all possible moves
    possible_moves = {
        "left": {'x': my_snake_head['x'] - 1, 'y': my_snake_head['y']},
        "right": {'x': my_snake_head['x'] + 1, 'y': my_snake_head['y']},
        "up": {'x': my_snake_head['x'], 'y': my_snake_head['y'] - 1},
        "down": {'x': my_snake_head['x'], 'y': my_snake_head['y'] + 1}
    }
    
    # Make a dictionary of all possible moves and their scores
    possible_moves_score = {
        "left": float('-inf'),  # Use negative infinity as initial score for unsafe moves
        "right": float('-inf'),
        "up": float('-inf'),
        "down": float('-inf')
    }

    # Calculate the score for each safe move
    for move in safe_moves:
        # Temporarily modify the game state to simulate the move
        game_state['you']['body'][0] = possible_moves[move]
        # Calculate the score for this hypothetical game state
        possible_moves_score[move] = calculate_game_state_score(game_state)
        # Revert the game state back to the original after scoring
        game_state['you']['body'][0] = my_snake_head

    # ===== LOGGER =====
    print("Possible moves score: " + str(possible_moves_score))
    # ==================

    # Find the move with the highest score
    best_move = max(possible_moves_score, key=possible_moves_score.get)

    # Return the best move
    return best_move