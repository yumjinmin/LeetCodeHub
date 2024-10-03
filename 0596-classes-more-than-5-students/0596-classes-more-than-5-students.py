import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses.groupby('class').filter(lambda x: len(x) >= 5)['class'].drop_duplicates().to_frame()
    ## courses 데이터프레임에서 class 열을 기준으로 그룹화
    ## 각 그룹(클래스)에 대해 그룹의 행 수가 5 이상인 경우에만 해당 그룹을 필터링
    ## 필터링된 결과에서 class 열만 선택
    ## 중복된 클래스 이름들을 제거
    ## 결과가 기본적으로 Series 형식으로 반환되기 때문에, 이를 DataFrame 형식으로 변환