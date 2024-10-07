import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 设置随机种子以确保结果可复现
np.random.seed(42)

# 生成日期范围
start_date = datetime(2020, 1, 1)  # 起始日期为2020年1月1日
end_date = datetime(2023, 12, 31)  # 结束日期为2023年12月31日
date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]  # 生成从起始到结束的所有日期

# 生成社保卡号
social_security_numbers = [f"SSN{str(i).zfill(5)}" for i in range(1, 101)]  # 生成100个社保卡号，格式为SSN00001到SSN00100

# 生成商品编码和名称
product_codes = [f"P{i}" for i in range(1, 10)]  # 生成9个商品编码，格式为P1到P9
product_names = [f"Product {i}" for i in range(1, 10)]  # 生成9个商品名称，格式为Product 1到Product 9

# 生成测试数据
data = {
    '购药时间': [d.strftime('%Y-%m-%d %A') for d in np.random.choice(date_range, size=1000)],  # 生成包含日期和星期几的字符串
    '社保卡号': np.random.choice(social_security_numbers, size=1000),  # 随机选择1000个社保卡号
    '商品编码': np.random.choice(product_codes, size=1000),  # 随机选择1000个商品编码
    '商品名称': np.random.choice(product_names, size=1000),  # 随机选择1000个商品名称
    '销售数量': np.random.randint(1, 100, size=1000),  # 生成1000个介于1到100之间的整数作为销售数量
    '应收金额': np.random.uniform(10, 1000, size=1000),  # 生成1000个介于10到1000之间的浮点数作为应收金额
    '实收金额': np.random.uniform(10, 1000, size=1000)   # 生成1000个介于10到1000之间的浮点数作为实收金额
}

# 创建DataFrame
df = pd.DataFrame(data)

# 添加一些缺失值
df.loc[np.random.choice(df.index, size=100), '购药时间'] = np.nan  # 在'购药时间'列中随机选择100行设置为NaN
df.loc[np.random.choice(df.index, size=100), '社保卡号'] = np.nan  # 在'社保卡号'列中随机选择100行设置为NaN
df.loc[np.random.choice(df.index, size=100), '商品编码'] = np.nan  # 在'商品编码'列中随机选择100行设置为NaN
df.loc[np.random.choice(df.index, size=100), '商品名称'] = np.nan  # 在'商品名称'列中随机选择100行设置为NaN
df.loc[np.random.choice(df.index, size=100), '销售数量'] = np.nan  # 在'销售数量'列中随机选择100行设置为NaN
df.loc[np.random.choice(df.index, size=100), '应收金额'] = np.nan  # 在'应收金额'列中随机选择100行设置为NaN
df.loc[np.random.choice(df.index, size=100), '实收金额'] = np.nan  # 在'实收金额'列中随机选择100行设置为NaN

# 添加一些异常值
df.loc[np.random.choice(df.index, size=50), '销售数量'] = -1  # 在'销售数量'列中随机选择50行设置为-1
df.loc[np.random.choice(df.index, size=50), '应收金额'] = -1  # 在'应收金额'列中随机选择50行设置为-1
df.loc[np.random.choice(df.index, size=50), '实收金额'] = -1  # 在'实收金额'列中随机选择50行设置为-1

# 查看生成的测试数据
# print(df.head())
path = r'./TestData.csv'
df.to_csv(path,index=False,encoding='utf-8-sig')