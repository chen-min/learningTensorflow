#code = UTF-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf 
const1 = tf.constant([[2,2]])
const2 = tf.constant([[4],[4]])
multiple = tf.matmul(const1, const2)
print(multiple)
#创建一个session会话对象
sess = tf.Session()
result = sess.run(multiple)
print(result)

if const1.graph is tf.get_default_graph():
    print('const1所在的图是当前上下文默认的图')
#关闭已用完的Session
sess.close()
#第二种方法来创建和关闭session
with tf.Session() as sess:
    result2 = sess.run(multiple)
    print("multiple的结果是" , result2)
