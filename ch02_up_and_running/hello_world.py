import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
print(tf.__version__)

h = tf.constant('Hello')
w = tf.constant(' World!')
hw = h + w

print(hw)

with tf.Session() as sess:
    ans = sess.run(hw)

print(ans)