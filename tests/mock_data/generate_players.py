import numpy as np
import pandas as pd

def generate_mock_players(num=500):
    positions = ['PG', 'SG', 'SF', 'PF', 'C']
    return pd.DataFrame({
        'player_id': np.arange(1, num+1),
        'height': np.random.normal(198, 8, num),
        'weight': np.random.normal(95, 10, num),
        'position': np.random.choice(positions, num),
        'draft_year': np.random.randint(2010, 2024, num)
    })