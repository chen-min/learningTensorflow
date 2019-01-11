#code = UTF-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

hw = tf.constant("test, tensorflow~~~~~~~~~~~~~")

#启动一个tensorflow的session
sess = tf.Session()
#Y运行graph
print(sess.run(hw))

sess.close()