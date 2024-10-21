# KMeans实战 2D算法自动聚类 无监督式
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# 读取数据集并进行预处理
df = pd.read_csv("./data/kmeans_blobs.csv")
df.columns = df.columns.str.lower()
df.drop('id', axis=1, inplace=True)
df.columns = ['test1', 'test2', 'cluster']

# 分离特征和标签
X = df.drop('cluster', axis=1)
y = df['cluster']

# 初始化KMeans模型并进行拟合
km = KMeans(n_clusters=3, random_state=0)
km.fit(X)

# 获取聚类中心和预测标签
centers_ = km.cluster_centers_
y_pred = km.predict(X)

# 绘制原始数据分布图
fig2 = plt.subplot(121)
scatter0 = plt.scatter(df['test1'][df['cluster'] == 0], df['test2'][df['cluster'] == 0])
scatter1 = plt.scatter(df['test1'][df['cluster'] == 1], df['test2'][df['cluster'] == 1])
scatter2 = plt.scatter(df['test1'][df['cluster'] == 2], df['test2'][df['cluster'] == 2])
plt.xlabel("test1")
plt.ylabel("test2")
plt.title('raw-test1-test2')
plt.legend((scatter0, scatter1, scatter2), ('scatter0', 'scatter1', 'scatter2'))

# 绘制预测数据分布图
fig3 = plt.subplot(122)
scatter0 = plt.scatter(df['test1'][y_pred == 0], df['test2'][y_pred == 0])
scatter1 = plt.scatter(df['test1'][y_pred == 1], df['test2'][y_pred == 1])
scatter2 = plt.scatter(df['test1'][y_pred == 2], df['test2'][y_pred == 2])
plt.xlabel("test1")
plt.ylabel("test2")
plt.title('predict-test1-test2')
plt.scatter(centers_[:, 0], centers_[:, 1])
plt.legend((scatter0, scatter1, scatter2), ('scatter0', 'scatter1', 'scatter2'))

# 对预测标签进行修正以匹配真实标签
y_corrected = []
for i in y_pred:
    if i == 0:
        y_corrected.append(1)
    elif i == 1:
        y_corrected.append(2)
    else:
        y_corrected.append(0)

# 计算修正后的预测标签与真实标签之间的准确率
acc = accuracy_score(y, y_corrected)
y_corrected = np.array(y_corrected)
print(acc)  # 1.0

# 绘制修正后的预测数据分布图
fig4 = plt.figure()
scatter0 = plt.scatter(df['test1'][y_corrected == 0], df['test2'][y_corrected == 0])
scatter1 = plt.scatter(df['test1'][y_corrected == 1], df['test2'][y_corrected == 1])
scatter2 = plt.scatter(df['test1'][y_corrected == 2], df['test2'][y_corrected == 2])
plt.xlabel("test1")
plt.ylabel("test2")
plt.title('predict2-test1-test2')
plt.scatter(centers_[:, 0], centers_[:, 1])
plt.legend((scatter0, scatter1, scatter2), ('scatter0', 'scatter1', 'scatter2'))

# 使用训练好的模型进行新的预测
print(km.predict([[30, 20]]))  # 此处是未校正的预测结果
plt.show()
