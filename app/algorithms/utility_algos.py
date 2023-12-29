from copy import deepcopy

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

# ========== RETURNS SAFE MOVES ==========
def get_safe_moves(game_state, is_move_safe, snake_id = None):

    for move in ["left", "right", "up", "down"]:
        simulated_game_state = simulate_move(game_state, move, snake_id or game_state['you']['id'])

        # If the snake_id is not provided, assume it is the snake of the player
        # If the snake_id is provided, assume it is the snake of the opponent. The next() function will return the first element of the list that satisfies the condition
        new_head = next(s['body'][0] for s in simulated_game_state['board']['snakes'] if s['id'] == simulated_game_state['you']['id']) if not snake_id else next(s['body'][0] for s in simulated_game_state['board']['snakes'] if s['id'] == snake_id)

        is_move_safe[move] = is_move_possible(game_state, (new_head['x'], new_head['y']))

    return is_move_safe

# ========== FINDS THE SNAKE IDS OF THE OPPONENTS ==========
def get_opponent_snake_ids(game_state):
    opponent_snake_ids = []
    for snake in game_state['board']['snakes']:
        if snake['id'] != game_state['you']['id']:
            opponent_snake_ids.append(snake['id'])
    return opponent_snake_ids

# ========== SIMULATES A SNAKE MOVE ==========
def simulate_move(game_state, move, snake_id):
    game_state_copy = deepcopy(game_state) 

    # Get the snake and its head
    snake = next(s for s in game_state_copy['board']['snakes'] if s['id'] == snake_id)
    new_head = simulate_head_move(snake['body'][0], move)

    # Update the snake's body
    snake['body'].insert(0, new_head)

    # Check to see whether the snake was able to grow in size after eating food
    if new_head not in game_state_copy['board']['food']:
        snake['body'].pop()  # Assume no food eaten

    # Update the game state with the new snake position
    return game_state_copy

# ========== SIMULATES A SNAKE HEAD MOVE ==========
def simulate_head_move(snake_head, move):
    # Extract the current position
    x, y = snake_head['x'], snake_head['y']

    # Update the position based on the move
    if move == 'left':
        x -= 1
    elif move == 'right':
        x += 1
    elif move == 'up':
        y += 1
    elif move == 'down':
        y -= 1

    # Return the new position as a tuple
    return {'x': x, 'y': y}

# ========== CHECKS IF THE GAME STATE IS A TERMINAL STATE ==========
def is_terminal(game_state):
    my_snake = game_state['you']
    # Check for zero health or if the snake has no body parts
    return my_snake['health'] <= 0 or not my_snake['body']

# ========== Normalize a value to the range [-1, 1] ==========
def normalize(value, min_value, max_value):
    # Avoid division by zero
    if max_value - min_value == 0:
        return 0
    # First it divides to make the value between 0 and 1, then it multiplies by 2 and subtracts 1 to make it between -1 and 1
    return 2 * ((value - min_value) / (max_value - min_value)) - 1

gs = {'game': {'id': '418e0083-877f-4781-9a5c-a432b1d1cc17', 'ruleset': {'name': 'standard', 'version': 'v1.2.3', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': 'custom'}, 'turn': 5, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_fyT8RTv7qw6DKKJYfb9fXmbS', 'name': 'Academic Weapon (Beta)', 'latency': '162', 'health': 95, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}], 'food': [{'x': 0, 'y': 6}, {'x': 5, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_fyT8RTv7qw6DKKJYfb9fXmbS', 'name': 'Academic Weapon (Beta)', 'latency': '162', 'health': 95, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}}

print(get_safe_moves(gs, {"up": True, "down": True, "left": True, "right": True}))