import pandas as pd
import os

base = r""
src = os.path.join(base, "Final-dataset", "Training-custom.csv")
out = os.path.join(base, "Final-dataset", "Train.csv")

df = pd.read_csv(src)

df = df.rename(columns={
    'city_x': 'city',
    'type_x': 'type',
    'cluster_x': 'cluster',
    'year_x': 'year',
    'month_x': 'month',
    'dayofweek_x': 'dayofweek',
    'weekofyear_x': 'weekofyear'
})

dropem = ['city_y', 'type_y', 'cluster_y', 'year_y', 'month_y', 'dayofweek_y', 'weekofyear_y']
for c in dropem:
    if c in df.columns:
        df.drop(columns=c, inplace=True)

df.to_csv(out, index=False)

print("Train.csv done", out)
print("columns:", df.columns.tolist())
