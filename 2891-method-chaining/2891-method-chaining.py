import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals[animals['weight']>=100].sort_values(by='weight', ascending=False)
    return animals.loc[:, ['name']]

    # animals.loc[:, 'name'] 이렇게 한 개의 칼럼만 지정한 경우 데이터프레임이 아닌 시리즈 형식을 반환하므로 대괄호를 넣어줘야 함
