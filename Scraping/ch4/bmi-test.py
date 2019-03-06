from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("bmi.csv")

label = tbl["label"]
# 正規化
w = tbl["weight"] / 100
h = tbl["height"] / 200
wh = pd.concat([w, h], axis=1)

train_data, test_data, train_label, test_label = \
    train_test_split(wh, label)

clf = svm.SVC(gamma="auto")
# clf = svm.LinearSVC()
clf.fit(train_data, train_label)

pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
cl_report = metrics.classification_report(test_label, pre)
print("正解率=", ac_score)
print("レポート=\n", cl_report)
