import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders_filtered = orders.groupby('customer_number')['order_number'].count().reset_index()
    return orders_filtered[orders_filtered['order_number'] == orders_filtered['order_number'].max()][['customer_number']]