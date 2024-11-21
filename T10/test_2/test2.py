import pandas as pd
import numpy as np

# 设置随机种子以确保结果可复现
np.random.seed(42)

# 定义时间范围
dates = pd.date_range(start='2012-01-01', end='2023-12-31', freq='D')

# 创建数据框
data = {
    '日期': np.random.choice(dates, size=10000),
    '患者ID': np.random.choice(range(1, 10001), size=10000, replace=False),
    '年龄': np.random.randint(12, 100, size=10000),
    '性别': np.random.choice(['男', '女'], size=10000),
    '症状': np.random.choice(['鼻塞', '喷嚏', '流涕', '发热', '咳嗽', '头痛'], size=10000),
    '诊断': np.random.choice(['是', '否'], size=10000, p=[0.8, 0.2])
}

df = pd.DataFrame(data)

# 添加脏数据
# 缺失值
df.loc[np.random.choice(df.index, 500, replace=False), '年龄'] = np.nan
df.loc[np.random.choice(df.index, 500, replace=False), '性别'] = np.nan
df.loc[np.random.choice(df.index, 500, replace=False), '症状'] = np.nan
df.loc[np.random.choice(df.index, 500, replace=False), '诊断'] = np.nan

# 异常值
df.loc[np.random.choice(df.index, 100, replace=False), '年龄'] = np.random.randint(101, 150, size=100)
df.loc[np.random.choice(df.index, 100, replace=False), '患者ID'] = np.random.randint(1001, 2000, size=100)

# 重复记录
df = pd.concat([df, df.sample(500, replace=True)], ignore_index=True)

# 打乱数据顺序
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# 添加额外的脏数据
# 错误的日期格式
df.at[0, '日期'] = '2014-01-01T00:00:00'
df.at[1, '日期'] = '2014/01/01'

# 错误的数据类型
df.at[2, '年龄'] = np.nan
df.at[3, '性别'] = np.nan
df.at[4, '症状'] = np.nan
df.at[5, '诊断'] = np.nan

# 保存到CSV文件
df.to_csv('cold_patient_data.csv', index=False)

# 查看前几行数据
print(df.head())
