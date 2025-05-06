import requests

def fetch_matches(game: str) -> list:
    
    mock_data = {
        "dota2": [
            {"team1": "Team Spirit", "team2": "OG", "time": "2025-05-10 18:00"},
            {"team1": "PSG.LGD", "team2": "Gaimin Gladiators", "time": "2025-05-11 21:00"},
        ],
        "csgo": [
            {"team1": "NAVI", "team2": "FaZe Clan", "time": "2025-05-09 16:00"},
        ]
    }
    return mock_data.get(game.lower(), [])
