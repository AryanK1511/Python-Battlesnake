# ===== STOPS SNAKE FROM GOING OUT OF BOUNDS =====
def prevent_out_of_bounds_movement(game_state, is_move_safe):
    my_head = game_state["you"]["body"][0]  
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']

    # The snake does not go outside from left or right
    if my_head["x"] <= 0:
        is_move_safe["left"] = False
    if my_head["x"] >= board_width - 1:
        is_move_safe["right"] = False
    # The snake does not go outside from top or bottom
    if my_head["y"] <= 0:
        is_move_safe["down"] = False
    if my_head["y"] >= board_height - 1:
        is_move_safe["up"] = False

    return is_move_safe

# ===== STOPS SNAKE FROM COLLIDING WITH OTHER SNAKES AND ITSELF =====
def prevent_collisions(game_state, is_move_safe):
    my_head = game_state["you"]["body"][0]  
    my_tail = game_state["you"]["body"][-1]
    
    for snake in game_state["board"]["snakes"]:
        for body_part in snake["body"]:
            # To prevent horizontal collsions
            if body_part["x"] == my_head["x"] - 1 and body_part["y"] == my_head["y"]:
                if body_part != my_tail: is_move_safe["left"] = False
            if body_part["x"] == my_head["x"] + 1 and body_part["y"] == my_head["y"]:
                if body_part != my_tail: is_move_safe["right"] = False
            # To prevent vertical collisions
            if body_part["y"] == my_head["y"] + 1 and body_part["x"] == my_head["x"]:
                if body_part != my_tail: is_move_safe["up"] = False
            if body_part["y"] == my_head["y"] - 1 and body_part["x"] == my_head["x"]:
                if body_part != my_tail: is_move_safe["down"] = False

    return is_move_safe