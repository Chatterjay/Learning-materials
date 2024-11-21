import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("data/WALMART_SALES_DATA.csv")
df.duplicated().sum()
df.describe()
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")
df["Year"] = df['Date'].dt.year
df["Month"] = df['Date'].dt.month
df = df[(df['Store'] == 1) | (df['Store'] == 2) | (df['Store'] == 3) | (df['Store'] == 4)]
df['Store'].unique()
df['Weekly_Sales'] = (df['Weekly_Sales'] / 10000).round(2)  # 转换成万单位保留两位小数点

# 按年和商店分组计算总销售额
total_sales_by_year_and_store = df.groupby(["Year", "Store"])['Weekly_Sales'].sum().unstack().fillna(0)
# 计算每一年所有商店的总销售额
total_sales_by_year = total_sales_by_year_and_store.sum(axis=1)
# 计算每个商店在每一年的销售额占比
sales_ratio_by_year_and_store = (total_sales_by_year_and_store.div(total_sales_by_year, axis=0) * 100).round(2)
# 打印结果

print("每一年每个商店的总销售额:")
print(total_sales_by_year_and_store)

print("每一年每个商店的销售额占比:")
print(sales_ratio_by_year_and_store)
