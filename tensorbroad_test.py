#code = UTF-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf 
 #构造图的结构>>> 用一个线性方程的例子 y = W*x +b

W = tf.Variable(2.0, dtype=tf.float32, name="Weight") #权重
b = tf.Variable(1.0, dtype=tf.float32, name="Bias")  #偏差
x = tf.placeholder(dtype=tf.float32, name="Input") #输入
with tf.name_scope("Output") :  #输出的命名空间
    y = W * x + b

const = tf.constant(2.0) #不需要初始化
#定义保存日志的路径
path = "./log"

#创建用于初始化所有变量(variable)的操作
init = tf.global_variables_initializer()

#创建会话
with tf.Session() as sess:
    sess.run(init)  #实现初始化变量
    writer = tf.summary.FileWriter(path, sess.graph)
    result = sess.run(y, {x: 3.0})
    print("y=%s" %result) #打印y=w*x+b的值



