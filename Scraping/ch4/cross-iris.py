import pandas as pd
from sklearn import svm, metrics, model_selection
# import random
# import re

csv = pd.read_csv('iris.csv')

data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]

clf = svm.SVC(gamma="auto")
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("各正解率=", scores)
print("正解率=", scores.mean())
