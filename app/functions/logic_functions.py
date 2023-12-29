from algorithms import utility_algos

# ===== FINDS THE BEST MOVE FROM THE EXISTING GAME STATE =====
def find_best_move(game_state):
    best_move = ""
    return best_move

# ===== STOPS SNAKE FROM GOING OUT OF BOUNDS AND COLLIDING INTO OTHER SNAKES =====
def prevent_out_of_bounds_movements_and_collisions(game_state, is_move_safe):
    return utility_algos.get_safe_moves(game_state, is_move_safe)