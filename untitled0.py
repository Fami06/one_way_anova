import pandas as pd
from scipy.stats import f_oneway

# データの定義
data1 = [2.761, 2.295, 2.934, 2.579, 2.028, 2.459, 2.872, 2.879, 2.972, 3.12, 3.133]
data2 = [2.739, 2.485, 2.89, 3.061, 3.15, 2.518, 3.362, 2.682, 3.039, 3.121, 3.351]
data3 = [3.806, 3.349, 3.619, 3.567, 3.42, 3.419, 3.501, 3.566, 3.527, 3.539, 3.633]
data4 = [3.439, 3.457, 3.406, 3.083, 3.303, 3.208, 3.323, 3.387, 3.39, 3.466, 3.57]
data5 = [3.445, 3.473, 3.204, 3.726, 3.697, 3.397, 3.649, 3.654, 3.644, 3.559, 3.773]
data6 = [3.609, 3.284, 3.34, 3.212, 3.575, 3.56, 3.549, 3.683, 3.627, 3.481, 3.679]

# データをデータフレームにまとめる
df = pd.DataFrame({
    'Time1': data1,
    'Time2': data2,
    'Time3': data3,
    'Time4': data4,
    'Time5': data5,
    'Time6': data6
})

import scipy.stats as stats

# Repeated Measures ANOVAの実行
F_value, p_value = stats.f_oneway(df['Time1'], df['Time2'], df['Time3'], df['Time4'], df['Time5'], df['Time6'])

print(f'F値: {F_value}')
print(f'p値: {p_value}')

