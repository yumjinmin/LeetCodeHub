import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_emails = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$')]
    return valid_emails
