import os
import pandas as pd

data_dir = r""

csv_list = [fname for fname in os.listdir(data_dir) if fname.endswith('.csv')]

file_info = []

for csv_file in csv_list:
    file_path = os.path.join(data_dir, csv_file)
    try:
        data_df = pd.read_csv(file_path)
        file_info.append({
            'file_name': csv_file,
            'col_count': data_df.shape[1],
            'row_count': data_df.shape[0]
        })
    except Exception as err:
        file_info.append({
            'file_name': csv_file,
            'col_count': 'err',
            'row_count': str(err)
        })

for detail in file_info:
    print(detail)
