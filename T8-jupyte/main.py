import pandas as pd
from pandas import read_csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder

data_val = read_csv("./data/RandomTreeData/test.csv")
data_raw = read_csv("./data/RandomTreeData/train.csv")

data_all = [data_raw, data_val]

# TODO 列名去除大写首行
data_raw.columns = data_raw.columns.str.lower()
data_val.columns = data_val.columns.str.lower()

# TODO 绘制存活柱状图
# sns.countplot(data_raw['survived'])

# TODO 查看训练集中的空值
# print(data_raw.isnull().sum())
# print(data_val.isnull().sum())

# print(id(data_all[0]) == id(data_raw))

# TODO 对源数据集进行描述
# print(data_raw.describe(include='all'))
# print(data_raw.head())

# TODO 对原始测试集和训练集进行清洗
for dataset in data_all:
    # 补足空缺值
    dataset['age'] = dataset['age'].fillna(dataset['age'].median())
    dataset['fare'] = dataset['fare'].fillna(dataset['fare'].median())
    dataset['embarked'] = dataset['embarked'].fillna(dataset['embarked'].mode()[0])  # mode()取出现频率较高的字符返回的是数组

# 此处删除字段后会自行深拷贝一份覆盖数组中原有的
# TODO 删除缺失太多的字段
drop_columns = ['passengerid', 'ticket', 'cabin']
data_all[0] = data_all[0].drop(drop_columns, axis=1)
data_all[1] = data_all[1].drop(drop_columns, axis=1)

# TODO 特征信息构建
for dataset in data_all:
    # 构建新的字段:
    # （1）family_size 家庭规模：sibsp + parch
    dataset['family_size'] = dataset['sibsp'] + dataset['parch'] + 1  # 家庭规模默认为0加上自己
    # （2）单身 single 1:单身，0：非单身
    dataset['single'] = 1
    dataset['single'] = dataset.loc[dataset['single'] > 1] = 0  # 0：不是单身
    # （3）身份 title
    #  dataset['title'] = dataset['name'].str.split(', ',expand=True)[1].str.split('.',expand=True)[0]
    dataset['title'] = dataset['name'].apply(lambda x: x.split(",")[1]).apply(lambda x: x.split('.')[0])
    # （4）票价 fare_bin
    dataset['fare_bin'] = pd.qcut(dataset['fare'], 4)  # 根据票价，分成4组（其中每一组的元素个数一致）
    # （5）年龄 age_bin
    dataset['age_bin'] = pd.qcut(dataset['age'].astype(int), 4)  # 根据年龄分组，分成四组 （其中每一组的元素个数一致）

title_names = data_all[0]['title'].value_counts() < 10
# TODO title: 将那些称谓的人数小于10的数据，全部归为一类：other
data_all[0]['title'] = data_all[0]['title'].apply(lambda x: 'other' if title_names[x] else x)
# 计算每种身份的获救概率
data_all[0]['survived'].groupby(data_all[0]['title']).mean()

# TODO 构建新的字段，基于scikit-learn中的LabelEncoder()
label = LabelEncoder()
for dataset in data_all:
    # 将数据转换成 01 格式
    dataset['sex_code'] = label.fit_transform(dataset['sex'])
    dataset['embarked_code'] = label.fit_transform(dataset['embarked'])
    dataset['title_code'] = label.fit_transform(dataset['title'])
    dataset['age_bin_code'] = label.fit_transform(dataset['age_bin'])
    dataset['fare_bin_code'] = label.fit_transform(dataset['fare_bin'])

# TODO 训练模型
Target = ['survived']  # 标签
data_columns_one = ['sex', 'pclass', 'embarked', 'title', 'sibsp', 'parch', 'fare', 'age', 'family_size', 'single']
columns_one = Target + data_columns_one

data_one_dummy = pd.get_dummies(data_all[0][data_columns_one])
data_one_dummy_list = data_one_dummy.columns.tolist()

X_train_one, X_test_one, y_train_one, y_test_one = train_test_split(data_one_dummy[data_one_dummy_list],

                                                                    data_all[0][Target], random_state=0)

# 确保 y_train_one 是一维数组
y_train_one = y_train_one.values.ravel()

print(X_train_one.shape)
print(X_test_one.shape)

rf = RandomForestClassifier(random_state=1, n_jobs=-1)
# 网格搜索
param_gird = {
    'criterion': ['gini', 'entropy'],
    'min_samples_leaf': [1, 5, 10],
    'min_samples_split': [2, 4, 10, 12, 16],
    'n_estimators': [50, 100, 400, 700, 1000]
}
gs = GridSearchCV(estimator=rf, param_grid=param_gird, scoring='accuracy', cv=3, n_jobs=-1)

gs.fit(X_train_one, y_train_one)
# print(gs.best_score_)
#  网格中搜索最优配置
# print(gs.best_params_)

rf2 = RandomForestClassifier(criterion='entropy',
                             min_samples_leaf=5,
                             min_samples_split=16,
                             n_estimators=400)

rf2.fit(X_train_one, y_train_one)

# TODO 测试集上预测
# 根据特征重要性进行排序
# print(pd.concat((pd.DataFrame(X_train_one.iloc[:,1:].columns,columns=['Variable']),
#                  pd.DataFrame(rf2.feature_importances_,columns=['importance'])),axis=1).sort_values(by='importance',ascending=False))

pred = rf2.predict(X_test_one)
pred_df = pd.DataFrame(pred, columns=['svrived'])
print(pred_df.head())
