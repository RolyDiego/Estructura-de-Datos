// progVector.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <conio.h>
#include <iostream>
#include "Cvector.h"

using namespace std;

int main(){
	int numElem;
	cout << "Numero de elmentos para el vector ? : ";
	cin >>numElem;
	Cvector v(numElem);
	v.cargar();
	v.mostrar();
	cout << "\n\nLa suma de todos los elementos es ---->>> : "<< v.sumarElementos();
	cout << "\nEl mayor elemento del vector es ---->>> : "<<v.mayorElemento();
	cout << "\nEl menor elemento del vector es ---->>> : "<<v.menorElemento();
	cout << "\nLa cantidad de elementos pares es ---->>> : "<<v.parElementos();
	cout << "\nLa cantidad de elementos impares es ---->>> : "<<v.imparElementos();
	cout << "\nLa suma de los elementos pares es ---->>> : "<<v.sumaParElementos();
	cout << "\nLa suma de los elementos impares es ---->>> : "<<v.sumaImparElementos();
	cout << "\nSi aplicamos inversa: ";
	v.cargarInver();
	v.mostrar();
	getch();
	return 0;
}