import tensorflow as tf

# a = tf.placeholder(tf.int32, [3])
a = tf.placeholder(tf.int32, [None])

b = tf.constant(10)
x2_op = a * b

sess = tf.Session()

r1 = sess.run(x2_op, feed_dict={a: [1, 2, 3, 4, 5]})
print(r1)
r2 = sess.run(x2_op, feed_dict={a: [10, 20, 10]})
print(r2)
