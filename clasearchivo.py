import os

print( "\nCrear un archivo")
print ("================")

NOMBRE_ARCHIVO = 'datos.txt'

archivo = open(NOMBRE_ARCHIVO, 'w') # abre el archivo datos.txt
archivo.write("\nDiego Martinez  09/04/2003   3428042")
archivo.write("\n==========================================")
archivo.write("\nJorge Saucedo   12/12/2002   2381038")
archivo.write("\n==========================================")
archivo.write("\nSebastian Mendoza  14/11/2002  8934280")
archivo.write("\n==========================================")
archivo.write("\nAdrian Telchy 10/09/2002  6457297")
archivo.write("\n==========================================")
archivo.write("\nJhair Do Ceu 10/10/2002  98389878")
archivo.close()

if NOMBRE_ARCHIVO in os.listdir("."):
    print (("\nArchivo creado en la ruta: \n\n\t{0}/{1}").format(os.getcwd(), NOMBRE_ARCHIVO))
else:
    print ("El archivo no fue creado!!!\n")
    

print ("\n\nLeer un archivo")
print ("===============\n")

archivo = open(NOMBRE_ARCHIVO, 'r')
contenido = archivo.read()
print (contenido)
archivo.close()

print ("\n\nIterar sobre un archivo")
print ("=======================\n")

archivo = open(NOMBRE_ARCHIVO, 'r')
for linea in archivo:
    print (linea)
print ("\n")
archivo.close()
