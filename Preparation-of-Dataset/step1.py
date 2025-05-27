import pandas as pd
import os

path = r''

train = pd.read_csv(os.path.join(path, 'train.csv'))
store = pd.read_csv(os.path.join(path, 'stores.csv'))
dates = pd.read_csv(os.path.join(path, 'dates.csv'))
hol = pd.read_csv(os.path.join(path, 'holidays.csv'))

train = train.merge(store, on='store_id', how='left')

holi_dates = hol['date'].unique()
dates['holi'] = dates['date'].isin(holi_dates).astype(int)

train = train.merge(dates, on='date', how='left')

train = train.sort_values(by=['store_id', 'category_id', 'date'])
train['lag7'] = train.groupby(['store_id', 'category_id'])['target'].shift(7)
train['lag14'] = train.groupby(['store_id', 'category_id'])['target'].shift(14)
train['mean7'] = train.groupby(['store_id', 'category_id'])['target'].shift(1).rolling(7).mean()

colz = [
    'date', 'store_id', 'category_id', 'target',
    'onpromotion', 'nbr_of_transactions',
    'city', 'type', 'cluster',
    'year', 'month', 'dayofweek', 'weekofyear',
    'is_month_start', 'is_month_end', 'holi',
    'lag7', 'lag14', 'mean7'
]

train = train[colz]

out = r''
os.makedirs(out, exist_ok=True)

name = os.path.join(out, 'Training-custom.csv')
train.to_csv(name, index=False)

print("file saved", train.shape)
