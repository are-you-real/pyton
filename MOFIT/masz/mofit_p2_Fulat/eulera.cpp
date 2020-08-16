#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>

#define M 1.989e30
#define G 6.6741e-11
#define au 149597870700

using namespace std;

void schemat_Eulera(double x, double y, double vx, double vy, double dt, double T, fstream &plik, double tol){

	double t=0.0;
	double r;
	double xn,yn,vxn,vyn;
	double xn1,yn1,vxn1,vyn1;
	double xn2,yn2,vxn2,vyn2;
	double epsx,epsy;

	while(t<=T){

		r=sqrt(x*x+y*y);
		//rachunek z dt
		xn=x+vx*dt;
		yn=y+vy*dt;
		vxn=vx-G*M/(r*r*r)*x*dt;
		vyn=vy-G*M/(r*r*r)*y*dt;
		//rachunek z dt/2
		xn1=x+vx*dt/2;
		yn1=y+vy*dt/2;
		vxn1=vx-G*M/(r*r*r)*x*dt/2;
		vyn1=vy-G*M/(r*r*r)*y*dt/2;
		xn2=xn1+vxn1*dt/2;
		yn2=yn1+vyn1*dt/2;
		vxn2=vxn1-G*M/(r*r*r)*xn1*dt/2;
		vyn2=vyn1-G*M/(r*r*r)*yn1*dt/2;
		//szacowanie bledu
		epsx=xn2-xn;
		epsy=yn2-yn;
		if(abs(epsx)<=tol and abs(epsy)<=tol){
			x=xn2;
			y=yn2;
			vx=vxn2;
			vy=vyn2;
			plik<<t/(365*24*3600)<<" "<<x/au<<" "<<y/au<<" "<<sqrt(x/au*x/au+y/au*y/au)<<" "<<dt/(24*3600)<<endl;
			t+=dt;
			cout<<t/(365*24*3600)<<endl;
		}
		dt=0.9*dt*pow(tol/sqrt(epsx*epsx+epsy*epsy),0.5);
	}

}

int main(){

	double T=3*75.0*365*24*3600;
	double dt=3600.0;
	double x,y,vx,vy;
	double tol=1;

	fstream plik;
	plik.open("eulera_1.txt", ios::out);

	//warunki poczatkowe
	x=0.0;
	y=0.586*au;
	vx=54600.0;
	vy=0.0;

	plik<<0.0<<" "<<x/au<<" "<<y/au<<" "<<endl;
	schemat_Eulera(x,y,vx,vy,dt,T,plik, tol);

	plik.close();

	return 0;
}
