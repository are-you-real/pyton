import random

f=open("dada.txt",'w')

x0=1.0
y0=1.0
No=0.0
Nk=0.0
Sk=4.0
for i in range(1000000):
	x=random.random()
	y=random.random()	
	if (x**2+y**2)<=1:
		No+=1
		Nk+=1
	else: 
		Nk+=1
	pii=No*Sk/Nk	
	if i<100:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", liczony/prawdziwy wynik=" + str(pii/3.1415) + '\n')
	elif i==999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", liczony/prawdziwy wynik=" + str(pii/3.1415)+ '\n')
	elif i==9999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + "liczony/prawdziwy wynik=" + str(pii/3.1415)+ '\n')
	elif i==99999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + "liczony/prawdziwy wynik=" + str(pii/3.1415) + '\n')
 	elif i==999999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + "liczony/prawdziwy wynik=" + str(pii/3.1415) + '\n')
	elif i==9999999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", prawdziwy wynik pi =3.1415" + '\n')

f.close()	
