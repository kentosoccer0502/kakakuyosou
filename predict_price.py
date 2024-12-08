import os
import pandas as pd
from sklearn.linear_model import LinearRegression

from utils import arrange_data


def predict_price(room_size, distance, years, area):
    main_path = os.path.dirname(os.path.abspath(__file__))
    dataset_file_path = os.path.join(main_path, "dataset")
    os.chdir(dataset_file_path)
    file = "仮想マンション価格.xlsx"
    df = pd.read_excel(file)
    df = arrange_data(df)
    y = df[['価格(千円)']]
    x = df[['広さ', '距離（分）', '築年数', 'B','C']]
    if area == 'A':
        is_areaB = 0
        is_areaC = 0
    elif area == 'B':
        is_areaB = 1
        is_areaC = 0
    elif area == 'C':
        is_areaB = 0
        is_areaC = 1
    else: 
        print('エリアニアはA,B,C以外が入力されています')
    
    x_train = x
    y_train = y
    x_test = pd.DataFrame(
        [[room_size, distance, years, is_areaB, is_areaC]],
        columns=['広さ', '距離（分）', '築年数', 'B', 'C'],
    )
    print(x_test)
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    y_pred = y_pred.tolist()
    y_pred = y_pred[0][0]
    y_pred = round(y_pred, 0)
    y_pred = int(y_pred)
    print('予想価格：', y_pred, '千円')
    return y_pred



