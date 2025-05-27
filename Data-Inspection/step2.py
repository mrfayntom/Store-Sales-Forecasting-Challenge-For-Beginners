import os
import pandas as pd

data_dir = r""

csv_list = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

for csv_file in csv_list:
    file_path = os.path.join(data_dir, csv_file)
    try:
        mini_df = pd.read_csv(file_path, nrows=1)
        col_list = mini_df.columns.tolist()
        print(f"{csv_file} : {col_list}")
    except Exception as err:
        print(f"{csv_file} : Error - {err}")
