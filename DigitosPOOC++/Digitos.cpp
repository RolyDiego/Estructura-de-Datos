#include "StdAfx.h"
#include "Digitos.h"


Digitos::Digitos(int x){
	a = x;
}

Digitos::~Digitos(){
	
}

int Digitos::sumarDigitos(){
	int sum = 0, digito;
	while(a > 0){
		digito = a % 10;
        a = a / 10;
        sum=sum+digito;
     }
	return(sum);
}

int Digitos::sumarDigitosPares(){
	int sum = 0, digito;
	while(a > 0){
		digito = a % 10;
        a = a / 10;
		if(digito % 2 ==0){
             sum=sum+digito;
        }
     }
	return(sum);
}

int Digitos::sumarDigitosImpares(){
	int sum = 0, digito;
	while(a > 0){
		digito = a % 10;
        a = a / 10;
		if(digito % 2 !=0){
             sum=sum+digito;
        }
     }
	return(sum);
}
int Digitos::contarDigitos(){
	int digito, conta=0;
	while(a > 0){
		digito = a % 10;
        a = a / 10;
        conta=conta+1;
     }
	return(conta);
}

int Digitos::contarDigitosPares(){
	int digito, conta=0;
	while(a > 0){
		digito = a % 10;
        a = a / 10;
		if(digito % 2 ==0){
			conta=conta+1;
		}
     }
	return(conta);
}

int Digitos::contarDigitosImpares(){
	int digito, conta=0;
	while(a > 0){
		digito = a % 10;
        a = a / 10;
		if(digito % 2 != 0){
			conta=conta+1;
		}
     }
	return(conta);
}

int Digitos::mayorDigito(){
	int digito, mayor = 0;
	while(a > 1){
		digito =  a % 10; 
		if(digito>mayor){
			mayor = digito;
		}
		a = a / 10;
	}
	return(mayor);
}

int Digitos::menorDigito(){
	int digito = 0, menor = digito;
	while(a > 1){
		digito =  a % 10; 
		if(digito<menor){
			menor = digito;
		}
		a = a / 10;
	}
	return(menor);
}