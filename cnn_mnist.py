#code = UTF-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('mnist_data',one_hot=True)
#one_hot 独热码的编码形式
#0,1,2,3,4,5,6,7,8,9 
#0: 1000000000
#1: 0100000000
#2: 0010000000
#3: 0001000000
#4: 0000100000
#5: 0000010000

#None表示张量(tensor)的第一个维度可以是任意长度
train_x = tf.placeholder(tf.float32, [None, 28 * 28]) / 255.
train_y = tf.placeholder(tf.int32, [None,10])
images = tf.reshape(tf.reshape(train_x,[-1,28,28,1]))

#构建卷积神经网络
