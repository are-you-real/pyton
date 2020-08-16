f=open("dada2.txt",'w')
pii=4.0
print (-1)**2, (-1)**3
f.write(str(1) + ') wynik "Pi"=' + str(pii) + ", prawdziwy wynik pi =3.1415" + '\n')
for i in range(3,10,2):
	print (-1)**i
	pii=pii+(1.0/i)*((-1)**(i))
	
	if i<100:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", prawdziwy wynik pi =3.1415" + '\n')
	elif i==999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", prawdziwy wynik pi =3.1415" + '\n')
	elif i==9999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", prawdziwy wynik pi =3.1415" + '\n')
	elif i==99999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", prawdziwy wynik pi =3.1415" + '\n')
 	elif i==999999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", prawdziwy wynik pi =3.1415" + '\n')
	elif i==9999999:
		f.write(str(i+1)+') wynik "Pi"=' + str(pii) + ", prawdziwy wynik pi =3.1415" + '\n')


f.close()	
	
