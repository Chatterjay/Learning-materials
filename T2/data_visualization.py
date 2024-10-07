import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 设置随机种子以确保结果可复现
np.random.seed(42)

# 生成日期范围
start_date = datetime(2014, 1, 1)  # 起始日期为2014年1月1日
end_date = datetime(2023, 12, 31)  # 结束日期为2023年12月31日
date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]  # 生成从起始到结束的所有日期

# 生成药品类型
medicine_types = ['中成药', '西药']

# 生成测试数据
data = {
    '销售时间': np.random.choice(date_range, size=10000),  # 随机选择10000个日期
    '药品类型': np.random.choice(medicine_types, size=10000),  # 随机选择药品类型
    '销售额': np.random.uniform(10, 1000, size=10000)  # 生成10000个介于10到1000之间的浮点数作为销售额
}

# 创建DataFrame
df_trend = pd.DataFrame(data)

# 查看生成的测试数据
print(df_trend.head())

# 将生成的数据保存到CSV文件
output_file_path_trend = r'./药品消费数据.csv'
df_trend.to_csv(output_file_path_trend, index=False, encoding='utf-8-sig')
print(f"药品消费趋势分析数据已保存至: {output_file_path_trend}")