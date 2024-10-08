from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 糖尿病预测??
# 链接 https://www.bilibili.com/video/BV1YU411U79L?p=13

dbs = datasets.load_diabetes()
x = dbs.data
y = dbs.target
# 拆分测试集和训练集
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 多元线性回归算法
module = LinearRegression()
# 训练集训练模型
module.fit(X_train, y_train)
# 测试集预测
y_pred = module.predict(X_test)
y_pred_train = module.predict(X_train)
# 模型评估
print("均方差: %.2f" % mean_squared_error(y_test,y_pred))
print("均方差: %.2f" % mean_squared_error(y_train,y_pred_train))
