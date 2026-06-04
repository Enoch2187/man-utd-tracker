


import requests
import matplotlib.pyplot as plt

from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4"

headers = {
    "X-Auth-Token": API_KEY
}

def get_cumulative_points(season):
    """ Fetches  Manchester United's matches for a given season,
    calculates cumulative points match by match,
    and returns the list running totals
    """
    response = requests.get(
    f"{BASE_URL}/teams/66/matches",
        headers=headers,
        params={
            "season": season,
            "status": "FINISHED"
        }
    )

    data = response.json()
    matches = data["matches"]

    cumulative_points = []
    total_points = 0

    for  match in matches:
        home_team = match["homeTeam"]["name"]
        home_score = match["score"]["fullTime"]["home"]
        away_score = match["score"]["fullTime"]["away"]

        if home_team == "Manchester United FC":
            united_score = home_score
            united_conceded = away_score
        else:
            united_score = away_score
            united_conceded = home_score

        if united_score > united_conceded:
            total_points += 3
        elif united_score == united_conceded:
            total_points += 1

        cumulative_points.append(total_points)

    return cumulative_points


seasons = [2023, 2024]
colors = ["green","red"]

plt.figure(figsize =(12,6))

for season, color in zip(seasons, colors):
    points = get_cumulative_points(season)
    match_numbers = list(range(1,len(points) + 1))
    plt.plot(
        match_numbers,
        points,
        color = color,
        linewidth = 2,
        marker = "o",
        markersize = 4,
        label = f"{season}/{str(season + 1)[-2:]}"
    )
    plt.title("Manchester United - Season Comparison", fontsize = 14)
    plt.xlabel("Match Number")
    plt.ylabel("Cumulative Points")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
plt.show()