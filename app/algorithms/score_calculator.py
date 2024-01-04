from .a_star_algorithm import a_star, heuristic_cost_estimate
from .flood_fill_algorithm import flood_fill
from .utility_algos import is_terminal

# ===== SCORE CALCULATOR =====
def calculate_game_state_score(game_state):
    # Check for terminal state
    if is_terminal(game_state):
        return float('-inf')

    return 1