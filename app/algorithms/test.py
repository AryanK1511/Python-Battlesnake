from copy import deepcopy

gs = {'game': {'id': '418e0083-877f-4781-9a5c-a432b1d1cc17', 'ruleset': {'name': 'standard', 'version': 'v1.2.3', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': 'custom'}, 'turn': 5, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_fyT8RTv7qw6DKKJYfb9fXmbS', 'name': 'Academic Weapon (Beta)', 'latency': '162', 'health': 95, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}], 'food': [{'x': 0, 'y': 6}, {'x': 5, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_fyT8RTv7qw6DKKJYfb9fXmbS', 'name': 'Academic Weapon (Beta)', 'latency': '162', 'health': 95, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fdac53', 'head': 'smart-caterpillar', 'tail': 'coffee'}}}

gs_cpy = deepcopy(gs)

gs_cpy["board"]["snakes"][0]["body"].insert(0, {"x": 12222, "y": 32})

print(gs_cpy)
print("-----")
print(gs)

print(gs["board"]["snakes"][0]["id"])