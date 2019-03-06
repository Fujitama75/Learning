import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mr = pd.read_csv("mushroom.csv", header=None)

label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row.iloc[0])
    row_data = []
    for v in row.iloc[1:]:
        # ord: ASCIIコードに変換
        row_data.append(ord(v))
    data.append(row_data)

train_data, test_data, train_label, test_label = \
    train_test_split(data, label)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(train_data, train_label)

pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
cl_report = metrics.classification_report(test_label, pre)
print("正解率=", ac_score)
print("レポート=\n", cl_report)
