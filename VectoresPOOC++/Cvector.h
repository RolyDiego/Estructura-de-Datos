class Cvector{
	int vec[50];	
	int n;
public:
	Cvector(int a);
	~Cvector();

	void cargar();
	
	void mostrar();
	
	int sumarElementos();

	int mayorElemento();

	int menorElemento();

	int parElementos();
	
	int imparElementos();

	int sumaParElementos();

	int sumaImparElementos();

	void cargarInver();

};