import json

players = [
    {
        "name": "Bijan Robinson",
        "games_played":4,
        "rushing_yards": 494,
        "receiving_yards": 120,
        "rushing_touchdowns": 4,
        "receiving_touchdowns": 1
    },
    {
        "name": "Drake London",
         "games_played":4,
        "rushing_yards": 4,
        "receiving_yards": 370,
        "rushing_touchdowns": 0,
        "receiving_touchdowns": 0
    },
    {
        "name": "Kyle Pitts",
         "games_played":4,
        "rushing_yards": 0,
        "receiving_yards": 67,
        "rushing_touchdowns": 0,
        "receiving_touchdowns": 0
    }
]
    
def save_players():
    with open("players.json", "w") as file:
        json.dump(players, file, indent=4)


def load_players():
    global players

    try:
        with open("players.json", "r") as file:
            players = json.load(file)

    except FileNotFoundError:
        save_players()

def view_all_stats():
    for player in players:
        total_yards = (
            player["rushing_yards"]
            + player["receiving_yards"]
        )

        total_touchdowns = (
            player["rushing_touchdowns"]
            + player["receiving_touchdowns"]
        )

        print(
            player["name"],
            "-",
            total_yards,
            "scrimmage yards,",
            total_touchdowns,
            "touchdowns"
        )


def find_highest_yards():
    highest_player = None

    for player in players:
        total_yards = (
            player["rushing_yards"]
            + player["receiving_yards"]
        )

        if highest_player is None:
            highest_player = player
            highest_yards = total_yards

        elif total_yards > highest_yards:
            highest_player = player
            highest_yards = total_yards

    print(
        highest_player["name"],
        "has the most scrimmage yards with",
        highest_yards,
        "yards."
    )
def find_highest_touchdowns():
    highest_player = None
    highest_touchdowns = 0

    for player in players:
        total_touchdowns = (
            player["rushing_touchdowns"]
            + player["receiving_touchdowns"]
        )

        if highest_player is None:
            highest_player = player
            highest_touchdowns = total_touchdowns

        elif total_touchdowns > highest_touchdowns:
            highest_player = player
            highest_touchdowns = total_touchdowns

    print(
        highest_player["name"],
        "has the most touchdowns with",
        highest_touchdowns,
        "touchdowns."
    )
def view_team_averages():
    total_yards = 0
    total_touchdowns = 0

    for player in players:
        player_yards = (
            player["rushing_yards"]
            + player["receiving_yards"]
        )

        player_touchdowns = (
            player["rushing_touchdowns"]
            + player["receiving_touchdowns"]
        )

        total_yards += player_yards
        total_touchdowns += player_touchdowns

    average_yards = total_yards / len(players)
    average_touchdowns = total_touchdowns / len(players)

    print("Average scrimmage yards:", round(average_yards, 2))
    print("Average touchdowns:", round(average_touchdowns, 2))

def find_lowest_yards():
    lowest_player = None

    for player in players:
        total_yards = (
            player["rushing_yards"]
            + player["receiving_yards"]
        )

        if lowest_player is None:
            lowest_player = player
            lowest_yards = total_yards

        elif total_yards < lowest_yards:
            lowest_player = player
            lowest_yards = total_yards

    print(
        lowest_player["name"],
        "has the lowest scrimmage yards with",
        lowest_yards,
        "yards."
    )

def find_lowest_touchdowns():
    lowest_player = None

    for player in players:
        total_touchdowns = (
            player["rushing_touchdowns"]
            + player["receiving_touchdowns"]
        )

        if lowest_player is None:
            lowest_player = player
            lowest_touchdowns = total_touchdowns

        elif total_touchdowns < lowest_touchdowns:
            lowest_player = player
            lowest_touchdowns = total_touchdowns

    print(
        lowest_player["name"],
        "has the fewest touchdowns with",
        lowest_touchdowns,
        "touchdowns."
    )
def view_stats_per_game():
    for player in players:
        total_yards = (
            player["rushing_yards"] + player["receiving_yards"]
        )

        total_touchdowns = (
            player["rushing_touchdowns"] + player["receiving_touchdowns"]
        )

        games = player["games_played"]

        if games > 0:
            yards_per_game = total_yards / games
            touchdowns_per_game = total_touchdowns / games

            print(f"\nPlayer: {player['name']}")
            print(f"Yards per game: {yards_per_game:.2f}")
            print(f"Touchdowns per game: {touchdowns_per_game:.2f}")
def find_per_game_leaders():
    highest_yards_player = None
    highest_yards_per_game = -1

    highest_touchdowns_player = None
    highest_touchdowns_per_game = -1

    for player in players:
        games = player["games_played"]

        if games <= 0:
            continue

        total_yards = player["rushing_yards"] + player["receiving_yards"]
        total_touchdowns = player["rushing_touchdowns"] + player["receiving_touchdowns"]

        yards_per_game = total_yards / games
        touchdowns_per_game = total_touchdowns / games

        if yards_per_game > highest_yards_per_game:
            highest_yards_per_game = yards_per_game
            highest_yards_player = player["name"]

        if touchdowns_per_game > highest_touchdowns_per_game:
            highest_touchdowns_per_game = touchdowns_per_game
            highest_touchdowns_player = player["name"]

    if highest_yards_player is not None:
        print("\n===== PER-GAME LEADERS =====")
        print(f"Most yards per game: {highest_yards_player} ({highest_yards_per_game:.2f})")
        print(f"Most touchdowns per game: {highest_touchdowns_player} ({highest_touchdowns_per_game:.2f})")
    else:
        print("No players have valid games played.")
