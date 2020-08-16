import math 
pi=3.1415
fi=[]
A=15
y=[]
	
for i in range(50):
		
	fi.append(i*2*pi/50)
	y=(A*math.sin(fi[i]))
	x=int(y)
	print i
	if x>0:	
		print ' '*100,
		print '+'*x
	elif x==0:	
		print ' '*100,		
		print 0
	elif x<0:
		x=-x
		print ' '*(100-x),
		print '-'*x
	

