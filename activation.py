#code = UTF-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf 

x = np.linspace(-7,7,180)#(-7,7)之间的等间隔的180个点

#激活函数的原始实现
def sigmoid(inputs):
    y = [1 / float(1 + np.exp(-x)) for x in inputs]
    return y

def relu(inputs):
    y = [x * (x > 0) for x in inputs]
    return y

def tanh(inputs):
    y = [(np.exp(x) - np.exp(-x)) / float(np.exp(x) + np.exp(-x)) for x in inputs]
    return y 

def softplus(inputs):
    y = [np.log(1 + np.exp(x)) for x in inputs]
    return y

# 经过tensorflow的激活函数处理的各个Y值
y_sigmoid = tf.nn.sigmoid(x)
y_relu =tf.nn.relu(x)
y_tanh = tf.nn.tanh(x)
y_softplus = tf.nn.softplus(x)

sess = tf.Session()
y_sigmoid, y_relu, y_tanh, y_softplus = sess.run([y_sigmoid, y_relu, y_tanh, y_softplus])

#创建各个激活函数的图形
plt.subplot(221)
plt.plot(x,y_sigmoid,c='red',label='sigmoid')
plt.ylim(-0.2,1.2)
plt.legend(loc="best")

plt.subplot(222)
plt.plot(x,y_relu,c='green',label='relu')
plt.ylim(-1,6)
plt.legend(loc="best")


sess.close()

