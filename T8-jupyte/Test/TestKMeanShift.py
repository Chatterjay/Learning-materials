# 导入必要的库
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth

# 读取聚类数据集
df = pd.read_csv("../data/cluster_data.csv")
# 将列名转换为小写
df.columns = df.columns.str.lower()
# 重命名列名为'test1'和'test2'
df.columns = ['test1', 'test2']

# 将数据框赋值给X，作为特征数据
X = df

# 创建子图，绘制原始数据的散点图
fig = plt.subplot(121)
plt.scatter(df['test1'], df['test2'])
plt.xlabel("test1")
plt.ylabel("test2")

# 估计带宽，用于MeanShift算法
bw = estimate_bandwidth(X, n_jobs=-1, n_samples=10)

# 创建MeanShift对象并进行模型训练
ms = MeanShift(bandwidth=bw, n_jobs=-1)
ms.fit(X)
# 预测数据点的簇标签
y_pred = ms.predict(X)

# 打印每个簇的样本数量
print(pd.Series(y_pred).value_counts())

# 再次创建子图，根据预测的簇绘制数据点
fig2 = plt.subplot(122)
sc0 = plt.scatter(df['test1'][y_pred == 0], df['test2'][y_pred == 0])
sc1 = plt.scatter(df['test1'][y_pred == 1], df['test2'][y_pred == 1])
# 添加图例
plt.legend((sc0, sc1), ("sc0", 'sc1'))
plt.xlabel("test1")
plt.ylabel("test2")

print(ms.predict([[10, -3]]))
# 显示图形
plt.show()
