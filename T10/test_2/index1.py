import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 示例诊断辅助数据
data = {
    'symptom1': [1, 0, 1, 0],
    'symptom2': [0, 1, 0, 1],
    'symptom3': [1, 1, 0, 0],
    'diagnosis': [1, 0, 1, 0]
}

df = pd.DataFrame(data)

# 数据集拆分
X = df[['symptom1', 'symptom2', 'symptom3']]
y = df['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 模型训练
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 模型预测
predictions = model.predict(X_test)
print(predictions)