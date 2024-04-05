import random

# List of golf courses
def get_course():
    golf_courses = [
        "Big Spring Country Club",
        "Woodhaven Country Club",
        "Oxmoor Country Club",
        "Crescent Hill Golf Course",
        "Shelby County Country Club",
        "Oldham County Country Club",
        "Polo Fields",
        "Lake Forest",
        "Persimmon Ridge",
    ]
    selected_course = random.choice(golf_courses)
    print(f"You will play at: {selected_course}")

# List of four players (you can replace with actual player names)
def get_players():
    player1 = str(input("First players name: "))
    player2 = str(input("Second players name: "))
    player3 = str(input("Third players name: "))
    player4 = str(input("Fourth players name: "))
    
    players = [player1, player2, player3, player4]
    random.shuffle(players)
    pairs = [(players[i], players[i + 1]) for i in range(0, len(players), 2)]
    for pair in pairs:
        print(f"Pair: {pair[0]} vs {pair[1]}")

# Print the results
if __name__ == "__main__":
    get_players()
    get_course()