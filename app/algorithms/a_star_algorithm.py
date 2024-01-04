from .utility_algos import is_move_possible
import heapq

# Calculate Manhattan Distance between the current position and the goal (Distance Formula)
def heuristic_cost_estimate(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# Implementation of the A* algorithm
# This function will return an array of tuples that will outline the path from the start node to the target node
def a_star(game_state, start, goal):
    rows, columns = game_state['board']['height'], game_state['board']['width']
    open_set = [(0, start)] # Initialize the open set with the start node, using a min-heap for efficient retrieval of the node with the lowest cost
    came_from = {} # Dictionary to keep track of the path taken
    cheapest_path_from_start = {start: 0} # Dictionary storing the cost of the cheapest path from the start node to the current node
    total_cost_from_start = {start: heuristic_cost_estimate(start, goal)} # Dictionary storing the estimated total cost from the start node to the goal through the current node

    while open_set:
        # Pop the node with the lowest total score from the open set
        current_total_cost_from_start, current_node = heapq.heappop(open_set)

        # If the current node is the goal, reconstruct and return the path
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)

            # ===== LOGGER =====
            # print("A* Path: ", path[::-1])
            # ==================s

            return path[::-1]  # Reversed path from start to goal

        # Explore the neighbors of the current node
        for neighbour in [(current_node[0] + 1, current_node[1]), 
                          (current_node[0] - 1, current_node[1]), 
                          (current_node[0], current_node[1] + 1), 
                          (current_node[0], current_node[1] - 1)]:
            # Check if the neighbor is within the grid and if the move is possible (safe)
            if 0 <= neighbour[0] < rows and 0 <= neighbour[1] < columns and is_move_possible(game_state, neighbour):
                # Calculate the cost from the start node to the neighbor through the current node
                tentative_cheapest_path_from_start = cheapest_path_from_start[current_node] + 1
                
                # If the path to this neighbor is the shortest found so far
                if neighbour not in cheapest_path_from_start or tentative_cheapest_path_from_start < cheapest_path_from_start[neighbour]:
                    # Update the path and the costs
                    came_from[neighbour] = current_node
                    cheapest_path_from_start[neighbour] = tentative_cheapest_path_from_start
                    total_cost_from_start[neighbour] = tentative_cheapest_path_from_start + heuristic_cost_estimate(neighbour, goal)
                    # Add the neighbor to the open set
                    heapq.heappush(open_set, (total_cost_from_start[neighbour], neighbour))

    # If the goal is not reachable, return None
    return None 