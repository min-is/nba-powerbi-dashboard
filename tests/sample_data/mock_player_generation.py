import pandas as pd
import numpy as np

def generate_player(num=1000):
    return pd.DataFrame({
        'player_id': [f"{i:04}" for i in range(num)],
        'height': np.random.normal(198, 8, num),
        'weight': np.random.normal(95, 10, num),
        'position': np.random.choice(['G', 'F', 'C'], num)
    })