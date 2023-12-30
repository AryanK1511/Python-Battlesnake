from .a_star_algorithm import a_star, heuristic_cost_estimate
from .flood_fill_algorithm import flood_fill

# ========== SCORES A GAME STATE BASED ON VARIOUS FACTORS ==========
def calculate_game_state_score(game_state):
    snake_head = next(s for s in game_state['board']['snakes'] if s['id'] == game_state['you']['id'])['head']
    snake_head_tuple = (snake_head['x'], snake_head['y'])

    food_items = game_state['board']['food']
    food_tuples = [(item['x'], item['y']) for item in food_items]
    closest_food = min(food_tuples, key=lambda food: heuristic_cost_estimate(snake_head_tuple, food))

    # Get the A* path length
    a_star_path = a_star(game_state, snake_head_tuple, closest_food)
    a_star_path_length = len(a_star_path) if a_star_path else 1

    # Get the Flood Fill score
    flood_fill_area = flood_fill(game_state, snake_head_tuple)

    # Weights
    path_weight = -1
    area_weight = 1

    # Calculate the score
    final_score = (path_weight * a_star_path_length) + (area_weight * flood_fill_area)

    # ===== LOGGER =====
    print("-----STATS-----")
    print("Path: " + str(a_star_path))
    print("Path Length: " + str(a_star_path_length))
    print("Area: " + str(flood_fill_area))
    print("Final Score: " + str(final_score))
    print("---------------")
    # ==================

    return final_score