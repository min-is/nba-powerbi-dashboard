from kaggle.api.kaggle_api_extended import KaggleApi

def load_historical_data():
    api = KaggleApi()
    api.authenticate()
    
    # Download NBA play-by-play data from Kaggle
    api.dataset_download_files(
        'nathanlauga/nba-games',
        path='data_architecture/raw',
        unzip=True
    )
    
    # Convert to parquet
    for season in range(2015, 2024):
        df = pd.read_csv(f"data_architecture/raw/games_{season}.csv")
        df.to_parquet(f"data_architecture/processed/games_{season}.parquet")