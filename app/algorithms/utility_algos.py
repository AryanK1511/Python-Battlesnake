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
    if new_head in [food for food in game_state_copy['board']['food']]:
        # If food is eaten, increase the health of the snake and remove that food from the board
        snake['health'] = 100  # Assuming full health is restored on eating food
        game_state_copy['board']['food'].remove(new_head)
    else:
        # If no food eaten, reduce the health and remove the last segment of the snake's body
        snake['health'] -= 1  # Assuming health decreases by 1 for each move
        snake['body'].pop()

    # Update the "you" part of the game state if it's our snake
    if snake_id == game_state['you']['id']:
        game_state_copy['you'] = snake

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
    # Retrieve our snake's information
    our_snake = next(s for s in game_state['board']['snakes'] if s['id'] == game_state['you']['id'])

    # Check if our snake's health is zero
    if our_snake['health'] <= 0:
        return True

    # Check if our snake has no body parts remaining, indicating it has died
    if not our_snake['body']:
        return True

    # Check if our snake's head is in a collision with walls or other snakes
    head = our_snake['body'][0]
    # Check for wall collisions
    if head['x'] < 0 or head['x'] >= game_state['board']['width'] or head['y'] < 0 or head['y'] >= game_state['board']['height']:
        return True

    # Check for collisions with all snakes (including our own body)
    for snake in game_state['board']['snakes']:
        for segment in snake['body']:
            if head['x'] == segment['x'] and head['y'] == segment['y']:
                # If the collision is with our own head, it's not a terminal state
                if segment == head and snake['id'] == our_snake['id']:
                    continue
                return True

    # If none of the terminal conditions are met, return False
    return False


# ========== GETS ALL POSSIBLE MOVES OF THE OPPONENTS ==========
def get_all_opponent_moves(game_state):
    opponent_moves = {}
    for snake in game_state['board']['snakes']:
        if snake['id'] != game_state['you']['id']:
            # Assume each opponent snake can move in four directions
            opponent_moves[snake['id']] = ['up', 'down', 'left', 'right']
    return opponent_moves