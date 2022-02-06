README
====

pandasめも  

## Description
pandasは高機能なのでググるとたくさんの情報が出てくる。
目的は同じでもやり方は多様だから、毎回調べていると一向に定着しないし、メンテナンスもしんどくなってくる。
よってお決まりの方法をいくつか記録しておく。

処理速度の観点は度外視。
高速化を求められる場面に出くわしたらその時に考えりゃいい。


### 0. 表示を整える
手間なしで他人に見せられるようにしておく

    ```py
    # 有効数字(小数点以下をそろえる)
    pd.options.display.float_format = '{:.3f}'.format

    # 有効数字(全体の桁数をそろえる)
    pd.options.display.float_format = '{:.6g}'.format

    # 表示を省略しない
    pd.options.display.max_rows = None

    # アライメント系
    pd.set_option('display.unicode.east_asian_width', True)
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
def conv_num_to_eng_string(x):
    print(x)
    if type(x) in [int, float, complex]:
        x = decimal.Decimal(str(x)).normalize().to_eng_string()
    return x

df = df.applymap(conv_num_to_eng_string)

```


これでいい感じにやってくれていそうな気もする。
```py
pd.options.display.float_format = '{:.3g}'.format
```








### 1. 列の項目を先に決めて行を追加していく

- pandas_practice.py
    - add_row_by_append()
    - add_row_by_loc()
    - add_row_by_loc_2()

## Requirement
- python3  
    - Python 3.8.1 で動作確認
    - pandas

## Licence

[MIT](https://github.com/shka86/foo/blob/master/LICENCE)

## Author

[shka86](https://github.com/shka86)
