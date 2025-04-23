from sklearn.ensemble import IsolationForest

def detect_statistical_anomalies(df):
    features = ['PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV']
    clf = IsolationForest(contamination = 0.05)
    df['anomaly_score'] = clf.fit_predict(df[features])
    return df[df['anomaly_score'] == -1]