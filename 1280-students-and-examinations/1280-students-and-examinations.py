import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
        left = pd.merge(students, subjects, how='cross').sort_values(by=['student_id', 'subject_name'])
        right = examinations.groupby(['student_id', 'subject_name'],).agg(attended_exams=('subject_name', 'count')).reset_index()
        result = pd.merge(left=left, right=right, how='left', on=['student_id', 'subject_name'])
        result['attended_exams'] = result['attended_exams'].fillna(0)
        return result
