from .utility_algos import get_safe_moves, is_terminal, simulate_move, get_all_opponent_moves
from .score_calculator import calculate_game_state_score
from copy import deepcopy
from collections import deque

# Maintain a history of positions to penalize repetition
position_history = deque(maxlen=10)  # Adjust maxlen to how far back you want to remember

def minimax(game_state, depth, maximizing_player, is_move_safe, alpha=float('-inf'), beta=float('inf'), move_history=[]):
    # Deep copy the safe moves dictionary to avoid modifying the original during recursion
    minimax_move_safe = deepcopy(is_move_safe)

    # Check if we have reached the maximum depth or a terminal state of the game
    if depth == 0 or is_terminal(game_state):
        # Calculate and return the score of the current game state
        score = calculate_game_state_score(game_state)
        # print("Score: ", score, "Move History: ", move_history)
        return score

    # If it's the maximizing player's turn (our snake)
    if maximizing_player or len(game_state['board']['snakes']) == 1:
        # Initialize the best score seen so far to negative infinity
        max_eval = float('-inf')

        # Get a list of safe moves for the maximizing player
        safe_moves = [move for move, safe in get_safe_moves(game_state, is_move_safe, game_state['you']['id']).items() if safe]

        # Iterate over all safe moves
        for move in safe_moves:
            # Simulate the move and get the resulting game state
            child_game_state = simulate_move(game_state, move, game_state['you']['id'])
            # Recursively call minimax for the child game state, reducing the depth
            eval = minimax(child_game_state, depth - 1, False, minimax_move_safe, alpha, beta, move_history + [move])

            # Update max_eval with the maximum score seen so far
            max_eval = max(max_eval, eval)
            # Update alpha (the best score the maximizer can guarantee at current level or above)
            alpha = max(alpha, eval)
            # Alpha-beta pruning: stop evaluating if alpha is greater than or equal to beta
            if beta <= alpha:
                break

        return max_eval
    else:  # If it's the minimizing player's turn (opponent snake)
        # Initialize the best score seen so far to positive infinity
        min_eval = float('inf')

        # Get all possible moves for the opponent snakes
        opponent_moves = get_all_opponent_moves(game_state)

        # Iterate over each opponent snake and their possible moves
        for snake_id, moves in opponent_moves.items():
            for move in moves:
                # Simulate each move and get the resulting game state
                child_game_state = simulate_move(game_state, move, snake_id)
                # Recursively call minimax for the child game state, reducing the depth
                eval = minimax(child_game_state, depth - 1, True, minimax_move_safe, alpha, beta, move_history + [move])

                # Update min_eval with the minimum score seen so far
                min_eval = min(min_eval, eval)
                # Update beta (the best score the minimizer can guarantee at current level or above)
                beta = min(beta, eval)
                # Alpha-beta pruning: stop evaluating if beta is less than or equal to alpha
                if beta <= alpha:
                    break

        return min_eval
