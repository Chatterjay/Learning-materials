# 逻辑回归 回归预测学生考试通过
from tkinter.messagebox import showerror

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 读取考试数据
df = pd.read_csv("./data/examdata.csv")
# 将列名转换为小写
df.columns = df.columns.str.lower()

# fig1 = plt.figure()
# plt.scatter(df.loc[:, 'exam1'], df.loc[:, 'exam2'])
# plt.title("exam1-exam2")
# plt.xlabel('exam1')
# plt.ylabel('exam2')
# plt.show()

# 创建一个掩码，用于区分通过和未通过的学生
mask = df.loc[:, 'pass'] == 1
# 取反 取出pass=0的
# print(~mask)
# fig2 = plt.figure()
# passed = plt.scatter(df.loc[:, 'exam1'][mask], df.loc[:, 'exam2'][mask])
# failed = plt.scatter(df.loc[:, 'exam1'][~mask], df.loc[:, 'exam2'][~mask])
# plt.title("exam1-exam2")
# plt.xlabel('exam1')
# plt.ylabel('exam2')
# plt.legend((passed, failed), ('passed', 'failed'))
# plt.show()

# 准备数据进行逻辑回归分析
X = df.drop('pass', axis=1)
X1 = df['exam1']
X2 = df['exam2']
y = df.loc[:, 'pass']

# 训练模型
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
# print(X.shape,y.shape)
lr.fit(X, y)

#  预测 结果和评估表现
y_pred = lr.predict(X)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y, y_pred)
print(accuracy)

# print(lr.predict([[70,65]]))
# print(lr.coef_)
# print(lr.intercept_)
theta0 = lr.intercept_
theta1, theta2 = lr.coef_[0][0], lr.coef_[0][1]
# print(theta0, theta1, theta2)

# 计算决策边界
X2_new = -(theta0 + theta1 * X1) / theta2
# print(X2_new)
# fig3 = plt.figure()
#
# passed = plt.scatter(df.loc[:, 'exam1'][mask], df.loc[:, 'exam2'][mask])
# failed = plt.scatter(df.loc[:, 'exam1'][~mask], df.loc[:, 'exam2'][~mask])
# plt.title("exam1-exam2")
# plt.xlabel('exam1')
# plt.ylabel('exam2')
# plt.legend((passed, failed), ('passed', 'failed'))
# plt.plot(X1,X2_new)
# plt.show()

# 添加二次特征以提高模型性能
X1_2 = X1 * X1
X2_2 = X2 * X2
X1_X2 = X1 * X2

X_new = {"X1": X1, "X2": X2, 'X1_2': X1_2, 'X2_2': X2_2, 'X1_X2': X1_X2}
X_new = pd.DataFrame(X_new)

# 使用新的特征训练逻辑回归模型
lr2 = LogisticRegression()
lr2.fit(X_new, y)
y2_pred = lr2.predict(X_new)
accuracy2 = accuracy_score(y, y2_pred)

X1_new = X1.sort_values()

print(accuracy2)
theta0 = lr2.intercept_
theta1, theta2, theta3, theta4, theta5 = lr2.coef_[0][0], lr2.coef_[0][1], lr2.coef_[0][2], lr2.coef_[0][3], \
    lr2.coef_[0][4]
a = theta4
b = theta5 * X1_new + theta2
c = theta0 + theta1 * X1_new + theta3 * X1_new * X1_new

# 计算新的决策边界
X2_new_boundary = (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
print(X2_new_boundary)
fig4 = plt.figure()
passed = plt.scatter(df.loc[:, 'exam1'][mask], df.loc[:, 'exam2'][mask])
failed = plt.scatter(df.loc[:, 'exam1'][~mask], df.loc[:, 'exam2'][~mask])
plt.title("exam1-exam2")
plt.xlabel('exam1')
plt.ylabel('exam2')
plt.legend((passed, failed), ('passed', 'failed'))
plt.plot(X1_new, X2_new_boundary)
plt.show()
