import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = pd.melt(products, id_vars=['product_id'], var_name='store', value_name='price')
    return products.dropna()
