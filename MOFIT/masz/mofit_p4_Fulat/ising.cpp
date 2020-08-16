#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <ctime>

#define J 100.0
#define H 0.1

using namespace std;

double energia(int i, int j, int **S,int n){
	double energia=0.0;
	if(S[i][j]==S[(i+1)%n][j]) energia+=1;
	else energia-=1;
	if(S[i][j]==S[i][(j+1)%n]) energia+=1;
	else energia-=1;
	if(S[i][j]==S[(i-1+n)%n][j]) energia+=1;
	else energia-=1;
	if(S[i][j]==S[i][(j-1+n)%n]) energia+=1;
	else energia-=1;
	return -J*energia;
}

double etot(int **S,int n, double( *energia)(int,int,int **,int)){
	double suma_ij=0.0;
	double suma_i=0.0;
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			suma_ij+=0.5*energia(i,j,S,n);
		}
	}
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			suma_i+=H*S[i][j];
		}
	}
	return suma_ij-suma_i;
}

int main(){

srand(time(NULL));

fstream plik;
plik.open("ising.txt", ios::out);

double kT=0.01;
int nn=5;
int n=pow(2,nn);
double N=n*n;

//INICJALIZACJA TABLICY SPINOW
int **S=new int *[n];
for(int i=0; i<n; i++) S[i]=new int [n];

for(int i=0; i<n; i++){
	for(int j=0; j<n; j++){
		S[i][j]=1;
		//cout<<"S["<<i<<"]"<<"["<<j<<"]="<<S[i][j]<<endl;
	}
}

//OBLICZANIE ENERGII CAŁKOWITEJ UKŁADU
double Etot;
Etot=etot(S,n,energia);
cout<<"Etot="<<Etot/N<<endl;

//SCHEMAT METROPOLISA

double r;
double ns;
double dE;
double Epop;
int i_r,j_r;
double dkT=20.0;
double Esr,Ssr;
double iter=n*n*10000;
double suma_i;

Esr=Etot*10000;

for(kT=1e-5; kT<=1000; kT+=dkT){

	Etot=etot(S,n,energia);
	Epop=Esr;

	Esr=0.0;
	Ssr=0.0;
	for(int m=0; m<iter; m++){
		cout<<m<<endl;
		i_r=int(rand()%n);
		j_r=int(rand()%n);
		ns=S[i_r][j_r];
		dE=-2*energia(i_r,j_r,S,n)+2*H*ns;
		r=(double)rand()/RAND_MAX;
		if (r<exp(-dE/kT) || dE<=0.0 ){
			S[i_r][j_r]=-ns;
			Etot+=dE;
		}
		Esr+=Etot/N;
		suma_i=0.0;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				suma_i+=S[i][j];
			}
		}
		Ssr+=suma_i/N;
	}
	cout<<kT<<endl;
	plik<<kT<<" "<<Esr/iter<<" "<<Ssr/iter<<" "<<(Esr-Epop)/(iter*dkT)<<endl;
}


return 0;
}
