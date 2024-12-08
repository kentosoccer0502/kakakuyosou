import os
import pandas as pd
from jeraconv import jeraconv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np


def arrange_data(df):
    df = df.dropna(axis=0)
    j2w = jeraconv.J2W()
    list_chiku = []
    for wareki in df['建築年']:
        seireki = j2w.convert(wareki)
        list_chiku.append(2022 - seireki)
    df = df.copy()
    df['築年数'] = list_chiku
    df_area_dummy = pd.get_dummies(df['エリア'], drop_first=True)
    df_area_dummy = df_area_dummy.astype(int)
    df = pd.concat([df,df_area_dummy], axis=1)
    df = df.drop(['エリア','建築年'], axis=1)
    return df