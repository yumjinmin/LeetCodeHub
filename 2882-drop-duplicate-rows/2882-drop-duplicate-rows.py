import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True,ignore_index=False)
    return customers

# subset: 중복값을 검사할 열 입니다. 기본적으로 모든 열을 검사합니다.
# keep: {first/last} 중복 제거 시 남길 행입니다. first면 첫값을 남기고 last면 마지막 값을 남깁니다.
# inplace: 원본을 변경할지의 여부입니다.
# ignore_index: 원래 index를 무시할지 여부입니다. True일 경우 0,1,2, ... , n으로 부여됩니다.
