import pandas as pd

from matplotlib import pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth

df = pd.read_csv('../data/testSet.csv')
X_test = pd.read_csv('../data/testSet2.csv')

df.columns = df.columns.str.lower()
X_test.columns = X_test.columns.str.lower()
X = df

# fig = plt.subplot(121)
# plt.scatter(df['v1'], df['v2'])
# fig2 = plt.subplot(122)
# plt.scatter(X_test['v1'], X_test['v2'])

bw = estimate_bandwidth(X, n_jobs=-1, n_samples=10)
ms = MeanShift(bandwidth=bw, n_jobs=-1)
ms.fit(X)
y_pred = ms.predict(X)

fig1 = plt.subplot(221)
sc0 = plt.scatter(X['v1'], X['v2'])
plt.xlabel('v1')
plt.ylabel('v2')
plt.title("raw-v1-v2")

fig2 = plt.subplot(222)
sc0 = plt.scatter(X['v1'][y_pred == 0], X['v2'][y_pred == 0])
sc1 = plt.scatter(X['v1'][y_pred == 1], X['v2'][y_pred == 1])
sc2 = plt.scatter(X['v1'][y_pred == 2], X['v2'][y_pred == 2])
sc3 = plt.scatter(X['v1'][y_pred == 3], X['v2'][y_pred == 3])
plt.legend((sc0, sc1, sc2), ('sc0', 'sc1', 'sc2'))
plt.xlabel('v1')
plt.ylabel('v2')
plt.title("predict-v1-v2")

y_pred2 = ms.predict(X_test)

fig3 = plt.subplot(223)
sc0 = plt.scatter(X_test['v1'], X_test['v2'])
plt.xlabel('v1')
plt.ylabel('v2')
plt.title("predict-raw-v1-v2")

fig4 = plt.subplot(224)
sc0 = plt.scatter(X_test['v1'][y_pred2 == 0], X_test['v2'][y_pred2 == 0])
sc1 = plt.scatter(X_test['v1'][y_pred2 == 1], X_test['v2'][y_pred2 == 1])
sc2 = plt.scatter(X_test['v1'][y_pred2 == 2], X_test['v2'][y_pred2 == 2])
sc3 = plt.scatter(X_test['v1'][y_pred2 == 3], X_test['v2'][y_pred2 == 3])
plt.legend((sc0, sc1, sc2), ('sc0', 'sc1', 'sc2'))
plt.xlabel('v1')
plt.ylabel('v2')
plt.title("predict-test-v1-v2")
plt.show()
