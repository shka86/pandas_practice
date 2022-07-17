#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    # データフレームを作成 -----------------------------------
    rows = [
        ['item0', 7.5382, -45.3561],
        ['item1', 23.8294, -50.2675],
        ['item2', 1.6672, -34.8013],
        ['item3', 27.4099, -33.5921],
        ['item4', 33.4072, -63.4817],
        ['item5', 84.0186, -70.1679],
        ['item6', 14.2406, -33.9176],
        ['item7', 73.9508, -56.4601],
        ['item8', 95.1479, -90.2869],
        ['item9', 55.3651, -26.5356],
    ]

    df = pd.DataFrame(
        columns=['item', 'val_pos', 'val_neg'],
        data=rows
    )

    print(df)

    # グラフ表示 -----------------------------------
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_xlim(-100, 100)
    ax1.set_xticks(np.arange(-100,101,20))
    # ax1.grid(which="both", color="black", alpha=0.5)
    # ax1.grid(True)
    # ax1.invert_yaxis()

    df.plot.barh(ax=ax1, x='item', title='simple horizontal bar')

    plt.show()
    # plt.savefig('hoge.png')
    # plt.close('all')
