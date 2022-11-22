README
====

pandasめも  

## Description
pandasは高機能なのでググるとたくさんの情報が出てくる。
目的は同じでもやり方は多様だから、毎回調べていると一向に定着しないし、メンテナンスもしんどくなってくる。
よってお決まりの方法をいくつか記録しておく。

あくまでpythonを仕事の効率化ツールとして使うことを想定している。
細かい例外処理や速度の観点はあまり重要視していない。
それらが求められる場面に出くわしたらその時に考えりゃいい。


```py
import pandas as pd

# サンプルデータ 文字列系
df_str = pd.DataFrame(
    index=['行0', '行1', '行2'],
    columns=['列0', '列1', '列2'],
    data=[
        ['行0列0', '行0列1', '行0列2'],
        ['行1列0', '行1列1', '行1列2'],
        ['行2列0', '行2列1', '行2列2'],
    ]
)

print(df_str)

import pandas as pd

# サンプルデータ 数値系
df_num = pd.DataFrame(
    index=['行0', '行1', '行2'],
    columns=['列0', '列1', '列2'],
    data=[
        [0, 1, 2],
        [0.0, 11.1, 0.00022],
        [0e0, 1e-15, 2e9],
    ]
)

print(df_num)


```


### 0. 表示を整える
手間なしで他人に見せられるようにしておく

    ```py
    # 有効数字(小数点以下をそろえる)
    pd.options.display.float_format = '{:.3f}'.format

    # 有効数字(全体の桁数をそろえる)
    pd.options.display.float_format = '{:.6g}'.format

    # 表示を省略しない
    pd.options.display.max_rows = None

    # 日本語の桁数をそろえる。formatで桁数をそろえるときに、
    # これを設定しないと2バイト文字が1文字でカウントされてずれる。
    pd.set_option('display.unicode.east_asian_width', True)

    # アライメント系
    pd.options.display.colheader_justify = 'left'
    pd.options.display.colheader_justify = 'center'
    pd.options.display.colheader_justify = 'right'


    ```

- 工学的記数法/工学表記

pandasだと指数部分が e+02 とか e-07 とかになる。
キロとかマイクロとかの単位で表示してくれると楽なのに。
多少無理やりだが decimal ライブラリを使う方法を用意しておく
ただし、全部が全部工学表記になるわけではなさそう。

```py
import decimal 

def conv_num_to_eng_string(x):
    print(x)
    if type(x) in [int, float, complex]:
        x = decimal.Decimal(str(x)).normalize().to_eng_string()
    return x

df = df.applymap(conv_num_to_eng_string)
print(df)

```


これでいい感じにやってくれていそうな気もする。
```py
pd.options.display.float_format = '{:.3g}'.format
```



### 1: 列の項目を先に決めて行を追加していく

- pandas_practice.py
    - add_row_by_append()
    - add_row_by_loc()
    - add_row_by_loc_2()


```py
import pandas as pd
#  add_row_by_append()
""" 
appendを使う方法。
pandasnoversionによってはwarningが出る。
"""
# 列の項目だけ定義した空のデータテーブルを作る
df = pd.DataFrame(
    columns=['測定条件', 'データA', 'データB']
)

# 行のデータをリストに格納する。csvか何かからデータを取ってきた想定。
row0 = ['室温', 100.0, 1e-3]
row1 = ['50℃', 3000.43, 5.5e-6]
row2 = ['0℃', 10.26347, 8888e12]
rows = [
    row0,
    row1,
    row2
    ]

# 行を追加していく
for row in rows:
    temp_series = pd.Series(row, index=df.columns)
    df = df.append(temp_series, ignore_index=True)

print(df)

```

```py
import pandas as pd
#  add_row_by_loc()
""" 
appendを使う方法。
pandasnoversionによってはwarningが出る。
"""
# 列の項目だけ定義した空のデータテーブルを作る
df = pd.DataFrame(
    columns=['測定条件', 'データA', 'データB']
)

# 行のデータをリストに格納する。csvか何かからデータを取ってきた想定。
row0 = ['室温', 100.0, 1e-3]
row1 = ['50℃', 3000.43, 5.5e-6]
row2 = ['0℃', 10.26347, 8888e12]
rows = [
    row0,
    row1,
    row2
]

# 行を追加していく
for row in rows:
    temp_series = pd.Series(row, index=df.columns)
    df = df.append(temp_series, ignore_index=True)

print(df)

```

```py
import pandas as pd
""" locを使う方法。dfの後ろに追加していく
"""
# 列の項目だけ定義した空のデータテーブルを作る
df = pd.DataFrame(
    columns=['測定条件', 'データA', 'データB']
)

# 行のデータをリストに格納する。csvか何かからデータを取ってきた想定。
row0 = ['室温', 100.0, 1e-3]
row1 = ['50℃', 3000.43, 5.5e-6]
row2 = ['0℃', 10.26347, 8888e12]
rows = [
    row0,
    row1,
    row2
]

# 行を追加していく
len_df = len(df)
for i, row in enumerate(rows):
    df.loc[i + len_df] = row

print(df)

```

```py
import pandas as pd
""" 二次元listからデータフレームに変換する方法。
"""

# 行のデータをリストに格納する。csvか何かからデータを取ってきた想定。
row0 = ['室温', 100.0, 1e-3]
row1 = ['50℃', 3000.43, 5.5e-6]
row2 = ['0℃', 10.26347, 8888e12]
rows = [
    row0,
    row1,
    row2
]

# 行を追加していく
df = pd.DataFrame(
    rows,
    columns=['測定条件', 'データA', 'データB']
)

print(df)

```


### 2: 行の項目を先に決めて列を追加していく

    転置すれば行追加で対応できるので、基本的に行追加できる形式に持っていく。
    どうしても必要になったら調べる。

