import pandas as pd
from sklearn import model_selection, svm, metrics

train_csv = pd.read_csv("./mnist/train.csv")
test_csv = pd.read_csv("./mnist/t10k.csv")

train_label = train_csv.iloc[:, 0]
train_data = train_csv.iloc[:, 1:577]
test_label = train_csv.iloc[:, 0]
test_data = train_csv.iloc[:, 1:577]

print("学習データ数:", len(train_label))

params = [
    {"C": [1, 10, 100, 1000], "kernel": ["linear"]},
    {"C": [1, 10, 100, 1000], "kernel": ["rbf"], "gamma": [0.001, 0.0001]}
]

clf = model_selection.GridSearchCV(
    svm.SVC(), params, n_jobs=-1
)
clf.fit(train_data, train_label)
print("学習器=", clf.best_estimator_)

pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(pre, test_label)
print("正解率=", ac_score)
