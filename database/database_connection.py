import sqlite3
import pandas as pd


def save_table_database(database_name: str, df: pd.DataFrame, table_name: str) -> None:
    conn = sqlite3.connect(database_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
