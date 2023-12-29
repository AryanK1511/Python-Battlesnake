from .a_star_algorithm import a_star, heuristic_cost_estimate
from .flood_fill_algorithm import flood_fill
from.utility_algos import normalize

# ========== SCORES A GAME STATE BASED ON VARIOUS FACTORS ==========
def calculate_game_state_score(game_state):
    # Defining the maximum possible values for A* and Flood Fill
    max_path_length = game_state['board']['width'] * game_state['board']['height']
    max_area = max_path_length

    # Get the coordinates of the closeset food item
    snake_head = game_state['you']['body'][0]
    food_items = game_state['board']['food']

    # Converting the list of dictionaries to a list of tuples
    food_tuples = [(item['x'], item['y']) for item in food_items]

    # Converting the single dictionary to a tuple
    snake_head_tuple = (snake_head['x'], snake_head['y'])

    closest_food = min(food_tuples, key=lambda food: heuristic_cost_estimate(snake_head_tuple, food))

    # Get the A* path length
    a_star_path = a_star(game_state, snake_head_tuple, closest_food)
    a_star_path_length = len(a_star_path) if a_star_path else max_path_length

    # Get the Flood Fill area
    flood_fill_area = flood_fill(game_state, snake_head_tuple)

    # Normalize the scores
    # normalized_path_length = normalize(a_star_path_length, 0, max_path_length)
    # normalized_area = normalize(flood_fill_area, 0, max_area)

    # Weights
    path_weight = 0.4
    area_weight = 0.6

    # Calculate the score
    final_score = (path_weight * a_star_path_length) + (area_weight * flood_fill_area)

    print("-----STATS-----")
    print("Path: " + str(a_star_path))
    print("Path Length: " + str(a_star_path_length))
    print("Area: " + str(flood_fill_area))
    print("Final Score: " + str(final_score))
    print("---------------")

    # Clamp final score between -1 and 1
    # final_score = max(-1, min(final_score, 1))

    return final_score