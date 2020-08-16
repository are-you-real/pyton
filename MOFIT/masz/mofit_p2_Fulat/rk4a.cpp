#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>

#define M 1.989e30
#define G 6.6741e-11
#define au 149597870700.0

using namespace std;

void pochodne(double t, double *u, double *f){

	f[0]=u[2];
	f[1]=u[3];
	double r=sqrt(u[0]*u[0]+u[1]*u[1]);
	f[2]=-G*M/(r*r*r)*u[0];
	f[3]=-G*M/(r*r*r)*u[1];

}

void rk4(double t, double dt, int n, double *u, void (*f)(double, double *, double *)){

	double k1[n];
	double k2[n];
	double k3[n];
	double k4[n];
	double w[n];

	for(int i=0; i<n; i++) w[i]=u[i];
	f(t,w,k1);

	for(int i=0; i<n; i++) w[i]=u[i]+dt/2*k1[i];
	f(t+dt/2,w,k2);

	for(int i=0; i<n; i++) w[i]=u[i]+dt/2*k2[i];
	f(t+dt/2,w,k3);

	for(int i=0; i<n; i++) w[i]=u[i]+dt*k3[i];
	f(t+dt,w,k4);

	for(int i=0;i<n;i++) u[i]=u[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]);

}


int main(int argc, char* argv[]){

	double dt=10*24*3600.0;
	double T=3*75.0*365*24*3600;
	double t=0.0;
	double tol=1000;

	int n=4;
	int N=int(T/dt);

	double u[n], un1[n], un2[n];

	fstream plik;
	plik.open("rk4a_1000.txt", ios::out);

	//warunki poczatkowe
	u[0]=0.0;
	u[1]=0.586*au;
	u[2]=54600.0;
	u[3]=0.0;

	un1[0]=0.0;
	un1[1]=0.586*au;
	un1[2]=54600.0;
	un1[3]=0.0;

	un2[0]=0.0;
	un2[1]=0.586*au;
	un2[2]=54600.0;
	un2[3]=0.0;

	double epsx,epsy,eps;

	while(t<T){
		for(int m=0; m<=n; m++) un1[m]=u[m];
		rk4(t,dt,n,u,pochodne);
		rk4(t,dt/2,n,un1,pochodne);
		rk4(t,dt/2,n,un1,pochodne);
		epsx=(un1[0]-u[0])/15.0;
		epsy=(un1[1]-u[1])/15.0;
		if(epsx>epsy) eps=epsx;
		else eps=epsy;
		if(eps==0.0) eps+=1e-10;
		eps=abs(eps);
		if(eps<=tol){
			for(int m=0; m<=n; m++) u[m]=un1[m];
			plik<<t/(365*24*3600)<<" "<<sqrt(u[0]/au*u[0]/au+u[1]/au*u[1]/au)<<" "<<dt/(24*3600.0)<<" "<<u[0]/au<<" "<<u[1]/au<<endl;
			t+=dt;
			cout<<t/(365*24*3600)<<endl;
		}
		dt=0.9*dt*pow(tol/eps,1.0/5.0);
	}

	plik.close();

	return 0;
}
