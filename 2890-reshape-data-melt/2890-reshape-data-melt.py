import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

# pivot과 반대 작업 수행
# id_vars는 기준이 되는 id 변수
# id_vars를 기준으로 원래 데이터 셋에 있던 여러개의 칼럼을 variable 칼럼에 위에서 아래로 길게 쌓음
# 값은 value 칼럼에 들어감
# var_name은 variable 칼럼의 이름을 설정할 때 사용
# value_name은 value 칼럼의 이름을 설정할 때 사용
