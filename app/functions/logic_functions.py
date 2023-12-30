from algorithms.utility_algos import get_safe_moves, simulate_move
from algorithms.score_calculator import calculate_game_state_score

# ===== STOPS SNAKE FROM GOING OUT OF BOUNDS AND COLLIDING INTO OTHER SNAKES =====
def prevent_out_of_bounds_movements_and_collisions(game_state, is_move_safe):
    return get_safe_moves(game_state, is_move_safe)

# ===== FINDS THE BEST MOVE BASED ON THE GAME STATE =====
def find_best_move(game_state, is_move_safe):
    safe_moves = [move for move, isSafe in is_move_safe.items() if isSafe]
    possible_moves_score = { move: float('-inf') for move in ["left", "right", "up", "down"] }

    for move in safe_moves:
        simulated_game_state = simulate_move(game_state, move, game_state['you']['id'])
        possible_moves_score[move] = calculate_game_state_score(simulated_game_state)
        print("********")
        print("OG GS: ")
        print(game_state)
        print("SGS: ")
        print(simulated_game_state)
        print("Move: " + move)
        print("********")

    # ===== LOGGER =====
    print("Possible moves score: " + str(possible_moves_score))
    # ==================

    # Find the move with the highest score
    best_move = max(possible_moves_score, key=possible_moves_score.get)

    # Return the best move
    return best_move