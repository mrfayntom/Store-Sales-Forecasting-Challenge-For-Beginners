import os
import pandas as pd

path = r''

files = [x for x in os.listdir(path) if x.endswith('.csv')]

stuff = {}

for f in files:
    p = os.path.join(path, f)
    try:
        tmp = pd.read_csv(p, nrows=5)
        all = pd.read_csv(p)
        stuff[f] = [len(all), list(tmp.columns)]
    except Exception as err:
        stuff[f] = 'fail: ' + str(err)

for name, info in stuff.items():
    if isinstance(info, list):
        print(name, "=>", info[0], "rows,", info[1])
    else:
        print(name, "=>", info)
