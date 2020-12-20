#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import random
import pandas as pd
from pathlib import Path as p
from pprint import pprint as pp

def make_json():

    d_ref0 = {}
    for i in range(8):
        d_ref0[f"corner{i}"] = {"mean": random.random(),
                              "stdev": random.random()
        }

    with open("ref0.json", "w") as f:
        json.dump(d_ref0, f, indent=4)

    d_ref1 = {}
    for i in range(8):
        d_ref1[f"corner{i}"] = {"mean": random.uniform(100, 200),
                              "stdev": random.uniform(100, 200)
        }

    with open("ref1.json", "w") as f:
        json.dump(d_ref1, f, indent=4)


def json2csv():

    df = pd.read_json("ref0.json", encoding="utf-8")
    df.transpose().to_csv("ref0.csv", encoding="utf-8")
    df = pd.read_json("ref1.json", encoding="utf-8")
    df.transpose().to_csv("ref1.csv", encoding="utf-8")


def test():

    # read namelist
    with open("namelist.json", "r") as f:
        namelist = json.load(f)

    # transform namelist
    namelist_mod = {}
    for x in namelist:
        print(x)
        namelist_mod[namelist[x]["id"]] = namelist[x]
        namelist_mod[namelist[x]["id"]]["name"] = x
        namelist_mod[namelist[x]["id"]].pop("id")
    pp(namelist_mod)

    # read criteria
    criteria = p(".").glob("ref*_criteria.csv")
    print(list(criteria))
    exit()
    # read result
    df = pd.read_csv("res.csv", encoding="utf-8")
    print(df, "\n")

    # drop row
    df = df.drop(df.index[[0]])
    print(df, "\n")

    # calc spec
    df['mean+3stdev'] = df['mean'] + 3 * df['stdev'] + 0.05 * 125
    print(df, "\n")

    df['|'] = "|"
    df['criteria'] = "99.9999"
    print(df, "\n")

    d = json.loads(df.to_json(orient='index'))
    pp(d)

    for i in d:
        data_id = d[i]["Louis"]
        criteria = namelist_mod[data_id]["criteria"]
        d[i]["criteria"] = criteria
    pp(d)

    df = pd.DataFrame.from_dict(d, orient='index')
    print(df, "\n")

    # for index, row in df.iterrows():
    #     print(row)

if __name__ == '__main__':

    # make_json()
    # json2csv()
    test()
