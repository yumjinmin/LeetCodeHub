import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director_counts = actor_director.groupby(['actor_id', 'director_id']).nunique().reset_index()
    return actor_director_counts[actor_director_counts['timestamp'] >=3][['actor_id', 'director_id']]