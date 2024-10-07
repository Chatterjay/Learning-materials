import pandas as pd
import numpy as np

# 定义年份范围
years = list(range(2014, 2024))

# 生成每个月的数据
months = [f'{y}-{m:02d}' for y in years for m in range(1, 13)]

# 生成随机的销售额数据
np.random.seed(0)  # 设置随机种子以保证每次运行结果一致
traditional_chinese_medicine_sales = np.random.randint(1000, 5000, size=len(months))
western_medicine_sales = np.random.randint(2000, 6000, size=len(months))

# 创建 DataFrame
data = {
    'YearMonth': months,
    'TraditionalChineseMedicineSales': traditional_chinese_medicine_sales,
    'WesternMedicineSales': western_medicine_sales
}

df = pd.DataFrame(data)

# 将数据保存为 CSV 文件
df.to_csv('medicine_sales_data.csv', index=False)

# 打印前几行数据
print(df.head())