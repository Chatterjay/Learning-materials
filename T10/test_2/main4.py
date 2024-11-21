import pandas as pd

df = pd.read_excel("./朝阳医院2018年销售数据.xlsx", sheet_name='Sheet1')
df.dropna(subset=['社保卡号', '购药时间'], inplace=True)

df['购药时间'] = df['购药时间'].str.split(" ").map(lambda x: x[0])
df['购药时间'] = pd.to_datetime(df['购药时间'], errors='coerce')
df['购药时间'].dropna()
#

print(df)
