import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
# import random
# import re

csv = pd.read_csv('iris.csv')

csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv["Name"]

train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)

'''
def convert_float(n):
    if re.match(r'^[0-9\.]+$', n):
        return float(n)
    else:
        return n

csv = []
with open('iris.csv', 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        cols = list(map(convert_float, cols))
        csv.append(cols)

del csv[0]

random.shuffle(csv)

total_len = len(csv)
train_len = int(total_len * 2 / 3)

train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)
'''

clf = svm.SVC(gamma='auto')
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("正解率=", ac_score)
