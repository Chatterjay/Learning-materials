import matplotlib
import pandas as pd
import numpy as np
from fontTools.subset import subset
from matplotlib import pyplot as plt

df = pd.read_csv("data/test.csv")

df['销售额'] = df['销售额'].fillna(df['销售额'].mean())
df['日期'] = pd.to_datetime(df['日期'])
df['年'] = df['日期'].dt.year
df['月'] = df['日期'].dt.month
#  转换经济单位
df['销售额'] = (df['销售额'] / 10000).round(2)
print(df['商品类别'].value_counts())
# 按照年月分组统计销售额
total_sales_by_year_and_store = df.groupby(['年', '商品类别'])['销售额'].sum().unstack()

# 计算总共销售额
total_sales_by_year = total_sales_by_year_and_store.sum(axis=1)

# 计算销售占比
sales_ratio_by_year_and_store = (total_sales_by_year_and_store.div(total_sales_by_year, axis=0) * 100).round(2)

# 每年的销售额
print(total_sales_by_year_and_store)
# 计算每年占比
print(sales_ratio_by_year_and_store)

