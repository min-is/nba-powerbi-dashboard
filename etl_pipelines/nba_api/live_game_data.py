class NBALiveFeed:
    def __init__(self):
        self.play_by_play_url = "https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_0022300544.json"
    
    def get_real_time_stats(self):
        """json endpoint Q15s"""
        while game_active:
            response = requests.get(self.play_by_play_url)
            yield self._parse_feed(response.json())