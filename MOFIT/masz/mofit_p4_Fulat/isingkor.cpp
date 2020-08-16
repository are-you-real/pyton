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

double ijsr_f(int **S, int d, int n){
	return S[n/2-d][n/2-d]*S[n/2][n/2];
}
double jsr_f(int **S, int d, int n){
	return S[n/2-d][n/2-d];
}

int main(){

srand(time(NULL));

fstream plik;
plik.open("isingkor.txt", ios::out);

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
double Esr,Ssr,isr;
double iter=n*n*10000;
double suma_i;
double ijsr[5]={0,0,0,0,0};
double jsr[5]={0,0,0,0,0};
double korelacja[5]={0,0,0,0,0};
double d[5]={1,2,3,4,9};

Esr=Etot*10000;

for(kT=1e-5; kT<=1000; kT+=dkT){

	Etot=etot(S,n,energia);
	Epop=Esr;

	Esr=0.0;
	Ssr=0.0;
	isr=0.0;
	for(int i=0;i<5;i++){
		ijsr[i]=0.0;
		jsr[i]=0.0;
		korelacja[i]=0.0;
	}
	for(int m=0; m<iter; m++){
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
		isr+=S[n/2][n/2];
		for(int i=0;i<5;i++) ijsr[i]+=ijsr_f(S,d[i],n);
		for(int i=0;i<5;i++) jsr[i]+=jsr_f(S,d[i],n);
	}

	cout<<kT<<endl;
	for(int i=0;i<5;i++) korelacja[i]=ijsr[i]/iter-jsr[i]/iter*isr/iter;
	plik<<kT<<" "<<korelacja[0]<<" "<<korelacja[2]
	<<" "<<korelacja[3]<<" "<<korelacja[4]
	<<" "<<korelacja[5]<<" "<<(Esr-Epop)/(iter*dkT)<<endl;
}


return 0;
}
