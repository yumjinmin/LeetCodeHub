import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # 조건을 만족하는 직원에게 보너스를 지급
    # if 대신 loc를 사용해 필터링 
    employees.loc[(employees['employee_id']%2==1) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    # 나머지 직원들에게는 보너스를 0으로 설정
    employees['bonus'] = employees['bonus'].fillna(0)
    
    # employee_id와 bonus만 반환
    return employees[['employee_id', 'bonus']].sort_values('employee_id')

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df['bonus'] = ((employees['employee_id'] % 2 != 0) & ~(employees['name'].str.startswith('M')))*employees['salary']
    df = df[['employee_id', 'bonus']].sort_values(by = 'employee_id')
    return df
