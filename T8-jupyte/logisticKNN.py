# KNN实战 有监督式
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 读取数据集并进行预处理
df = pd.read_csv("./data/kmeans_blobs.csv")
df.columns = df.columns.str.lower()
df.drop('id', axis=1, inplace=True)
df.columns = ['test1', 'test2', 'cluster']

# 分离特征和标签
X = df.drop('cluster', axis=1)
y = df['cluster']

# 初始化K近邻分类器，设置邻居数为3
knn = KNeighborsClassifier(n_neighbors=3)
# 使用特征和标签拟合模型
knn.fit(X, y)
# 进行预测
y_pred = knn.predict(X)

# 计算预测准确率
acc = accuracy_score(y, y_pred)
print("KNN accuracy: ", acc)
# 输出预测结果和真实标签的价值计数
print(pd.Series(y_pred).value_counts(), pd.Series(y).value_counts())
# 对新数据进行预测
print(knn.predict([[30, 20]]))

# 绘制散点图，展示不同预测簇的数据分布
fig = plt.figure()
sc0 = plt.scatter(df['test1'][y_pred == 0], df['test2'][y_pred == 0])
sc1 = plt.scatter(df['test1'][y_pred == 1], df['test2'][y_pred == 1])
sc2 = plt.scatter(df['test1'][y_pred == 2], df['test2'][y_pred == 2])
plt.legend((sc0, sc1, sc2), ('sc0', 'sc1', 'sc2'))
plt.title('KNN-test1-test2')
plt.xlabel("test1")
plt.ylabel("test2")
plt.show()
