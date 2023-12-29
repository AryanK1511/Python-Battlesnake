from utility_algos import get_safe_moves
import heapq

def heuristic_cost_estimate(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def a_star(game_state, start, goal, is_move_safe):
    rows, columns = game_state['board']['height'], game_state['board']['width']
    open_set = [(0, start)]
    came_from = {}
    cheapest_path_from_start = {start: 0}
    total_cost_from_start = {start: heuristic_cost_estimate(start, goal)}

    while open_set:
        # Get the safe moves for our battlesnake
        safe_move_coordinates = get_safe_moves(game_state, is_move_safe)

        current_total_cost_from_start, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]
        
        for neighbour in [(current_node[0] + 1, current_node[1]), (current_node[0] - 1, current_node[1]), (current_node[0], current_node[1] + 1), (current_node[0], current_node[1] - 1)]:
            if 0 <= neighbour[0] < rows and 0 <= neighbour[1] < columns:
                tentative_cheapest_path_from_start = cheapest_path_from_start[current_node] + 1
                if neighbour not in cheapest_path_from_start or tentative_cheapest_path_from_start < cheapest_path_from_start[neighbour]:
                    came_from[neighbour] = current_node
                    cheapest_path_from_start[neighbour] = tentative_cheapest_path_from_start
                    total_cost_from_start[neighbour] = tentative_cheapest_path_from_start + heuristic_cost_estimate(neighbour, goal)
                    heapq.heappush(open_set, (total_cost_from_start[neighbour], neighbour))

    return None  # Moved outside the while loop
    
# ===== TESTING =====
is_move_safe = {"up": True, "down": True, "left": True, "right": True}

game_state = {'game': {'id': '8395c520-48bd-400d-86f5-40b70844e1b3', 'ruleset': {'name': 'standard', 'version': 'v1.2.3', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': 'custom'}, 'turn': 150, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_HVJ9FrPYVQQgQVp7BCK7VrHM', 'name': 'Academic Weapon', 'latency': '160', 'health': 91, 'body': [{'x': 10, 'y': 4}, {'x': 10, 'y': 3}, {'x': 9, 'y': 3}, {'x': 8, 'y': 3}, {'x': 8, 'y': 4}, {'x': 9, 'y': 4}, {'x': 9, 'y': 5}, {'x': 10, 'y': 5}, {'x': 10, 'y': 6}, {'x': 10, 'y': 7}, {'x': 10, 'y': 8}, {'x': 10, 'y': 9}], 'head': {'x': 10, 'y': 4}, 'length': 12, 'shout': '', 'squad': '', 'customizations': {'color': '#888888', 'head': 'default', 'tail': 'default'}}], 'food': [{'x': 0, 'y': 8}, {'x': 2, 'y': 6}, {'x': 0, 'y': 9}, {'x': 3, 'y': 9}, {'x': 2, 'y': 0}, {'x': 7, 'y': 1}, {'x': 1, 'y': 5}, {'x': 10, 'y': 1}, {'x': 8, 'y': 7}, {'x': 4, 'y': 9}, {'x': 9, 'y': 10}], 'hazards': []}, 'you': {'id': 'gs_HVJ9FrPYVQQgQVp7BCK7VrHM', 'name': 'Academic Weapon', 'latency': '160', 'health': 91, 'body': [{'x': 10, 'y': 4}, {'x': 10, 'y': 3}, {'x': 9, 'y': 3}, {'x': 8, 'y': 3}, {'x': 8, 'y': 4}, {'x': 9, 'y': 4}, {'x': 9, 'y': 5}, {'x': 10, 'y': 5}, {'x': 10, 'y': 6}, {'x': 10, 'y': 7}, {'x': 10, 'y': 8}, {'x': 10, 'y': 9}], 'head': {'x': 10, 'y': 4}, 'length': 12, 'shout': '', 'squad': '', 'customizations': {'color': '#888888', 'head': 'default', 'tail': 'default'}}}

print(a_star(game_state, (1, 1), (4, 4), is_move_safe))