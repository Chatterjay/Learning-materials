import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 生成日期范围
start_date = datetime(2014, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# 生成商品编码和商品名称
product_codes = ['A001', 'B002', 'C003', 'D004']
product_names = ['Medicine A', 'Medicine B', 'Medicine C', 'Medicine D']

# 生成随机数据
np.random.seed(42)  # 确保结果可复现
data = {
    '日期': date_range * len(product_codes),  # 每个商品在每个日期都有记录
    '商品编码': np.repeat(product_codes, len(date_range)),
    '商品名称': np.repeat(product_names, len(date_range)),
    '销售数量': np.random.randint(0, 100, size=len(date_range) * len(product_codes)),
    '应收金额': np.random.uniform(50, 500, size=len(date_range) * len(product_codes)),
    '实收金额': np.random.uniform(40, 450, size=len(date_range) * len(product_codes)),
    '销售额': np.random.uniform(100, 1000, size=len(date_range) * len(product_codes))
}

# 创建DataFrame
df_sales = pd.DataFrame(data)

# 保存为CSV文件
df_sales.to_csv(r"./sales_data.csv", index=False)

print("Sales data generated and saved to sales_data.csv")