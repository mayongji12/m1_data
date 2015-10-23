#__coding:utf-8__
#!/usr/bin/python
# File Name: matlib2.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2015年10月23日 星期五 10时13分54秒
#########################################################################
import numpy as np
import matplotlib.pyplot as plt
 
xData = np.arange(0,10,1)
yData1 = xData.__pow__(2.0)
yData2 = np.arange(15,61,5)
plt.figure(num=1, figsize=(8,6))
plt.title('Plot 1', size=14)
plt.xlabel('x-axis', size=14)
plt.ylabel('y-axis', size=14)
plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
plt.legend(loc='upper left')
plt.savefig('images/plot1.png', format='png')
