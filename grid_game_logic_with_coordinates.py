import random

grid_size = int(input("Enter the Grid size: "))
WIN_SIZE = grid_size * grid_size
print(f"Winning Postion is: {WIN_SIZE}")
player_count = 3

winner_flag = True

GAME_LOG = [{
    "player_name": "player 1",
    "dice_roll_history" : [],
    "position_history" : [],
    "coordinate_history": [],
    "winner_status": ""
    },
    {
    "player_name": "player 2",
    "dice_roll_history" : [],
    "position_history" : [],
    "coordinate_history": [],
    "winner_status": ""
    },
    {
    "player_name": "player 3",
    "dice_roll_history" : [],
    "position_history" : [],
    "coordinate_history" :[],
    "winner_status": ""
    }
]
coordinate_map = {}
for i in range(grid_size*grid_size):
    x = i%grid_size
    y = i // grid_size
    #print(f" {i+1} -> {x, y}")
    if y % 2 != 0:
        odd_index = True
        x = dec
        dec -= 1
        #print(f" {i + 1} -> {x, y}")
    else:
        dec = grid_size - 1
    print(f" {i + 1} -> {x, y}")
    coordinate_map[i+1] = (x,y)




player_turn = 0
while winner_flag:
    if player_turn > 2:
        player_turn = 0
    print(f"Player {player_turn + 1 } turns...")
    dice_result = random.choice(range(1,7))
    print(f"Dice Result: {dice_result}")
    GAME_LOG[player_turn]['dice_roll_history'].append(dice_result)

    if len(GAME_LOG[player_turn]['position_history']) < 1:
        position = dice_result
        GAME_LOG[player_turn]['position_history'].append(position)
        GAME_LOG[player_turn]['coordinate_history'].append(coordinate_map[position])
    else:
        position = GAME_LOG[player_turn]['position_history'][-1] + dice_result
        #GAME_LOG[player_turn]['coordinate_history'].append(coordinate_map[position])
        if position > WIN_SIZE:
            print(f"Invalid Dice Roll: {dice_result}")
            position = GAME_LOG[player_turn]['position_history'][-1]
            GAME_LOG[player_turn]['coordinate_history'].append(coordinate_map[position])
            #print(f"player{player_turn} \n {GAME_LOG[player_turn]['position_history']}")
        GAME_LOG[player_turn]['position_history'].append(position)
        GAME_LOG[player_turn]['coordinate_history'].append(coordinate_map[position])

    if GAME_LOG[player_turn]['position_history'][-1] == WIN_SIZE:
        GAME_LOG[player_turn]['winner_status'] = "Winner"
        winner_flag = False
    """
    Eliminate Logic
    """
    for player in range(3):
        if player == player_turn:
            continue
        if len(GAME_LOG[player]['position_history']) == 0:
            continue

        if position == GAME_LOG[player]['position_history'][-1]:
            print(f"Player {player_turn +1} eliminated player {player+1} at position {position}")
            GAME_LOG[player]['position_history'].append(0)
            GAME_LOG[player]['coordinate_history'].append((-1,-1))


    print(f"Dice History: {GAME_LOG[player_turn]['dice_roll_history']}")
    print(f"Position History: {GAME_LOG[player_turn]['position_history']}")
    player_turn += 1

print("==GAME LOG==")
print(GAME_LOG)












