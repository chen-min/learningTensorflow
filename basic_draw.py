#code = UTF-8
#映入pyplot模块
import  matplotlib.pyplot as plt 
import numpy as np  

x = np.linspace(-2,2,100)
y1 = 3 * x + 4
y2 = x ** 2
# 创建图像
# plt.plot(x,y1)
# plt.plot(x,y2)
plt.figure(num=1, figsize=(7,6))
plt.plot(x,y1)
plt.plot(x,y2, color="red", linewidth=3.0, linestyle="--")
plt.figure(num=2)
plt.plot(x,y2, color="green", linewidth=3.0, linestyle="--")

# 显示图像
plt.show()

