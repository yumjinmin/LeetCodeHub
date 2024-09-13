import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    list = []
    num_rows = players.shape[0]
    num_columns = players.shape[1]
    list.extend([num_rows, num_columns])
    return list