def rank_players():
    ranked_players = sorted(
        players,
        key=lambda player: (
            player["rushing_yards"] + player["receiving_yards"]
        ) / player["games_played"] if player["games_played"] > 0 else 0,
        reverse=True
    )

    print("\n===== PLAYER PERFORMANCE RANKINGS =====")

    for rank, player in enumerate(ranked_players, start=1):
        games = player["games_played"]

        if games > 0:
            total_yards = player["rushing_yards"] + player["receiving_yards"]
            yards_per_game = total_yards / games
            print(f"{rank}. {player['name']} — {yards_per_game:.2f} yards/game")
        else:
            print(f"{rank}. {player['name']} — No games recorded")

def search_player():
    search_name = input("Enter player name: ").strip().lower()

    found = False

    for player in players:
        if search_name == player["name"].lower():

            total_yards = (
                player["rushing_yards"]
                + player["receiving_yards"]
            )

            total_touchdowns = (
                player["rushing_touchdowns"]
                + player["receiving_touchdowns"]
            )

            print("Player:", player["name"])
            print("Rushing yards:", player["rushing_yards"])
            print("Receiving yards:", player["receiving_yards"])
            print("Total scrimmage yards:", total_yards)
            print("Rushing touchdowns:", player["rushing_touchdowns"])
            print("Receiving touchdowns:", player["receiving_touchdowns"])
            print("Total touchdowns:", total_touchdowns)

            found = True
            break

    if not found:
        print("Player not found.")

def compare_players():
    first_name = input("Enter the first player's name: ").strip().lower()
    second_name = input("Enter the second player's name: ").strip().lower()

    first_player = None
    second_player = None

    for player in players:
        if player["name"].lower() == first_name:
            first_player = player

        elif player["name"].lower() == second_name:
            second_player = player

    if first_player is None:
        print("First player not found.")
        return

    if second_player is None:
        print("Second player not found.")
        return

    first_yards = first_player["rushing_yards"] + first_player["receiving_yards"]
    second_yards = second_player["rushing_yards"] + second_player["receiving_yards"]

    first_touchdowns = first_player["rushing_touchdowns"] + first_player["receiving_touchdowns"]
    second_touchdowns = second_player["rushing_touchdowns"] + second_player["receiving_touchdowns"]

    print("\n--- PLAYER COMPARISON ---")

    print(first_player["name"])
    print("Scrimmage yards:", first_yards)
    print("Touchdowns:", first_touchdowns)

    print()

    print(second_player["name"])
    print("Scrimmage yards:", second_yards)
    print("Touchdowns:", second_touchdowns)

    print("\n--- DIFFERENCES ---")
    print("Yard difference:", abs(first_yards - second_yards))
    print("Touchdown difference:", abs(first_touchdowns - second_touchdowns))

    if first_yards > second_yards:
        print(first_player["name"], "has more scrimmage yards.")
    elif second_yards > first_yards:
        print(second_player["name"], "has more scrimmage yards.")
    else:
        print("Both players have the same scrimmage yards.")

    if first_touchdowns > second_touchdowns:
        print(first_player["name"], "has more touchdowns.")
    elif second_touchdowns > first_touchdowns:
        print(second_player["name"], "has more touchdowns.")
    else:
        print("Both players have the same number of touchdowns.")
def add_player():
    name = input("Enter player name: ").strip()

    if not name:
        print("Player name cannot be empty.")
        return

    for player in players:
        if player["name"].lower() == name.lower():
            print("That player already exists.")
            return

    try:
        rushing_yards = int(input("Enter rushing yards: "))
        receiving_yards = int(input("Enter receiving yards: "))
        rushing_touchdowns = int(input("Enter rushing touchdowns: "))
        receiving_touchdowns = int(input("Enter receiving touchdowns: "))

        if min(
            rushing_yards,
            receiving_yards,
            rushing_touchdowns,
            receiving_touchdowns
        ) < 0:
            print("Stats cannot be negative.")
            return

    except ValueError:
        print("Please enter whole numbers for all stats.")
        return

    new_player = {
        "name": name,
        "games_played": 4,
        "rushing_yards": rushing_yards,
        "receiving_yards": receiving_yards,
        "rushing_touchdowns": rushing_touchdowns,
        "receiving_touchdowns": receiving_touchdowns
    }

    players.append(new_player)

    save_players()

    print(name, "has been added successfully!")

    
def show_menu():
    print("\n===== FOOTBALL STATS ANALYZER =====")
    print("1. View All Player Stats")
    print("2. Find Highest Yards")
    print("3. Find Highest Touchdowns")
    print("4. View Team Averages")
    print("5. Find Lowest Yards")
    print("6. Find Lowest Touchdowns")
    print("7. Search for a Player")
    print("8. Compare Two Players")
    print("9. add a new player")
    print("10. view stats per game")
    print("11. find per-game leaders")
    print("12. Rank players by yards per game")
    print("13. exit")

    choice = input("Choose an option: ")
    return choice
load_players()

while True:
    choice = show_menu()

    if choice == "1":
        view_all_stats()
    elif choice == "2":
        find_highest_yards()
    elif choice == "3":
        find_highest_touchdowns()
    elif choice == "4":
        view_team_averages()
    elif choice == "5":
        find_lowest_yards()
    elif choice == "6":
        find_lowest_touchdowns()
    elif choice == "7":
        search_player()
    elif choice == "8":
        compare_players()
    elif choice == "9":
        add_player()
    elif choice == "10":
        view_stats_per_game()
    elif choice == "11":
        find_per_game_leaders()
    elif choice == "12":
        rank_players()
    elif choice == "13":
        print("Thanks for using Football Stats Analyzer!")
        break
    else:
        print("Invalid choice. Please enter 1-10.")







       
