import pandas as pd
import numpy as np
import random

def main():
    # 生成模拟数据
    years = list(range(2014, 2024))
    months = list(range(1, 13))

    # 创建一个空的DataFrame
    data = []
    for year in years:
        for month in months:
            # 模拟每个月的感冒病例数（随机生成）
            cases = random.randint(50, 500)
            data.append([year, month, cases])

    # 将数据转换为DataFrame
    df = pd.DataFrame(data, columns=['年份', '月份', '感冒病例数'])

    # 保存到CSV文件
    df.to_csv(r"D:\PyDemo\T5\data\cold_cases.csv", index=False)
if __name__ == '__main__':
    main()