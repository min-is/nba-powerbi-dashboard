def test_stat_ranges(player_stats_df):
    assert (player_stats_df['PTS'] >= 0).all()
    assert (player_stats_df['FG3A'] <= player_stats_df['FGA']).all()
    assert (player_stats_df['FT_PCT'].between(0, 1, inclusive = 'both')).all()