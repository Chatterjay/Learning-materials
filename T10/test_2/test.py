import pandas as pd
import numpy as np
import random

# 设置时间范围
dates = pd.date_range(start='2013-01-01', end='2022-12-31', freq='MS')

# 创建商品类别
categories = ['中成药', '西药']

# 生成销售数据
data = {
    '日期': dates,
    '商品类别': np.random.choice(categories, len(dates)),
    '销售量': np.random.randint(100, 1000, len(dates)),  # 随机生成销售量
    '销售额': np.random.randint(1000, 10000, len(dates))  # 随机生成销售额
}

# 添加脏数据
def add_dirty_data(df):
    # 随机添加重复销售记录
    df_duplicates = df.duplicated('日期', keep=False).sample(frac=0.1).index
    df.loc[df_duplicates, '销售额'] *= 2  # 假设重复销售额加倍作为脏数据表现
    # 添加缺失值
    df = df.dropna()  # 删除原有缺失值，为了演示添加缺失值的脏数据效果，这里先删除缺失值再添加新的缺失值
    df.loc[np.random.choice(df.index, 5), '销售额'] = np.nan  # 随机添加缺失值到销售额字段中
    return df

# 生成带有脏数据的销售数据集
df = pd.DataFrame(data)
df = add_dirty_data(df)  # 添加脏数据模拟真实场景中的异常情况和数据波动。这里只是简单的演示，您可以根据需要自定义脏数据的类型和比例。最终的脏数据生成需要根据实际应用场景进行定制。如果您需要更复杂的脏数据生成逻辑，请告诉我具体需求。生成的脏数据可能包括重复记录、缺失值、异常值等。这些脏数据可以模拟真实场景中的异常情况和数据波动。在实际应用中，您需要根据具体需求和数据质量要求进行适当的清洗和预处理。生成的脏数据仅用于模拟真实场景，不代表实际业务场景中的真实数据质量。请确保在使用前进行适当的数据清洗和验证。如果您需要进一步的帮助或指导，请随时告诉我。您可以根据实际需求调整代码中的参数和逻辑来生成符合您需求的数据集。
df.to_csv('test.csv',index=False)