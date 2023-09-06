import requests
import time
import pandas as pd
from database.database_connection import save_table_database
from utils import convert_to_sha1, save_two_df_to_json


def countries_information(url: str, database: str, path_name: str):
    try:
        response = requests.get(url)
        all_data = []

        if response.status_code == 200:
            data = response.json()

            for elem in data:
                start_time = time.perf_counter()

                lang = ''
                if elem.get("languages"):
                    lang = ", ".join([language for language in elem["languages"].values()])

                hash_sha1 = convert_to_sha1(lang)
                end_time = time.perf_counter()
                data = {
                    "Region": elem["region"],
                    "Country Name": elem["name"]["common"],
                    "Language": hash_sha1.upper(),
                    "Time (ms)": round(((end_time - start_time) * 1000), 4)
                }
                all_data.append(data)
            df_countries = pd.DataFrame(all_data)

            # Create stats
            stats_df = df_countries.describe().reset_index().drop(0)
            stats_df = pd.concat([stats_df, pd.DataFrame([{'index': 'sum', 'Time (ms)': df_countries["Time (ms)"].sum()}])], axis=0, ignore_index=True)
            stats_df.columns = ['Parameter', 'Value Time (ms)']

            # Save to database
            save_table_database(database, df_countries, 'countries_information')
            save_table_database(database, stats_df, 'time_stats')

            # Generate json file
            save_two_df_to_json(path_name, stats_df, 'time_stats', df_countries, 'countries')

            return df_countries, stats_df

        else:
            raise Exception(f"Error querying the API. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Connection error: {e}")


if __name__ == '__main__':
    url_to_connect = 'https://restcountries.com/v3.1/all'
    database_to_connect = 'database/tangelo-database.db'
    path_to_save = 'json_files/data.json'
    df, time_stats_df = countries_information(url_to_connect, database_to_connect, path_to_save)
    print(df)
    print(time_stats_df)
