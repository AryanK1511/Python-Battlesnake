from utility_algos import is_move_possible

# Flood Fill Algorithm Implementation
# This function will return the area that the snake can control in the specific game state provided
def flood_fill(game_state, start):
    rows, columns = game_state['board']['height'], game_state['board']['width']

    # Created a set to keep track of visited cells
    visited = set()

    # Check if the cell is safe to visit
    def is_safe(x, y):
        if 0 <= x < rows and 0 <= y < columns:
            return (x, y) not in visited and is_move_possible(game_state, (x, y))
        return False
    
    # Recursive function to perform flood fill
    def dfs(x, y):
        if not is_safe(x, y):
            return 0
        visited.add((x, y))

        # Accumulate the count of accessible cells
        return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
    
    # Return the area of that our snake controls
    return dfs(start[0], start[1])

# # ===== TESTING =====
# game_state = {'game': {'id': '8395c520-48bd-400d-86f5-40b70844e1b3', 'ruleset': {'name': 'standard', 'version': 'v1.2.3', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': 'custom'}, 'turn': 150, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_HVJ9FrPYVQQgQVp7BCK7VrHM', 'name': 'Academic Weapon', 'latency': '160', 'health': 91, 'body': [{'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 1}, 'length': 12, 'shout': '', 'squad': '', 'customizations': {'color': '#888888', 'head': 'default', 'tail': 'default'}}], 'food': [{'x': 0, 'y': 8}, {'x': 2, 'y': 6}, {'x': 0, 'y': 9}, {'x': 3, 'y': 9}, {'x': 2, 'y': 0}, {'x': 7, 'y': 1}, {'x': 1, 'y': 5}, {'x': 10, 'y': 1}, {'x': 8, 'y': 7}, {'x': 4, 'y': 9}, {'x': 9, 'y': 10}], 'hazards': []}, 'you': {'id': 'gs_HVJ9FrPYVQQgQVp7BCK7VrHM', 'name': 'Academic Weapon', 'latency': '160', 'health': 91, 'body': [{'x': 10, 'y': 4}, {'x': 10, 'y': 3}, {'x': 9, 'y': 3}, {'x': 8, 'y': 3}, {'x': 8, 'y': 4}, {'x': 9, 'y': 4}, {'x': 9, 'y': 5}, {'x': 10, 'y': 5}, {'x': 10, 'y': 6}, {'x': 10, 'y': 7}, {'x': 10, 'y': 8}, {'x': 10, 'y': 9}], 'head': {'x': 10, 'y': 4}, 'length': 12, 'shout': '', 'squad': '', 'customizations': {'color': '#888888', 'head': 'default', 'tail': 'default'}}}

# area = flood_fill(game_state, (0, 1))
# print(area)