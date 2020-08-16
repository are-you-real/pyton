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

	int n=4;
	int N=int(T/dt);

	double u[n];

	fstream plik;
	plik.open("rk4_10d.txt", ios::out);

	//warunki poczatkowe
	u[0]=0.0;
	u[1]=0.586*au;
	u[2]=54600.0;
	u[3]=0.0;

	//symulacja w czasie
	for(int i=1;i<=N;i++){
		rk4(t,dt,n,u,pochodne);
		t+=dt;
		plik<<t/(365*24*3600)<<" "<<u[0]/au<<" "<<u[1]/au<<" "<<u[2]<<" "<<u[3]<<endl;
	}

	plik.close();

	return 0;
}
