#APROFEX
# Diego Martinez Garzon - 29/05/2022
import os
import pickle

class Curso:
    def __init__(self, idDoc, nomb):
        self.idCurso = idDoc
        self.nombre = nomb

    def obtIdCurso(self):
        return (self.idCurso)

    def obtNombre(self):
        return (self.nombre)

    def __str__(self):
        return '{:7} {:30} '.format(self.idCurso, self.nombre)


class ArchivoCurso:
    Cursos = []  # lista donde se gestionaran los datos de los Cursos

    def __init__(self,):
        self.NomArchivo = 'pfxCurso.pkl'
        self.cargaArchivoEnLista()

    def cargaArchivoEnLista(self):
        fichero = open(self.NomArchivo, 'ab+')
        fichero.seek(0)
        try:
            self.Cursos = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            #print("Se han cargado {} Cursos..".format(len(self.Cursos)))

    def adiconar(self, doc):  # recibo un objeto de la clase alumno con los datos ya cargados
        self.Cursos.append(doc)  # adiciona en la lista
        self.almacenarEnArchivo()  # lo escribe en el archivo binario

    def almacenarEnArchivo(self):
        # crea de nuevo contenido de archivo
        fichero = open(self.NomArchivo, 'wb')
        pickle.dump(self.Cursos, fichero)
        fichero.close()

    def buscarMostrarUnCurso(self, cod):
        if len(self.Cursos) == 0:
            print("No hay Cursos...")
            return
        k = False
        for doc in self.Cursos:
            if(doc.obtIdCurso() == cod):
                print(doc)
                k = True
                break

        if(k == False):
            print("\nCodigo de Curso ", cod, " no existe !!!")
        return k

    def eliminarUnCurso(self, cod):
        if len(self.Cursos) == 0:
            print("No hay Cursos...")
            return
        k = False
        listAux = []
        for doc in self.Cursos:
            if(doc.obtIdCurso() == cod):
                k = True
            else:
                listAux.append(doc)

        if(k == True):
            self.Cursos = listAux
            self.almacenarEnArchivo()
            print("\nCurso ", cod, " eliminado exinosamente ...")
        else:
            print("\nCodigo de Curso ", cod, " no existe !!!")

    def modificarUnCurso(self, docModi):
        if len(self.Cursos) == 0:
            print("No hay Cursos...")
            return
        cod = docModi.obtIdCurso()
        k = False
        listAux = []
        for doc in self.Cursos:
            if(doc.obtIdCurso() == cod):
                k = True
                listAux.append(docModi)
            else:
                listAux.append(doc)

        if(k == True):
            self.Cursos = listAux
            self.almacenarEnArchivo()
            print("\nCurso ", cod, " Modificado exinosamente ...")
        else:
            print("\nCodigo de Curso ", cod, " no existe !!!")

    def listarTodosCursos(self):
        if len(self.Cursos) == 0:
            print("No hay Cursos...")
            return
        print("------------------------------------------------------------------------------------")
        print("           <<< ***   LISTA DE CuSOS    ****>>>")
        print("------------------------------------------------------------------------------------")
        print(" Codigo        Nombre Curso")
        print("------------------------------------------------------------------------------------")
        for doc in self.Cursos:
            # print(alum)
            print('{0:7}     {1:30}'.format( doc.obtIdCurso(), doc.obtNombre()))
        print("------------------------------------------------------------------------------------")

    # verifica si ya existe un registro con el mismo id, retorna TRUE si existe
    def verSiExisteCurso(self, cod):
        existe = False
        if len(self.Cursos) == 0:
            return(existe)

        for doc in self.Cursos:
            if(doc.obtIdCurso() == cod):
                existe = True
                break
        return (existe)

    def obtNombreCurso(self, cod):#retorna el nombre de Curso desde archivo lista
        nombreDoc = ""
        for doc in self.Cursos:
            if(doc.obtIdCurso() == cod):
                existe = True
                nombreDoc = doc.obtNombre()
                break
        return (nombreDoc)

# --Main de Cursos()
def menuCurso():
    aa = ArchivoCurso()
    while True:
        os.system('color 1f')
        print("\n\t-----------------------------------------------")
        print("\t\t<< ** MENU DE CURSOS ** >>")
        print("\t-----------------------------------------------")
        print("\t1. Adicionar nuevo Curso")
        print("\t2. Buscar por codigo y mostrar un determinado Curso")
        print("\t3. Modificar/Editar datos de un Curso")
        print("\t4. Eliminar un Curso")
        print("\t5. Listar todos los Cursos")
        print("\t0. Salir")
        print("\t-----------------------------------------------")
        opc = int(input("\tSelecciona una opcion : "))
        os.system('cls')
        if opc == 1:
            while True:  # valida para no intorducir codigos duplicados
                cod = int(input("Codigo : "))
                if(aa.verSiExisteCurso(cod) == True):
                    print("\nCodigo ya existe..!!!, intente con otro codigo..")
                else:
                    break

            nombre = input("Nombre del curso : ")
            aa.adiconar(Curso(cod, nombre))
        elif opc == 2:
            cod = int(input("Codigo  de Curso a buscar : "))
            aa.buscarMostrarUnCurso(cod)
        elif opc == 3:
            cod = int(input("Codigo  del Curso a modificar sus datos? : "))
            if(aa.buscarMostrarUnCurso(cod) == True):
                nombre = input("Nuevo Nombre del Curso: ")
                aa.modificarUnCurso(Curso(cod, nombre))
        elif opc == 4:
            cod = int(input("Codigo  de Curso a eliminar : "))
            aa.eliminarUnCurso(cod)
        elif opc == 5:
            aa.listarTodosCursos()
        elif opc == 0:
            os.system('color 0f')
            break
        else:
            os.system('color 4f')
            print('Se introdujo un valor fuera de las opciones')

        os.system('pause')
