import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# TODO 医疗预测分类
dataset = pd.read_csv("./data/Breast_cancer_data.csv")
# 根据标签diagnosis统计数据
# print(dataset['diagnosis'].value_counts()) # 1 阳性，0 阴性

X = dataset.drop('diagnosis', axis=1)
y = dataset['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, random_state=666, test_size=0.2)

# 数据归一化
sc = StandardScaler()
sc.fit(X_train, y_train)  # 拟合

X_train_scaler = sc.transform(X_train)  # 归一化
X_test_scaler = sc.transform(X_test)

# TODO 4 模型训练

import lightgbm as lgb

model = lgb.LGBMClassifier(random_state=42)  # 基础模型 不带超参数

# 方式一 基于基础模型训练
model.fit(X_train, y_train)

model2 = lgb.LGBMClassifier(random_state=42)  # 基础模型 不带超参数

# 方式二 基于归一化训练
model2.fit(X_train_scaler, y_train)

# TODO 模型预测
# 模型1
y_pred_1 = model.predict(X_test)
# 模型2
y_pred_2 = model2.predict(X_test_scaler)

# TODO 模型评估

print(accuracy_score(y_pred_1, y_test)) # 0.9385964912280702
print(accuracy_score(y_pred_2, y_test)) # 0.9210526315789473
