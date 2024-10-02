import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df_filtered = activity.groupby('player_id')['event_date'].min().reset_index()
    df_filtered.rename(columns={'event_date':'first_login'}, inplace=True)
    return df_filtered
