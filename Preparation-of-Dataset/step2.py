import pandas as pd
import os

path = r''

test = pd.read_csv(os.path.join(path, 'test.csv'))
store = pd.read_csv(os.path.join(path, 'stores.csv'))
dates = pd.read_csv(os.path.join(path, 'dates.csv'))
hols = pd.read_csv(os.path.join(path, 'holidays.csv'))
train = pd.read_csv(os.path.join(path, 'train.csv'))

holidates = hols['date'].unique()
dates['holi'] = dates['date'].isin(holidates).astype(int)

test = test.merge(store, on='store_id', how='left')
test = test.merge(dates, on='date', how='left')

train = train.sort_values(by=['store_id', 'category_id', 'date'])
train['l7'] = train.groupby(['store_id', 'category_id'])['target'].shift(7)
train['l14'] = train.groupby(['store_id', 'category_id'])['target'].shift(14)

lags = train[['store_id', 'category_id', 'date', 'l7', 'l14']]
test = test.merge(lags, on=['store_id', 'category_id', 'date'], how='left')

cols = [
    'date', 'store_id', 'category_id', 'onpromotion',
    'city', 'type', 'cluster',
    'year', 'month', 'dayofweek', 'weekofyear',
    'is_month_start', 'is_month_end', 'holi',
    'l7', 'l14'
]

test = test[cols]

out = r''
os.makedirs(out, exist_ok=True)

name = os.path.join(out, 'Prediction-test.csv')
test.to_csv(name, index=False)

print("Prediction-test.csv done", test.shape)
