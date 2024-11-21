import numpy as np
import pandas as pd

df = pd.read_csv('data/cold_patient_data.csv')
# 分离时间
df['日期'] = pd.to_datetime(df['日期'])
df['年'] = df['日期'].dt.year
df['月'] = df['日期'].dt.month
# 排序
df = df.sort_values(['年', '月'], ascending=True).reset_index(drop=True)
# 填补症状数据
print(df['患者ID'].unique())

df['年龄'] = df['年龄'].fillna(df['年龄'].mean())
df['性别'] = df['性别'].fillna(df['性别'].mode()[0])
df['症状'] = df['症状'].fillna(df['症状'].mode()[0])
df = df[df['诊断'] == '是']
# 无重复人员
df = df.drop_duplicates(subset=['患者ID'])

# 根据年月统计感冒的人数
monthly_counts  = df.groupby(['年', '月']).size().unstack().fillna(0)
print(monthly_counts)

print(monthly_counts.index.tolist())
print(monthly_counts.columns.tolist())
heatmap_data2 = []
for year in monthly_counts.index:
    for month in monthly_counts.columns:
        value = monthly_counts.loc[year, month]
        heatmap_data2.append([str(year), str(month), int(value)])
print(heatmap_data2)
