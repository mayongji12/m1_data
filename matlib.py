#__coding:utf-8__
#!/usr/bin/python
# File Name: matlib.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2015年10月23日 星期五 10时01分33秒
#########################################################################
import matplotlib as mpl
from PIL import Image
mpl.use('QT4Agg')
import matplotlib.pyplot as plt
#import ch
#ch.set_ch()
#X1 = range(0, 50)
#Y1 = [num**2 for num in X1] # y = x^2
#X2 = [0, 1]
#Y2 = [0, 1]  # y = x
lines = []
x = []
y = []
f = open('m1_af.txt','rb')
for line in f.readlines():
    lines.append(line.strip('\n'))
for dd in lines:
    x.append(dd.split(' ')[0])
    y.append(float(dd.split(' ')[1]))
x = x[::-1]
y = y[::-1]
Fig = plt.figure()                      # Create a `figure' instance
#Fig = plt.figure(figsize=(8,4))                      # Create a `figure' instance
#Ax = Fig.add_subplot(111)               # Create a `axes' instance in the figure
#Ax.plot(X1, Y1, X2, Y2)                 # Create a Line2D instance in the axes
#Fig.show()
#Fig.savefig("test.jpg")
#Ax.show()
#plt.plot(x,y)
#plt.title(u'流动资金总量(万亿)')
zhfont = mpl.font_manager.FontProperties(fname=r'/usr/share/fonts/truetype/arphic/ukai.ttc',size=14)
plt.bar(range(len(y)),y,align='center')
plt.xticks(range(len(y)),x,size='small')
plt.ylabel(u'流动资金总量（万亿）',fontproperties=zhfont)
plt.xlabel(u'时间',fontproperties=zhfont)
plt.show()
