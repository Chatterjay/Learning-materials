from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

# 加载数据集
newgroups_train = fetch_20newsgroups(subset='train')
newgroups_test = fetch_20newsgroups(subset='test')

pipeline = make_pipeline(CountVectorizer(),LogisticRegression(max_iter=3000))

pipeline.fit(newgroups_train.data,newgroups_train.target)

y_pred = pipeline.predict(newgroups_test.data)
print(accuracy_score(newgroups_test.target,y_pred))