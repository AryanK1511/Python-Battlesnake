import random
import typing
from .logic_functions import prevent_out_of_bounds_movements_and_collisions, find_best_move

# Called at battlesnake creation
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "AryanK1511", 
        "color": "#FDAC53",  
        "head": "smart-caterpillar",  
        "tail": "coffee"
    }

# Called when game begins
def start(game_state: typing.Dict):
    print("GAME START")

# Called when game finishes
def end(game_state: typing.Dict):
    print("GAME OVER\n")

# Called on every turn
def move(game_state: typing.Dict) -> typing.Dict:
    # Returning a dictionary at the end which tells the Battlesnake what direction to move
    is_move_safe = {"up": True, "down": True, "left": True, "right": True}
    best_move = ""

    # ========== Movement manipulators ========== 
    print("\n===========================================================================")

    # ===== LOGGER =====
    print(game_state) 
    # ==================
    
    is_move_safe = prevent_out_of_bounds_movements_and_collisions(game_state, is_move_safe)
    print("Safe moves after BOUNDARY AND COLLISION PREVENTION CODE: " + str(is_move_safe))

    best_move = find_best_move(game_state, is_move_safe)
    print("BEST MOVE: " + str(best_move))

    # ===== CHECK FOR AVAILABLE SAFE MOVES =====
    safe_moves = [move for move, isSafe in is_move_safe.items() if isSafe]

    # Choose a random move from the safe ones
    if len(safe_moves) > 0:
        if best_move in safe_moves:
            next_move = best_move
        else:
            next_move = random.choice(safe_moves)
    else:
        print("No safe moves")
        next_move = "left"

    print(f"MOVE {game_state['turn']}: {next_move}")
    print("===========================================================================")
    return {"move": next_move}