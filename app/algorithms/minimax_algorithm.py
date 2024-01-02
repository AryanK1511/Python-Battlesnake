from .utility_algos import get_safe_moves, is_terminal, simulate_move, get_all_opponent_moves
from .score_calculator import calculate_game_state_score

# Minimax algorithm implementation
def minimax(game_state, depth, maximizing_player, is_move_safe, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or is_terminal(game_state):
        return calculate_game_state_score(game_state), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        safe_moves = [move for move, safe in get_safe_moves(game_state, is_move_safe, game_state['you']['id']).items() if safe]
        for move in safe_moves:
            child_game_state = simulate_move(game_state, move, game_state['you']['id'])
            eval, _ = minimax(child_game_state, depth - 1, False, is_move_safe, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for snake_id, moves in get_all_opponent_moves(game_state).items():
            for move in moves:
                child_game_state = simulate_move(game_state, move, snake_id)
                eval, _ = minimax(child_game_state, depth - 1, True, is_move_safe, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval, None



    
# game_state = {'game': {'id': 'c35159b7-6fcd-4e94-835e-06de41f94f52', 'ruleset': {'name': 'standard', 'version': 'v1.2.3', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': 'custom'}, 'turn': 3, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_pSQkWvMBWMcmXtD7crrKxDTT', 'name': 'Scared Bot', 'latency': '1', 'health': 97, 'body': [{'x': 0, 'y': 3}, {'x': 1, 'y': 3}, {'x': 1, 'y': 4}], 'head': {'x': 0, 'y': 3}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#000000', 'head': 'bendr', 'tail': 'curled'}}, {'id': 'gs_WbQMWVvFmTRwvfwxDxvH7qVP', 'name': 'Loopy Bot', 'latency': '1', 'health': 99, 'body': [{'x': 5, 'y': 0}, {'x': 4, 'y': 0}, {'x': 4, 'y': 1}, {'x': 5, 'y': 1}], 'head': {'x': 5, 'y': 0}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'caffeine', 'tail': 'iguana'}}, {'id': 'gs_TPSpJTVgCXqm4Tjy8Q3fgkvH', 'name': 'Academic Weapon (Beta)', 'latency': '413', 'health': 99, 'body': [{'x': 6, 'y': 9}, {'x': 6, 'y': 10}, {'x': 5, 'y': 10}, {'x': 5, 'y': 9}], 'head': {'x': 6, 'y': 9}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}, {'id': 'gs_fxxrPCyTxBb6HYTRdtrd93kR', 'name': 'Hungry Bot', 'latency': '1', 'health': 99, 'body': [{'x': 10, 'y': 5}, {'x': 10, 'y': 6}, {'x': 9, 'y': 6}, {'x': 9, 'y': 5}], 'head': {'x': 10, 'y': 5}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#00cc00', 'head': 'alligator', 'tail': 'alligator'}}], 'food': [{'x': 0, 'y': 6}, {'x': 5, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_TPSpJTVgCXqm4Tjy8Q3fgkvH', 'name': 'Academic Weapon (Beta)', 'latency': '413', 'health': 99, 'body': [{'x': 6, 'y': 9}, {'x': 6, 'y': 10}, {'x': 5, 'y': 10}, {'x': 5, 'y': 9}], 'head': {'x': 6, 'y': 9}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}}

# print(minimax(game_state, 4, True, {"up": False, "down": True, "left": False, "right": True}))