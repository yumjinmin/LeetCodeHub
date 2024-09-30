import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)

# subset : 중복값을 검사할 열 입니다. 기본적으로 모든 열을 검사합니다.
# keep : {first / last} 중복 제거를 할때 남길 행입니다. first면 첫값을 남기고 last면 마지막 값을 남깁니다.
# inplace : 원본을 변경할지의 여부입니다.