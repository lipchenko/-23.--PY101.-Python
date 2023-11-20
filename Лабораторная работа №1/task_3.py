list_players = ["игрок1", "игрок2", "игрок3", "игрок4", "игрок5", "игрок6", "игрок7", "игрок8"]
middle_index = len(list_players) // 2  # 2

left_team = list_players[:middle_index]  # list_players[:2]
right_team = list_players[middle_index:]  # list_players[2:]

print(left_team)
print(right_team)


