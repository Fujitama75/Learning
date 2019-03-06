import pandas as pd
import numpy as np
import tensorflow as tf

csv = pd.read_csv("../ch4/bmi.csv")

csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100

# ラベルを３次元で
# thin=(0, 0, 1) ...
bclass = {
    "thin": [0, 0, 1],
    "normal": [0, 1, 0],
    "fat": [0, 0, 1]
}

csv["label_pat"] = csv["label"].apply(lambda x: np.array(bclass[x]))

test_csv = csv[15000:20000]
test_pat = test_csv[["weight", "height"]]
test_ans = list(test_csv["label_pat"])

x = tf.placeholder(tf.float32, [None, 2], name="x")  # 身長・体重
y_ = tf.placeholder(tf.float32, [None, 3], name="y_")  # ラベル

with tf.name_scope('interface') as scope:
    W = tf.Variable(tf.zeros([2, 3]), name="W")  # 重み
    b = tf.Variable(tf.zeros([3]), name="b")  # バイアス
    with tf.name_scope('softmax') as scope:
        # ソフトマックス回帰
        y = tf.nn.softmax(tf.matmul(x, W) + b)

# lossの計算
with tf.name_scope('loss') as scope:
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

with tf.name_scope('training') as scope:
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(cross_entropy)

predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

sess = tf.Session()
tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

sess.run(tf.global_variables_initializer())  # 変数初期化

for step in range(3500):
    i = (step * 100) % 14000
    rows = csv[1 + i: 1 + i + 100]
    x_pat = rows[["weight", "height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y_: y_ans}
    sess.run(train, feed_dict=fd)
    if step % 500 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
        print("step=", step, "cre=", cre, "acc=", acc)

acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
print("正解率=", acc)
