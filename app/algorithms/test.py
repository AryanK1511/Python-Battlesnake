from copy import deepcopy

gs = {'game': {'id': '418e0083-877f-4781-9a5c-a432b1d1cc17', 'ruleset': {'name': 'standard', 'version': 'v1.2.3', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': 'custom'}, 'turn': 5, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_fyT8RTv7qw6DKKJYfb9fXmbS', 'name': 'Academic Weapon (Beta)', 'latency': '162', 'health': 95, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}], 'food': [{'x': 0, 'y': 6}, {'x': 5, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_fyT8RTv7qw6DKKJYfb9fXmbS', 'name': 'Academic Weapon (Beta)', 'latency': '162', 'health': 95, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}}

gs_cpy = deepcopy(gs)

gs_cpy["board"]["snakes"][0]["body"].insert(0, {"x": 12222, "y": 32})

print(gs_cpy)
print("-----")
print(gs)

print(gs["board"]["snakes"][0]["id"])

# ===== TESTING =====
# is_move_safe = {"up": True, "down": True, "left": True, "right": False}

# game_state = {'game': {'id': '175781f0-04c2-44f1-bdc7-661a1be68361', 'ruleset': {'name': 'standard', 'version': 'v1.2.3', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': 'custom'}, 'turn': 15, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_8dXMgjjh63BWBTvYmf4QXHKK', 'name': 'Academic Weapon (Beta)', 'latency': '167', 'health': 97, 'body': [{'x': 8, 'y': 7}, {'x': 9, 'y': 7}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}], 'head': {'x': 8, 'y': 7}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}, {'id': 'gs_Gh669dXMSvWptHk4qpkjbfrB', 'name': 'Hungry Bot', 'latency': '1', 'health': 95, 'body': [{'x': 4, 'y': 5}, {'x': 3, 'y': 5}, {'x': 2, 'y': 5}, {'x': 1, 'y': 5}, {'x': 0, 'y': 5}, {'x': 0, 'y': 4}], 'head': {'x': 4, 'y': 5}, 'length': 6, 'shout': '', 'squad': '', 'customizations': {'color': '#00cc00', 'head': 'alligator', 'tail': 'alligator'}}, {'id': 'gs_vWDfpx6T78qQgHHhTjdqhxKd', 'name': 'Scared Bot', 'latency': '1', 'health': 85, 'body': [{'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 7, 'y': 2}], 'head': {'x': 6, 'y': 1}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#000000', 'head': 'bendr', 'tail': 'curled'}}], 'food': [{'x': 5, 'y': 5}, {'x': 4, 'y': 1}], 'hazards': []}, 'you': {'id': 'gs_8dXMgjjh63BWBTvYmf4QXHKK', 'name': 'Academic Weapon (Beta)', 'latency': '167', 'health': 97, 'body': [{'x': 8, 'y': 7}, {'x': 9, 'y': 7}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}], 'head': {'x': 8, 'y': 7}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}}

# print(a_star(game_state, (1, 1), (4, 4)))