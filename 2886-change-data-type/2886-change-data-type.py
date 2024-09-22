import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade':int})

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade':int}) # 할당 필요함 
    return students
