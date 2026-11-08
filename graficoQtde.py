import requests
import pandas as pd
import matplotlib.pyplot as plt

username = "pedro0250631"  # My personal username
headers = {"User-Agent": "MyChessGraph/1.0 (contact: your_email@example.com)"}

archives_url = f"https://api.chess.com/pub/player/{username}/games/archives"
response = requests.get(archives_url, headers=headers).json()
archives = response.get("archives", [])

games_data = []

print(f"Total months found: {len(archives)}")

for index, archive in enumerate(archives, 1):
    print(f"Processing month {index}/{len(archives)}...")

    res = requests.get(archive, headers=headers).json()

    for game in res.get("games", []):
        if game.get("time_class") == "bullet":
            is_white = game["white"]["username"].lower() == username.lower()
            player_info = game["white"] if is_white else game["black"]

            games_data.append({
                "end_time": game["end_time"],
                "rating": player_info["rating"]
            })

if games_data:
    df = pd.DataFrame(games_data).sort_values("end_time").reset_index(drop=True)

    df["game_number"] = range(1, len(df) + 1)

    plt.figure(figsize=(12, 6))

    plt.plot(df["game_number"], df["rating"], color="#7fa650", linewidth=1)

    plt.title(f"Rating Progression by Game (Bullet) - {username}")
    plt.xlabel("Number of Games Played")
    plt.ylabel("Rating")
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()
else:
    print("No games found for the selected time control.")
