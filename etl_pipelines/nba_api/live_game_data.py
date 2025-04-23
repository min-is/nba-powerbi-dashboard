import requests
import pandas as pd
from datetime import datetime

class NBALiveFeed:
    def __init__(self):
        self.base_url = "https://cdn.nba.com/static/json/liveData"
        
    def get_play_by_play(self, game_id):
        response = requests.get(f"{self.base_url}/playbyplay/playbyplay_{game_id}.json")
        return self._parse_pbp(response.json())
    
    def _parse_pbp(self, data):
        events = []
        for event in data['game']['actions']:
            events.append({
                'game_id': event['gameId'],
                'period': event['period'],
                'clock': event['clock'],
                'description': event['description'],
                'player_id': event['personId'],
                'team_id': event['teamId'],
                'x_coord': event.get('xLegacy', None),
                'y_coord': event.get('yLegacy', None),
                'event_type': event['actionType']
            })
        return pd.DataFrame(events)