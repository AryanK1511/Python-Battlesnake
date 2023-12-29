# from utility_algos import get_safe_moves, is_terminal, simulate_move
# from score_calculator import calculate_game_state_score

# # Minimax algorithm implementation
# def minimax(game_state, depth, maximizing_player):
#     # If we reach the terminal state, we score the game_state
#     if depth == 0 or is_terminal(game_state):
#         return calculate_game_state_score(game_state)
    
#     if maximizing_player:
#         max_eval = float('-inf')
#         for move in get_safe_moves(game_state): # Move can be up, down, left, right
#             my_snake_head = game_state['you']['body'][0]
#             child_game_state = simulate_move(my_snake_head, move)
#             eval = minimax(child_game_state, depth - 1, False)
#             max_eval = max(max_eval, eval)
#         return max_eval
#     else:
#         min_eval = float('inf')
#         for move in get_safe_moves(game_state):
#             child_game_state = simulate_move(game_state, move)
#             eval = minimax(child_game_state, depth - 1, True)
#             min_eval = min(min_eval, eval)
#         return min_eval
    
