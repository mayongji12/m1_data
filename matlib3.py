#__coding:utf-8__
#!/usr/bin/python
# File Name: matlib3.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2015年10月23日 星期五 11时03分17秒
#########################################################################
import matplotlib.pyplot as pl
from matplotlib.ticker import *
import numpy as np
MultipleLocator.MAXTICKS = 370000.00
fig = pl.figure(figsize=(10,6))
x = [201210,201211,201212,201213,201214,201215,201216]
y = [293309.78,296883.0,308672.99,311228.55,296103.24,310898.29,307648.42]
pl.plot(x, y, label='YR', color='red')

ax = pl.gca()
pl.ylim(0,800)
pl.xlim(0, np.max(x))

pl.subplots_adjust(bottom = 0.15)

pl.grid()
ax.xaxis.set_major_locator( MultipleLocator(3) )
ax.yaxis.set_major_locator( MultipleLocator(50) )
locs,labels = pl.xticks()
pl.xticks(locs, t)
pl.ylabel("Number")
pl.title("WCG => Samba")
pl.legend()
fig.autofmt_xdate()
pl.savefig("wcg.png")
