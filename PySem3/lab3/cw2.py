import random as r
import time as t
print ' '*98, 'START'
i=0
stop=10
s1=100-stop
ile=0
while abs(i)<=stop: 
	print ' '*(s1), '|',
	print ' '*(stop+i), '*',
	print ' '*(stop-i), '|', i
	t.sleep(0.05)
	war=r.uniform(-1,1)
	ile=ile+1
	if war>0:
		i=i+1
	elif war<0:
		i=i-1
print"wykonano", ile, "rzutow",

