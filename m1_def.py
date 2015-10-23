#__coding:utf-8__
#!/usr/bin/python
# File Name: m1_def.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2015年10月20日 星期二 18时08分30秒
#########################################################################
import json,os
def gethtml(url,cookie,dfile):
    os.system('curl %s -b %s > %s' % (url,cookie,dfile))
    f = open(dfile,'rb')
    lines = f.readlines()
    f.close()
    json.loads(lines[0])['returndata']['datanodes']
    m1 = []
    for i in data:
        if list(i['code'].split('.'))[1]=='A0B0103_sj':
            m1.append(float(i['data']['strdata']))
return m1

