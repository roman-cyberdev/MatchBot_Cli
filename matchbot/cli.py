import argparse
from matchbot.api import fetch_matches

def main():
    parser = argparse.ArgumentParser(description="MatchBot CLI - esports match tracker")
    parser.add_argument("game", help="Game to track (e.g., dota2, csgo)")
    args = parser.parse_args()

    matches = fetch_matches(args.game)
    if not matches:
        print(f"No upcoming matches found for {args.game}.")
        return

    print(f"\nUpcoming matches for {args.game.upper()}:\n")
    for match in matches:
        print(f"{match['team1']} vs {match['team2']} at {match['time']}")

if __name__ == "__main__":
    main()
