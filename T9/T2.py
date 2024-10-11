import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 定义字体
mpl.rcParams['font.family'] = ['sans-serif']
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

df = read_csv('./data/BostonHousing.csv')

# 自变量数据
X = df.drop(['medv'], axis=1)
# 因变量数据
y = df['medv']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.6, random_state=30)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 多元线性回归模型的评估 RMSE--均方差根，数值越小说明拟合度越高
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(mean_squared_error(y_test, y_pred))
print("MSE: ", MSE)
print("RMSE: ", RMSE)

plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.xlabel('真实')
plt.ylabel('预测')
plt.show()
