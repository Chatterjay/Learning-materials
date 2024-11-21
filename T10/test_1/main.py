from idlelib.iomenu import errors, encoding
from operator import index

import pandas as pd

df = pd.read_excel("朝阳医院2018年销售数据.xlsx", sheet_name="Sheet1")

df.rename(columns={'购药时间': '销售时间'}, inplace=True)
df.dropna(inplace=True)
df[['销售数量', '应收金额', '实收金额']] = df[['销售数量', '应收金额', '实收金额']].astype(float)
df['销售时间'] = df['销售时间'].str.split(" ").map(lambda x: x[0])
df['销售时间'] = pd.to_datetime(df['销售时间'], errors='coerce')
df.dropna(subset=['销售时间', '社保卡号'], inplace=True)
df = df.sort_values(by=['销售时间']).reset_index(drop=True)
df = df[(df['销售数量'] > 0) & (df['应收金额'] > 0) & (df['实收金额'] > 0)]

df.to_csv('data.csv', index=False)
print(df.head())
print(df.isnull().sum())
print(df.dtypes)
