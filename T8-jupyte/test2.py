import pandas as pd
import numpy as np
from matplotlib import pylab as plt

# 房屋预测价格 实践

df = pd.read_csv('./data/USA_Housing.csv')
df.columns = df.columns.str.lower()

X_test = [65000, 5, 5, 3000,200]
print(df.head())

fig = plt.figure(figsize=(10, 10))

fig1 = plt.subplot(231)
plt.scatter(df.loc[:, 'avg. area income'], df.loc[:, "price"])
plt.title('avg. area income VS Income')

fig2 = plt.subplot(232)
plt.scatter(df.loc[:, 'avg. area house age'], df.loc[:, "price"])
plt.title('avg. area house age VS Income')

fig3 = plt.subplot(233)
plt.scatter(df.loc[:, 'avg. area number of rooms'], df.loc[:, "price"])
plt.title('number of rooms VS Income')

fig4 = plt.subplot(234)
plt.scatter(df.loc[:, 'area population'], df.loc[:, "price"])
plt.title('area population VS Income')

# fig5 = plt.subplot(235)
# plt.scatter(df.loc[:, 'avg. area number of bedrooms'], df.loc[:, "price"])
# plt.title('avg. area number of bedrooms VS Income')

# plt.show()

# region 单因子预测

# region 多因子预测
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = df.loc[:, "avg. area number of rooms"]
y = df.loc[:, 'price']

# 要求二维数组
X = np.array(X).reshape(-1, 1)

lr1 = LinearRegression()
lr1.fit(X, y)
# 预测原始数据
y_pred1 = lr1.predict(X)
mse = mean_squared_error(y, y_pred1)
r2 = r2_score(y, y_pred1)

print(mse, r2)
fig6 = plt.figure(figsize=(10, 10))
plt.scatter(X, y)
plt.plot(X, y_pred1, 'r')
# plt.show()
# endregion

X_multi = df.drop(['price', 'address'], axis=1)
# print(X_multi)
# 创建线性回归模型
lr2 = LinearRegression()
lr2.fit(X_multi, y)
y_pred2 = lr2.predict(X_multi)
mse2 = mean_squared_error(y, y_pred2)
r22 = r2_score(y, y_pred2)
print(mse2, r22)

# 展示
plt.figure(figsize=(8, 5))
plt.scatter(y, y_pred2)
# plt.show()

# 测试数据
# 维度转换
X_test = np.array(X_test).reshape(1,-1)
# print(X_test.shape)
y_test_pred = lr2.predict(X_test)
print(y_test_pred)
# endregion
