#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
pd.options.display.colheader_justify = 'right'
pd.set_option('display.unicode.east_asian_width', True)

# 列の項目だけ定義した空のデータテーブルを作る
df = pd.DataFrame(
    columns=['測定条件', 'データA', 'データB']
)

# 行のデータをリストに格納する。csvか何かからデータを取ってきた想定。
row0 =['室温', 100.0, 1e-3]
row1 =['50℃', 300.43, 5.5e-6]
row2 =['0℃', 10.26347, 8888e12]
rows = [
    row0,
    row1,
    row2
]

for row in rows:
    temp_series = pd.Series(row, index=df.columns)
    df = df.append(temp_series, ignore_index=True)

print(df)

