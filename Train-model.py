import os
import pandas as pd
import lightgbm as lgb
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

base = r""
train_path = os.path.join(base, "Final-dataset", "Train.csv")
model_path = os.path.join(base, "Model", "lgb_model_v2.pkl")

df = pd.read_csv(train_path)

cat_feats = ['store_id', 'category_id', 'city', 'type', 'cluster']
encoders = {}
for c in cat_feats:
    le = LabelEncoder()
    df[c] = le.fit_transform(df[c])
    encoders[c] = le

X = df.drop(columns=['date', 'target'])
y = np.log1p(df['target'])

X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

train_set = lgb.Dataset(X_tr, label=y_tr)
val_set = lgb.Dataset(X_val, label=y_val)

params = {
    'objective': 'regression',
    'metric': 'rmse',
    'verbosity': -1,
    'boosting_type': 'gbdt',
    'learning_rate': 0.05,
    'num_leaves': 31,
    'max_depth': 8,
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'lambda_l2': 1.0,
    'seed': 42
}

cbs = [
    lgb.early_stopping(stopping_rounds=50),
    lgb.log_evaluation(period=50)
]

model = lgb.train(
    params,
    train_set,
    valid_sets=[train_set, val_set],
    valid_names=['train', 'valid'],
    num_boost_round=1000,
    callbacks=cbs
)

os.makedirs(os.path.dirname(model_path), exist_ok=True)
joblib.dump(model, model_path)

print("Model trained and saved at:", model_path)
