import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['work_time'] = employees['out_time'] - employees['in_time']
    total_time_df = employees.groupby(['emp_id', 'event_day']).agg(total_time=('work_time', 'sum')).reset_index()
    total_time_df_renamed = total_time_df[['event_day', 'emp_id', 'total_time']].rename(columns={'event_day':'day'})
    return total_time_df_renamed
