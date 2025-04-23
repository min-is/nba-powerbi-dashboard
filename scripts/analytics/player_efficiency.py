import numpy as np

def calculate_advanced_metrics(df):
    """Calculate 15+ advanced basketball metrics"""
    df['TS_PCT'] = df['PTS'] / (2 * (df['FGA'] + 0.44 * df['FTA']))
    df['PIE'] = (df['PTS'] + df['FGM'] + df['FTM'] - df['FGA'] - df['FTA'] + 
                df['DRB'] + 0.5 * df['ORB'] + df['AST'] + df['STL'] + 
                0.5 * df['BLK'] - df['PF'] - df['TOV']) / np.maximum(df['MIN'], 1)
    return df
