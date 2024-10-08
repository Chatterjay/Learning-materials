# 鸢尾花数据集?
# https://www.bilibili.com/video/BV1YU411U79L?p=16

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data
y = iris.target

# test_empty_argparse(random_state='随机种子')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 创建逻辑回归对象
# LogisticRegression(max_iter='最大迭代上限默认100')
lr = LogisticRegression()
# 使用训练集训练模型
lr.fit(X_train, y_train)
# 测试集预测
y_pred = lr.predict(X_test)
# 准确率
print('准确率: %.2f'% accuracy_score(y_test,y_pred))

