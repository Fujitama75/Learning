import pandas as pd
from sklearn import svm, metrics

xor_input = [
    # P Q result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
'''
data = []
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)
'''

xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.iloc[:, [0, 1]]
xor_label = xor_df.iloc[:, 2]

clf = svm.SVC(gamma='auto')
clf.fit(xor_data, xor_label)

pre = clf.predict(xor_data)
# print("予測結果:", pre)

ac_score = metrics.accuracy_score(xor_label, pre)
print("正解率=", ac_score)
'''
ok = 0
total = 0

for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
    total += 1
print("正解率:", ok, "/", total, "=", ok/total)
'''
