from algorithms.utility_algos import get_safe_moves, simulate_move
from algorithms.score_calculator import calculate_game_state_score
from algorithms.minimax_algorithm import minimax
from copy import deepcopy

# ===== STOPS SNAKE FROM GOING OUT OF BOUNDS AND COLLIDING INTO OTHER SNAKES =====
def prevent_out_of_bounds_movements_and_collisions(game_state, is_move_safe):
    return get_safe_moves(game_state, is_move_safe)

# ===== FINDS THE BEST MOVE BASED ON MINIMAX ALGORITHM =====
def find_best_move(game_state, is_move_safe_dict):
    best_move = None
    best_score = float('-inf')
    is_move_safe = deepcopy(is_move_safe_dict)
    
    # Then, we iterate through these moves, apply minimax, and choose the best
    for move, is_safe in is_move_safe.items():
        if is_safe:
            # Simulate the move to generate a new game state
            new_game_state = simulate_move(game_state, move, game_state['you']['id'])
            # Apply the minimax algorithm to the new game state
            score = minimax(new_game_state, 4, False, is_move_safe)
              # Depth is set to 2 for this example
            
            print("=======:", move, score)

            # If the score for this move is better than the best found so far, we update our best move
            if score > best_score:
                best_score = score
                best_move = move

    return best_move

# gs = {'game': {'id': 'bd8f00a4-edb7-467c-81b6-32e68fd08f95', 'ruleset': {'name': 'standard', 'version': 'v1.2.3', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': 'custom'}, 'turn': 118, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_BQM3VxR4rKFSyY6CSRvk4DpB', 'name': 'Academic Weapon (Beta)', 'latency': '195', 'health': 6, 'body': [{'x': 0, 'y': 6}, {'x': 1, 'y': 6}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}], 'head': {'x': 0, 'y': 6}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#ffffff', 'head': 'smart-caterpillar', 'tail': 'coffee'}}, {'id': 'gs_vrCYYCRYtCgP7P3M8DRmg66c', 'name': 'The Battlesnake Project', 'latency': '32', 'health': 95, 'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 9}, {'x': 3, 'y': 9}, {'x': 3, 'y': 10}, {'x': 2, 'y': 10}, {'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}, {'x': 2, 'y': 7}, {'x': 3, 'y': 7}, {'x': 3, 'y': 6}, {'x': 3, 'y': 5}, {'x': 3, 'y': 4}, {'x': 4, 'y': 4}, {'x': 5, 'y': 4}, {'x': 6, 'y': 4}, {'x': 7, 'y': 4}, {'x': 7, 'y': 3}, {'x': 8, 'y': 3}, {'x': 9, 'y': 3}], 'head': {'x': 2, 'y': 8}, 'length': 21, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}], 'food': [{'x': 9, 'y': 6}, {'x': 1, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_BQM3VxR4rKFSyY6CSRvk4DpB', 'name': 'Academic Weapon (Beta)', 'latency': '195', 'health': 6, 'body': [{'x': 0, 'y': 6}, {'x': 1, 'y': 6}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}], 'head': {'x': 0, 'y': 6}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#ffffff', 'head': 'smart-caterpillar', 'tail': 'coffee'}}}

# print(find_best_move(gs, {'left': False, 'right': False, 'up': True, 'down': True}))