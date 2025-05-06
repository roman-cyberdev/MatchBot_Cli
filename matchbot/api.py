import requests
import json

PANDASCORE_API_URL = "https://api.pandascore.io/v1/games/{game}/matches"
API_KEY = "your_pandascore_api_key_here"  

def fetch_pandascore_matches(game):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    
    url = PANDASCORE_API_URL.format(game=game)

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        matches = response.json()
        return matches

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {game}: {e}")
        return []
