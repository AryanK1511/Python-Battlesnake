from .a_star_algorithm import a_star, heuristic_cost_estimate
from .flood_fill_algorithm import flood_fill

# ========== SCORES A GAME STATE BASED ON VARIOUS FACTORS ==========
def calculate_game_state_score(game_state):
    # Get the snake head
    snake = next(s for s in game_state['board']['snakes'] if s['id'] == game_state['you']['id'])
    snake_head = snake['body'][0]  # The first part of the snake's body is its head
    snake_head_tuple = (snake_head['x'], snake_head['y'])

    # Get the closest food
    food_items = game_state['board']['food']
    food_tuples = [(item['x'], item['y']) for item in food_items]
    closest_food = min(food_tuples, key=lambda food: heuristic_cost_estimate(snake_head_tuple, food))

    # Get the A* path length
    a_star_path = a_star(game_state, snake_head_tuple, closest_food)
    a_star_path_length = len(a_star_path) if a_star_path else 0

    # Get the Flood Fill score and see the area that the snake controls
    flood_fill_area = flood_fill(game_state, snake_head_tuple)

    # Snake's current health
    snake_health = snake['health']

    # Determine weights
    health_threshold = 15
    if snake_health < health_threshold:
        food_weight = 50  # High weight to prioritize food when health is low
        area_weight = 10   # Lower area weight when in survival mode
        path_weight = 2     # Lower weight as longer paths are less desirable
    else:
        food_weight = 1  # Default weight for food
        path_weight = 0     # Lower weight as longer paths are less desirable
        area_weight = 10   # Higher weight to prioritize controlling area

    # Normalize scores
    max_area = game_state['board']['width'] * game_state['board']['height']
    normalized_area = flood_fill_area / max_area
    normalized_food_distance = 1 - (a_star_path_length / (game_state['board']['width'] + game_state['board']['height']))

    # Combine scores with weights
    final_score = (
        (food_weight * normalized_food_distance) + 
        (area_weight * normalized_area) -
        (path_weight * a_star_path_length)
    )

    # ===== LOGGER =====
    print("-----STATS-----")
    print("Path: " + str(a_star_path))
    print("Path Length: " + str(a_star_path_length))
    print("Area: " + str(flood_fill_area))
    print("Final Score: " + str(final_score))
    print("---------------")
    # ==================

    return final_score