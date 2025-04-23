import requests
import pandas as pd
from retrying import retry

class NBAStatsAPI:
    def __init__(self, api_key):
        self.base_url = "https://stats.nba.com/stats"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Referer': "https://stats.nba.com",
            'x-nba-stats-token': api_key
        }

        @retry(stop_max_attempt_number = 5, wait_fixed = 2500)

        def get_player_tracking(self, season):
            endpoint = "leaguedashptstats"
            params = {
                'PerMode': 'PerGame',
                'Season': season,
                'SeasonType': "Regular Season"
            }
            return self._api_call(endpoint, params)

        def _api_call(self, endpoint, params):
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers = self.headers,
                params = params
            )
            response.raise_for_status()
            return self._parse_response(response.json())
        
        def _parse_response(self, data):
            headers = data['resultSets'][0]['headers']
            rows = data['resultSets'][0]['rowSet']
            return pd.DataFrame(rows, columns = headers)