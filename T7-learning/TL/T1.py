import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# 读取药品销售数据
df = pd.read_csv(r"D:\PyDemo\T7-learning\data\sales_data.csv")

# 数据预处理
# 假设我们有以下特征列：日期、商品编码、商品名称、销售数量、应收金额、实收金额
# 目标变量是销售额
features = ['商品编码', '商品名称', '销售数量', '应收金额', '实收金额']
target = '销售额'

# 选择特征和目标变量
X = df[features]
y = df[target]

# 特征编码
X = pd.get_dummies(X, columns=['商品编码', '商品名称'])

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 数据标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 构建模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
y_pred_train = model.predict(X_train)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
mse2 = mean_squared_error(y_train, y_pred_train)
print(f"Mean Squared Error: %.2f"%mse)
print(f"Mean Squared Error: %.2f"%mse2)

# 保存模型
# joblib.dump(model, 'sales_prediction_model.pkl')
