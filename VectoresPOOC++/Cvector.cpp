#include "StdAfx.h"
#include "Cvector.h"
#include <iostream>
using namespace std;

Cvector::Cvector(int a){
	n = a;
}

Cvector::~Cvector(){
}

void Cvector::cargar(){
	for(int i=0; i<n; i++){
		cout<<"Introducir elemento vec{"<<i<<"]: ";
		cin >> vec[i];
	}
}


void Cvector::mostrar(){
	cout << endl << "El contenido del vector es -->"<<endl;
	for(int i=0; i<n; i++){
		cout<<vec[i]<<" ";
	}
}

int Cvector::sumarElementos(){
	int s = 0;
	for(int i=0; i<n; i++){
		s = s + vec[i];
	}
	return(s);
}

int Cvector::mayorElemento(){
	int mayor = vec[0];
	for(int i=1; i<n; i++){
		if(vec[i] > mayor){
			mayor = vec[i];
		}
	}
	return(mayor);
}

int Cvector::menorElemento(){
	int menor = vec[0];
	for(int i=1; i<n; i++){
		if(vec[i] < menor){
			menor = vec[i];
		}
	}
	return(menor);
}

int Cvector::parElementos(){
	int contaPar = 0;
	for(int i=0; i<n; i++){
		if(vec[i] %2 == 0){
			contaPar++;
		}
	}
	return(contaPar);
}

int Cvector::imparElementos(){
	int contaImpar = 0;
	for(int i=0; i<n; i++){
		if(vec[i] %2 != 0){
			contaImpar++;
		}
	}
	return(contaImpar);
}

int Cvector::sumaParElementos(){
	int sumaPar = 0;
	for(int i=0; i<n; i++){
		if(vec[i] %2 == 0){
			sumaPar =vec[i] + sumaPar;
		}
	}
	return(sumaPar);
}

int Cvector::sumaImparElementos(){
	int sumaImpar = 0;
	for(int i=0; i<n; i++){
		if(vec[i] %2 != 0){
			sumaImpar =vec[i] + sumaImpar;
		}
	}
	return(sumaImpar);
}

void Cvector::cargarInver(){
	int i, aux;
	for(i=0;i<n/2; i++){
       aux = vec[i];
       vec[i]=vec[n-1-i];
       vec[n-1-i]=aux;
    }
}