import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[:1].str.upper() + users['name'].str[1:].str.lower()
    # str[:1], str.upper()은 별개의 연산
    return users.sort_values(by='user_id')
