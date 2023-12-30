from .utility_algos import is_move_possible

# Flood Fill Algorithm Implementation - Iterative DFS
# Function to calculate flood-fill score from a given starting point
def flood_fill(game_state, start):
    visited = set()
    stack = [start]

    while stack:
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))

            # Explore adjacent cells (up, down, left, right)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x, next_y = x + dx, y + dy
                if is_move_possible(game_state, (next_x, next_y)):
                    stack.append((next_x, next_y))

    return len(visited)  # Return the size of the visited set, representing the connected region