import pandas as pd
import os
import joblib
import numpy as np

base = r""

test_f = os.path.join(base, 'Final-dataset', 'Prediction-test-updated.csv')
model_f = os.path.join(base, 'Model', 'lgb_model_v2.pkl')
subm_f = os.path.join(base, 'Final-dataset', 'Submission.csv')

df_t = pd.read_csv(test_f)
model = joblib.load(model_f)

def safe_encode(srs, le):
    cls_map = {c: i for i, c in enumerate(le.classes_)}
    return srs.map(cls_map).fillna(-1).astype(int)

cat_cols = ['store_id', 'category_id', 'city', 'type', 'cluster']

for c in cat_cols:
    enc_f = os.path.join(base, 'Encoders', f'{c}_encoder.pkl')
    le = joblib.load(enc_f)
    df_t[c] = safe_encode(df_t[c], le)

X_t = df_t.drop(columns=['date'])

pred_log = model.predict(X_t)
pred = np.expm1(pred_log)
pred[pred < 0] = 0

df_t['target'] = pred
df_t['ID'] = df_t.apply(lambda r: f"year_week_{r['year']}_store_{r['store_id']}_category_{r['category_id']}", axis=1)

subm = df_t[['ID', 'target']]
subm.to_csv(subm_f, index=False)

print("Prediction & submission done.\nSaved at:", subm_f)
