# KMeanShift实战 有监督式
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth

# 读取数据集并进行预处理
df = pd.read_csv("./data/kmeans_blobs.csv")
df.columns = df.columns.str.lower()
df.drop('id', axis=1, inplace=True)
df.columns = ['test1', 'test2', 'cluster']

# 分离特征和标签
X = df.drop('cluster', axis=1)
y = df['cluster']

# 估计带宽，用于MeanShift算法
bw = estimate_bandwidth(X, n_samples=50)

# 初始化MeanShift模型并进行训练
ms = MeanShift(bandwidth=bw, n_jobs=-1)
ms.fit(X)

# 预测数据点的簇标签
y_pred = ms.predict(X)

# 根据预测的簇标签，转换为原始标签的表示方式
y_corrected = []
for i in y_pred:
    if i == 0:
        y_corrected.append(2)
    elif i == 1:
        y_corrected.append(1)
    else:
        y_corrected.append(0)

y_corrected = np.array(y_corrected)

# 绘制MeanShift算法处理后的数据分布图
fig = plt.subplot(122)
sc0 = plt.scatter(df['test1'][y_corrected == 0], df['test2'][y_corrected == 0])
sc1 = plt.scatter(df['test1'][y_corrected == 1], df['test2'][y_corrected == 1])
sc2 = plt.scatter(df['test1'][y_corrected == 2], df['test2'][y_corrected == 2])
plt.legend((sc0, sc1, sc2), ('sc0', 'sc1', 'sc2'))
plt.title("KMeanShift-test1-test2")
plt.xlabel("test1")
plt.ylabel("test2")

# 绘制原始数据分布图
fig2 = plt.subplot(121)
sc0 = plt.scatter(df['test1'][y == 0], df['test2'][y == 0])
sc1 = plt.scatter(df['test1'][y == 1], df['test2'][y == 1])
sc2 = plt.scatter(df['test1'][y == 2], df['test2'][y == 2])
plt.legend((sc0, sc1, sc2), ('sc0', 'sc1', 'sc2'))
plt.title("Raw-test1-test2")
plt.xlabel("test1")
plt.ylabel("test2")
plt.show()
