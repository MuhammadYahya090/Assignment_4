import pandas as pd

def find_dupes(df):
    if df.empty: return pd.DataFrame()
    return df[df.duplicated(subset=['company_name', 'job_title', 'city', 'source_link'], keep=False)]