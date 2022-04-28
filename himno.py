import os#Diego Martinez

print( "\nCrear un archivo")
print ("================")

NOMBRE_ARCHIVO = 'datos.txt'

archivo = open(NOMBRE_ARCHIVO, 'w') # abre el archivo datos.txt
archivo.write('''
Diego Martinez

La España Grandiosa   
Con hado benigno   
aquí planto el signo   
de la redención.
''')
archivo.write('''
Y surgió a su sombra   
un pueblo eminente   
de límpida frente   
de leal corazón. 
''')
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
