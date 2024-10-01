import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salary = employee['salary'].sort_values(ascending=False).drop_duplicates()
    if len(sorted_salary) >= 2:
        second_highest = sorted_salary.iloc[1]
        return pd.DataFrame({'SecondHighestSalary': [second_highest]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [None]})