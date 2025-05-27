import pandas as pd
import os

base = r""
datap = os.path.join(base, "Data")
final = os.path.join(base, "Final-dataset", "Training-custom.csv")

train = pd.read_csv(final)
store = pd.read_csv(os.path.join(datap, "stores.csv"))
dates = pd.read_csv(os.path.join(datap, "dates.csv"))

train = train.merge(store[['store_id', 'city', 'type', 'cluster']], on='store_id', how='left')
train = train.merge(dates[['date', 'year', 'month', 'dayofweek', 'weekofyear']], on='date', how='left')

train.to_csv(final, index=False)

print("saved", train.shape)
