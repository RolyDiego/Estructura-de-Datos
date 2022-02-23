#include "StdAfx.h"
#include "Calculadora.h"


Calculadora::Calculadora(int x, int y){
	a = x;
	b = y;
}

Calculadora::~Calculadora(){
	
}

int Calculadora::sumar(){
	int r;
	r = a + b;
	return(r);
}

int Calculadora::restar(){
	int r;
	r = a - b;
	return(r);
}

int Calculadora::multiplicar(){
	int r;
	r = a * b;
	return(r);
}

int Calculadora::division(){
	int r;
	if(b == 0){
		r = 0;
	}else{
		r = a / b;
	}
	return(r);
}