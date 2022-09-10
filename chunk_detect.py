#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np

"""Nanで数値が挟まれたデータについて処理をする

    結局はデータをTure/Falseに変換して、その区切り位置を調べることが肝

"""

PASS_SPAN = 0.2
PASS_VALUE = 1
LABEL_PASS = "PASS"
LABEL_FAIL = "_F_A_I_L_"
PARTLY_CHECK = [0, 1, 3]


def chunk_detector(df):

    df_summary = pd.DataFrame(
        columns=df.columns,
        index=["judge", "num_chunk", "span", "edge_left", "edge_right"])

    df_bool = (df >= PASS_VALUE)
    print(df_bool)

    for col in df_bool:
        num_chunk, span, edge_left, edge_right = chunk_detector_(df_bool[col])
        df_summary.loc["span", col] = span
        df_summary.loc["num_chunk", col] = num_chunk
        df_summary.loc["edge_left", col] = edge_left
        df_summary.loc["edge_right", col] = edge_right

        if num_chunk == 3 and span >= PASS_SPAN:
            judge = LABEL_PASS
        else:
            judge = LABEL_FAIL

        df_summary.loc["judge", col] = judge

    return df_summary


def chunk_detector_(series):

    state = False  # PASS_VALUE未満で開始することを期待
    num_typechange = 0
    num_chunk = 0
    span = None
    edge_left = None
    edge_right = None

    for i, v in series.iteritems():

        if state:
            if not v:
                num_typechange += 1
                state = False

        else:
            if v:
                num_typechange += 1
                state = True

    num_chunk = num_typechange + 1
    if num_chunk == 3 or True:
        series = series.dropna()  # 中央のchunkだけ抜き出す
        edge_left = series.index[0]
        edge_right = series.index[-1]
        span = edge_right - edge_left

    return num_chunk, span, edge_left, edge_right


def judgement(df_summary):

    print("-----------------------------------")
    print(f"PASS_SPAN:  {PASS_SPAN}")
    print(f"PASS_VALUE: {PASS_VALUE}")
    print("---")
    print(df_summary)
    print("-----------------------------------\n")
    # 全体
    if LABEL_FAIL in df_summary.loc["judge"].unique():
        print("All : FAIL ***")
    else:
        print("All : PASS")

    print("")

    # 部分的
    if LABEL_FAIL in df_summary.iloc[:, PARTLY_CHECK].loc["judge"].unique():
        print("Part: FAIL ***")
    else:
        print("Part: PASS")
    print(f"   check for {PARTLY_CHECK}")

    print("\n-----------------------------------")


if __name__ == '__main__':

    # 入力データ作成
    df = pd.DataFrame(columns=["position", "item0", "item1", "item2", "item3"])

    for x in range(21):
        row = [-1 + 0.1 * x, np.nan, np.nan, np.nan, np.nan]
        df.loc[x] = row

    df.iloc[5:13, 1] = 1
    df.iloc[3:18, 2] = 1
    df.iloc[2:4, 3] = 1
    df.iloc[8:12, 3] = 1
    df.iloc[9:11, 4] = 1

    df.iloc[5:13, 3] = 1
    df.iloc[3:18, 4] = 1

    df = df.set_index("position")

    print(df)

    df_summary = chunk_detector(df)
    judgement(df_summary)
