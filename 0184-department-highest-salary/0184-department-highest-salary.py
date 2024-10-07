import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    salary_max = employee[employee['salary'] == employee.groupby('departmentId')['salary'].transform('max')]
    merged_df = salary_max.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    return merged_df.loc[:, ['name_dept', 'name_emp', 'salary']].rename(columns={'name_dept': 'Department', 'name_emp': 'Employee', 'salary': 'Salary'})
