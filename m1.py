#__coding:utf-8__
#!/usr/bin/python
# File Name: m1.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2015年10月20日 星期二 17时38分40秒
#########################################################################
import json
f = open('m1.txt','rb')
lines = f.readlines()
f.close()
line = lines[0]   #line  is  string
line2json=json.loads(line) #dict line2json has 2 item returndata and returncode
jsondata=line2json['returndata'] #dict jsondata has 2 item datanodes and wdnodes
data1 = jsondata['datanodes']
m_date = []
m_data = []
f = open('m1_af.txt','wb+')
for i in data1:        # dict i        
    flag = list(i['code'].split('.'))
    if flag[1]=='A0B0103_sj':
        date = flag[2]
        value = float(i['data']['strdata'])
        f.write('%s %s\n' %(date,value))
        m_date.append(date)
        m_data.append(value)
f.close()
m_date = m_date[::-1]
m_data = m_data[::-1]
m1 = zip(m_date,m_data)
print m1
                


