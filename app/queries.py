import pandas as pd
from sqlalchemy import text

def fetch_all(engine):
    return pd.read_sql("SELECT * FROM opportunities ORDER BY opportunity_id DESC", engine)

def execute_query(engine, sql, params):
    with engine.begin() as conn:
        conn.execute(text(sql), params)