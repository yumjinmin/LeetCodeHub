import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.pivot(weather, index='month', columns='city', values='temperature')
    return df