### 3: 集計

- 列の要素をカウントする

```py
# 要素がindex、出現個数をdataとするSeriesが返る
vc = df['hoge'].value_counts()

# indexのリストを取得する
vc.index.values.tolist()

```



### 4: 条件に合う行・列を抽出する

query は知っていて損はないけど、文字列検索の使い勝手が悪いから、
ここに示すブールインデックスでの抽出に絞って使うようにしたほうが使いまわしができる。

それから、条件文は括弧でくくることをクセづけたほうが良い。
ダサくても余計なエラーで時間を取られて仕事が進まないよりはましでしょう。

```py
# hoge列が100の行を抽出する
df_ = df[df['hoge'] == 100]


```

### 5: データを変更する

- セルを選択して値を変更する  

```py
import pandas as pd

# サンプルデータ 文字列系
df_str = pd.DataFrame(
    index=['行0', '行1', '行2'],
    columns=['列0', '列1', '列2'],
    data=[
        ['行0列0', '行0列1', '行0列2'],
        ['行1列0', '行1列1', '行1列2'],
        ['行2列0', '行2列1', '行2列2'],
    ]
)

print(df_str)

# 行番号、列番号で指定する場合。
# iatとilocの2種類がある。iatのほうが速いらしい。
df_str.iat[0, 1] = "iatで変更した！"
print(df_str)

df_str.iloc[0, 1] = "ilocで変更した！"
print(df_str)
# 行名、列名で指定する場合。
# atとlocの2種類がある。atのほうが速いらしい。
df_str.at["行0", "列1"] = "atで変更した！"
print(df_str)

df_str.loc["行0", "列1"] = "locで変更した！"
print(df_str)

# 行番号と列名で指定したい場合

# 行名がないdfに変更する
# drop=True でもともとついているindexを削除する。Falseだとindexが2重になる。Multiindexっていうのかな？階層ごとに集計できるなど利点がある。後で勉強するか。
print("index を振りなおす")
df_str = df_str.reset_index(drop=True)
print(df_str)

# 行が番号なので、列も番号にすればOK。
# 列名から列番号を取得するために get_loc() を使用する。
# 列番号は df.columns.get_loc()
# 行番号は df.index.get_loc() 今回は関係ないけど
col = df_str.columns.get_loc('列1')
df_str.iat[0, col] = "iatで変更した！"
print(df_str)

df_str.iloc[0, col] = "ilocで変更した！"
print(df_str)

```


### 6: - 関数を適用する  
    - map : Series にのみ適用可能
    - applymap : DataFrame にのみ適用可能
    - apply : Series と DataFrame に適用可能  
        一見どちらにも適用できて便利そうだけど、デフォルトでは戻り値が 行のリストが格納されたSeries になることに注意。
        テーブル全体に関数を適用しようとすると result_type オプションを指定する必要がある。
        面倒なので使わないのが吉。

```py
import pandas as pd

# サンプルデータ 文字列系
df_str = pd.DataFrame(
    index=['行0', '行1', '行2'],
    columns=['列0', '列1', '列2'],
    data=[
        ['行0列0', '行0列1', '行0列2'],
        ['行1列0', '行1列1', '行1列2'],
        ['行2列0', '行2列1', '行2列2'],
    ]
)
print(df_str)

# 適用する関数
def func1(x):
    '''入力文字列 x の末尾に "_mod" を付けて返すだけ。
        実際は数値の処理に置き換えるなどしてOK
    '''
    return f"{x}_mod"

print("# map : 列に関数が適用される")
df_ = df_str['列0'].map(func1)
print(df_)
print("# map : 元のデータフレームに変更を適用したり、新しい列を追加することもできる")
df_str['列1'] = df_str['列0'].map(func1)
df_str['列3'] = df_str['列0'].map(func1)
print(df_str)

print("# applymap : データフレーム全体に関数が適用される")
df_ = df_str.applymap(func1)
print(df_)

print("# apply : optionを指定しないと Series が返ってきてしまう。面倒。")
df_ = df_str.apply(func1)
print(df_)


print("# lambda式でもOK")
df_str['列1'] = df_str['列0'].map(lambda x: f"{x}_by_lambda")
print(df_str)


print("# 引数が複数の場合。lambda式を応用すればOK")
# 使う場面は多いんだけどググってもなかなか出てこないので書いておく。別の方法があるってことなのかな？
def func2(a, b):
    return f"{a}_{b}"
df_str['列1'] = df_str['列1'].map(lambda x: func2(x, "fukusuu"))
print(df_str)

```


### 7: データフレームの結合

列名がそろっているデータフレーム同士を縦につなげる。

```py
import pandas as pd
# サンプルデータ
df_A = pd.DataFrame(
    index=['A0', 'A1', 'A2'],
    columns=['列0', '列1', '列2'],
    data=[
        ['A0列0', 'A0列1', 'A0列2'],
        ['A1列0', 'A1列1', 'A1列2'],
        ['A2列0', 'A2列1', 'A2列2'],
    ]
)

df_B = pd.DataFrame(
    index=['B0', 'B1', 'B2'],
    columns=['列0', '列1', '列2'],
    data=[
        ['B0列0', 'B0列1', 'B0列2'],
        ['B1列0', 'B1列1', 'B1列2'],
        ['B2列0', 'B2列1', 'B2列2'],
    ]
)

print(df_A)
print(df_B)

# 縦方向の結合
df_AB_vertical = pd.concat(
    [df_A, df_B],
    ignore_index=True
)

print(df_AB_vertical)

```

## Requirement
- python3  
    - Python 3.8.1 で動作確認
    - pandas

## Licence

[MIT](https://github.com/shka86/foo/blob/master/LICENCE)

## Author

[shka86](https://github.com/shka86)
