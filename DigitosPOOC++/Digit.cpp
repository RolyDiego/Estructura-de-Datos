// Digit.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <conio.h>
#include "Digitos.h"
using namespace std;

int main(){
	int nro1, nro2,resul,op;
	cout << "Introducir un numero entero : ";
	cin >> nro1; 
	cout<<endl<<"*********************************";
	cout<<endl<<"Calculadora de Digitos";
	cout<<endl<<"1. Suma De Digitos";
	cout<<endl<<"2. Suma De Digitos Pares";
	cout<<endl<<"3. Suma De Digitos Impares";
	cout<<endl<<"4. Contador De Digitos";
	cout<<endl<<"5. Contador De Digitos Pares";
	cout<<endl<<"6. Contador De Digitos Impares";
	cout<<endl<<"7. Mayor Digito";
	cout<<endl<<"8. Menor Digito";
	cout<<endl<<"*********************************";
	cout<<endl<<"Que opcion eliges: ";
	cin>>op;
	Digitos obj(nro1);
	if(op == 1){
	resul = obj.sumarDigitos();
	cout <<endl<<"La suma es -->> : "<< resul;
	}
	if(op == 2){
	resul = obj.sumarDigitosPares();
	cout <<endl<<"La suma de los digitos pares es -->> : "<< resul;
	}
	if(op == 3){
	resul = obj.sumarDigitosImpares();
	cout <<endl<<"La suma de los digitos impares es -->> : "<< resul;
	}
	if(op == 4){
	resul = obj.contarDigitos();
	cout <<endl<<"La cantidad de digitos es -->> : "<< resul;
	}
	if(op == 5){
	resul = obj.contarDigitosPares();
	cout <<endl<<"La cantidad de digitos pares es -->> : "<< resul;
	}
	if(op == 6){
	resul = obj.contarDigitosImpares();
	cout <<endl<<"La cantidad de digitos impares es -->> : "<< resul;
	}
	if(op == 7){
	resul = obj.mayorDigito();
	cout <<endl<<"El digito mayor es -->> : "<< resul;
	}
	if(op == 8){
	resul = obj.menorDigito();
	cout <<endl<<"El digito menor es -->> : "<< resul;
	}

	getch();
	return 0;
}