#!/usr/bin/python3
# -*- coding: utf-8 -*-

import inspect
import pandas as pd
pd.options.display.colheader_justify = 'right'
pd.set_option('display.unicode.east_asian_width', True)
pd.options.display.float_format = '{:.3g}'.format


def add_row_by_append():
    """ appendを使う方法。pandasnoversionによってはwarningが出る。
    """
    print(f'\n### {inspect.currentframe().f_code.co_name}')
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


def add_row_by_loc():
    """ locを使う方法。これを使うとエンジニアリング表記になる？
    """
    print(f'\n### {inspect.currentframe().f_code.co_name}')

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
    for i, row in enumerate(rows):
        df.loc[i] = row

    print(df)


if __name__ == '__main__':

    add_row_by_append()
    add_row_by_loc()
