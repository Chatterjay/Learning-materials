import pandas as pd
import numpy as np
from datetime import datetime, timedelta
def main():

    # 设置随机种子以获得可重复的结果
    np.random.seed(42)

    # 生成日期范围（从2014-01-01到2023-12-31）
    start_date = datetime(2014, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # 定义药品类型列表
    medicine_types = ['中成药', '西药']

    # 创建空的DataFrame
    data = {
        '日期': [],
        '药品类型': [],
        '销售额': []
    }

    # 填充数据
    for single_date in date_range:
        for med_type in medicine_types:
            # 随机生成每日销售额，假设平均每天销售额在1000到5000之间
            sales = round(np.random.uniform(1000, 5000), 2)
            data['日期'].append(single_date)
            data['药品类型'].append(med_type)
            data['销售额'].append(sales)

    # 将字典转换为DataFrame
    df = pd.DataFrame(data)

    # 打乱数据顺序以模拟真实情况
    df = df.sample(frac=1).reset_index(drop=True)

    # 保存为CSV文件
    output_path = 'mds.csv'
    df.to_csv(output_path, index=False, encoding='utf-8-sig')

    print(f"数据已保存至 {output_path}")
if __name__ == '__main__':
    main()