import hashlib
import json
import pandas as pd
import time


def convert_to_sha1(string_to_convert: str) -> str:
    sha1 = hashlib.sha1()
    sha1.update(string_to_convert.encode('utf-8'))
    return sha1.hexdigest()


def save_two_df_to_json(path_name: str, df1: pd.DataFrame, name1_to_save: str, df2: pd.DataFrame, name2_to_save: str) -> None:
    json_file = {
        name1_to_save: df1.to_dict(orient='records'),
        name2_to_save: df2.to_dict(orient='records'),
    }

    with open(path_name, 'w') as f:
        f.write(json.dumps(json_file, indent=4))