import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby('sell_date')['product'].apply(lambda x: sorted(x.drop_duplicates())).reset_index(name='products')
    df['num_sold'] = df['products'].apply(len)  ## 리스트의 길이를 계산하여 'num' 칼럼 추가
    df['products'] = df['products'].apply(lambda x: ','.join(x))  ## products 리스트를 쉼표로 구분된 문자열로 변환
    df = df[['sell_date', 'num_sold', 'products']]  ## 'num' 칼럼을 'products' 칼럼 앞에 배치
    return df.sort_values(by='sell_date')