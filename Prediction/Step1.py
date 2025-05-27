import pandas as pd

fpath = r"/Prediction-test-updated.csv"

df = pd.read_csv(fpath)

print("Cols in file:")
print(df.columns.tolist())

req_feats = [
    'store_id', 'category_id', 'onpromotion', 'city', 'type', 'cluster',
    'year', 'month', 'dayofweek', 'weekofyear',
    'is_month_start', 'is_month_end', 'is_holiday',
    'lag_7', 'lag_14', 'nbr_of_transactions', 'rolling_mean_7'
]

miss_feats = [c for c in req_feats if c not in df.columns]

if not miss_feats:
    print("All req features present")
else:
    print("Missing features:")
    for f in miss_feats:
        print(" -", f)
