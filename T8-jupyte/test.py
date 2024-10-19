import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# 单因子训练模型

df = pd.read_csv(r'./data/12.csv')
# 一维数组
x = df.loc[:, 'x']
y = df.loc[:, 'y']

plt.figure()
plt.scatter(x, y)

# 转换二维数组
import numpy as np

x = np.array(x)
x = x.reshape(-1, 1)
y = np.array(y)
y = y.reshape(-1, 1)

lr_model = LinearRegression()
# print(type(x), x.shape,type(y),y.shape)
# 训练模型
lr_model.fit(x, y)  # 需要二维数组
y_pred = lr_model.predict(x)

# 预测
y_3 = lr_model.predict([[3.5]])
print(y_3)

a = lr_model.coef_
b = lr_model.intercept_
print(a, b)  # [[2.]] [5.] == y = 2x + 5
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
# mse 越接近0 r2越接近1
print(mse, r2)

# 评估模型
