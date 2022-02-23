// ProgCalcu.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <iostream>
#include <conio.h>
#include "Calculadora.h"
using namespace std;

int main(){
	int nro1, nro2,resul;
	cout << "Introducir un numero entero : ";
	cin >> nro1;
	cout << "\nIntroducir otro numero entero : ";
	cin >> nro2;

	Calculadora obj(nro1,nro2);
	resul = obj.sumar();
	cout <<endl<<"La suma es -->> : "<< resul;
	resul = obj.restar();
	cout<<endl<<"La resta es -->> : "<< resul;
	resul = obj.multiplicar();
	cout<<endl<<"La multiplicacion es -->> : "<< resul;
	if(nro2 == 0){
		cout<<"\nLa division entre cero no es posible";
	}else{
		resul = obj.division();
		cout<<endl<<"La division es -->> : "<< resul;
	}
	getch();
	return 0;
}
