#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>

#define M 1.989e30
#define G 6.6741e-11
#define au 149597870700

using namespace std;

void schemat_Eulera(double x, double y, double vx, double vy, double dt, double T, fstream &plik){
	
	double t=0.0;
	double r;
	double xn,yn,vxn,vyn;
	
	while(t<=T){
		
		r=sqrt(x*x+y*y);		
		xn=x+vx*dt;
		yn=y+vy*dt;
		vxn=vx-G*M/(r*r*r)*x*dt;
		vyn=vy-G*M/(r*r*r)*y*dt;
		x=xn;
		y=yn;
		vx=vxn;
		vy=vyn;		
		plik<<t/(365*24*3600)<<" "<<x/au<<" "<<y/au<<" "<<endl;
		t+=dt;
		cout<<t/(365*24*3600)<<endl;	
		
	}

}

int main(){

	double T=3*75.0*365*24*3600;
	double dt=3600.0/4.0;
	double x,y,vx,vy;
	
	fstream plik;
	plik.open("euler_15.txt", ios::out);
	
	//warunki poczatkowe
	x=0.0;
	y=0.586*au;
	vx=54600.0;
	vy=0.0;

	plik<<0.0<<" "<<x/au<<" "<<y/au<<" "<<endl;	
	schemat_Eulera(x,y,vx,vy,dt,T,plik);

	plik.close();

	return 0;
}
