from algorithms.utility_algos import get_safe_moves, simulate_move
from algorithms.score_calculator import calculate_game_state_score
from algorithms.minimax_algorithm import minimax

# ===== STOPS SNAKE FROM GOING OUT OF BOUNDS AND COLLIDING INTO OTHER SNAKES =====
def prevent_out_of_bounds_movements_and_collisions(game_state, is_move_safe):
    return get_safe_moves(game_state, is_move_safe)

# ===== FINDS THE BEST MOVE BASED ON MINIMAX ALGORITHM =====
def find_best_move(game_state, is_move_safe):
    score, best_move = minimax(game_state, 3, True, is_move_safe)
    return best_move