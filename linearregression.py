#code = UTF-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#用梯度下降的油画方法来解决线性回归问题

import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf 

points_num = 100
verctors = []
#用numpy的正态随机分布函数生成100个点
#这些点的(x,y)坐标值对应线性方程y=0.1*x + 0.2
for i in xrange(points_num):
    x1 = np.random.normal(0.0, 0.66)
    y1 = 0.1*x1 + 0.2 + np.random.normal(0.0,0.04)
    verctors.append([x1,y1])

x_data = [v[0] for v in verctors]
y_data = [v[1] for v in verctors]
plt.plot(x_data, y_data, 'r*', label="Original data")
plt.title('linear regression')
plt.legend()
plt.show()

#构建线性回归模型
W = tf.Variable(tf.random_uniform([1]), -1.0, 1.0) #初始化权重
b = tf.Variable(tf.zeros([1])) #初始化bias
y = W * x_data + b

#定义loss function， 对tensor的所有维度计算((y-y_data)^2)之和/N
loss = tf.reduce_mean(tf.square(y-y_data))
#用梯度下降的优化器来优化我们的loss function
optimizer = tf.train.GradientDescentOptimizer(0.5) #设置学习率0.5
train = optimizer.minimize(loss)

#创建会话
sess = tf.Session()

#初始化数据流图中的所有变量
init = tf.global_variables_initializer()
sess.run(init)

#训练20步
for step in xrange(20):
    #优化每一步
    sess.run(train)
    #打印出每一步的损失， 权重
    print("Step=%d, loss=%f, [Wegiht=%f Bias=%f]" %(step, sess.run(loss), sess.run(W),sess.run(b)))

#图像2： 回执所有的点并且绘制最佳拟合曲线
plt.plot(x_data, y_data, 'r*', label="Original data")
plt.title('linear regression')
plt.plot(x_data, ress.run(W)*x_data+sess.run(b), label='fitting line')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

sess.close()
