#APROFEX
# Diego Martinez Garzon - 29/05/2022
from operator import truediv
import os
import pickle
import pfxBoxTools
import pfxOfertaCurso
import pfxClasesProgramada

class Docente:
    def __init__(self, idDoc, nomb, mail, celu,passw):
        self.idDocente = idDoc
        self.nombre = nomb
        self.email = mail
        self.celular = celu
        self.password = passw

    def obtIdDocente(self):
        return (self.idDocente)

    def obtNombre(self):
        return (self.nombre)

    def obtEmail(self):
        return (self.email)

    def obtCelular(self):
        return (self.celular)

    def obtPassword(self):
        return (self.password)

    def __str__(self):
        return '{:7} {:30} {:40} {:10}'.format(self.idDocente, self.nombre, self.email, self.celular)


class ArchivoDocente:
    docentes = []  # lista donde se gestionaran los datos de los docentes

    def __init__(self,):
        self.NomArchivo = 'pfxDocente.pkl'
        self.cargaArchivoEnLista()

    def cargaArchivoEnLista(self):
        fichero = open(self.NomArchivo, 'ab+')
        fichero.seek(0)
        try:
            self.docentes = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            #print("Se han cargado {} docentes..".format(len(self.docentes)))

    def adiconar(self, doc):  # recibo un objeto de la clase alumno con los datos ya cargados
        self.docentes.append(doc)  # adiciona en la lista
        self.almacenarEnArchivo()  # lo escribe en el archivo binario

    def almacenarEnArchivo(self):
        # crea de nuevo contenido de archivo
        fichero = open(self.NomArchivo, 'wb')
        pickle.dump(self.docentes, fichero)
        fichero.close()

    def buscarMostrarUnDocente(self, cod):
        if len(self.docentes) == 0:
            print("No hay docentes...")
            return
        k = False
        for doc in self.docentes:
            if(doc.obtIdDocente() == cod):
                print(doc)
                k = True
                break

        if(k == False):
            print("\nCodigo de docente ", cod, " no existe !!!")
        return k

    def eliminarUnDocente(self, cod):
        if len(self.docentes) == 0:
            print("No hay docentes...")
            return
        k = False
        listAux = []
        for doc in self.docentes:
            if(doc.obtIdDocente() == cod):
                k = True
            else:
                listAux.append(doc)

        if(k == True):
            self.docentes = listAux
            self.almacenarEnArchivo()
            print("\nDocente ", cod, " eliminado exitosamente ...")
        else:
            print("\nCodigo de docente ", cod, " no existe !!!")

    def modificarUnDocente(self, docModi):
        if len(self.docentes) == 0:
            print("No hay docentes...")
            return
        cod = docModi.obtIdDocente()
        k = False
        listAux = []
        for doc in self.docentes:
            if(doc.obtIdDocente() == cod):
                k = True
                listAux.append(docModi)
            else:
                listAux.append(doc)

        if(k == True):
            self.docentes = listAux
            self.almacenarEnArchivo()
            print("\nDocente ", cod, " Modificado exinosamente ...")
        else:
            print("\nCodigo de docente ", cod, " no existe !!!")

    def listarTodosDocentes(self):
        if len(self.docentes) == 0:
            print("No hay docentes...")
            return
        print("------------------------------------------------------------------------------------")
        print("                   <<< ***   LISTA DE DOCENTES    ****>>>")
        print("------------------------------------------------------------------------------------")
        print(" Codigo        Nombre  y Apellido             E-mail                    Celular")
        print("------------------------------------------------------------------------------------")
        for doc in self.docentes:
            # print(alum)
            print('{0:7}     {1:30} {2:30} {3:10}'.format(
                doc.obtIdDocente(), doc.obtNombre(), doc.obtEmail(), doc.obtCelular()))
        print("------------------------------------------------------------------------------------")

    # verifica si ya existe un registro con el mismo id, retorna TRUE si existe
    def verSiExisteDocente(self, cod):
        existe = False
        if len(self.docentes) == 0:
            return(existe)

        for doc in self.docentes:
            if(doc.obtIdDocente() == cod):
                existe = True
                break
        return (existe)

    def obtNombreDocente(self, cod):#retorna el nombre de docente desde archivo lista
        nombreDoc = ""
        for doc in self.docentes:
            if(doc.obtIdDocente() == cod):
                existe = True
                nombreDoc = doc.obtNombre()
                break
        return (nombreDoc)

    def validaUsrDocente(self, mail,pwd):
        existe = False
        cod = 0
        if len(self.docentes) == 0:
            return(existe)

        for doc in self.docentes:
            if(doc.obtEmail() == mail):
                if(doc.obtPassword() == pwd):
                    cod = doc.obtIdDocente()
                    existe = True
                    break
        return (cod)


# --Main de Docentes()
def menuDocente():
    aa = ArchivoDocente()
    while True:
        os.system('color 1f')
        print("\n\t-----------------------------------------------")
        print("\t\t<< ** MENU DE DOCENTES ** >>")
        print("\t-----------------------------------------------")
        print("\t1. Adicionar nuevo Docente")
        print("\t2. Buscar por codigo y mostrar un determinado docente")
        print("\t3. Modificar/Editar datos de un Docente")
        print("\t4. Eliminar un Docente")
        print("\t5. Listar todos los Docentes")
        print("\t0. Salir")
        print("\t-----------------------------------------------")
        opc = int(input("\tSelecciona una opcion : "))
        os.system('cls')
        if opc == 1:
            while True:  # valida para no intorducir codigos duplicados
                cod = int(input("Codigo : "))
                if(aa.verSiExisteDocente(cod) == True):
                    print("\nCodigo ya existe..!!!, intente con otro codigo..")
                else:
                    break

            nombre  = input("Nombre y apellido : ")
            celu    = input("Nro de Celular : ")
            mail    = input("e-Mail : ")
            pwd     = pfxBoxTools.getpass("Password : ")
            aa.adiconar(Docente(cod, nombre, mail, celu,pwd))
        elif opc == 2:
            cod = int(input("Codigo  de Docente a buscar : "))
            aa.buscarMostrarUnDocente(cod)
        elif opc == 3:
            cod = int(input("Codigo  del Docente a modificar sus datos? : "))
            if(aa.buscarMostrarUnDocente(cod) == True):
                nombre  = input("Nuevo Nombre y apellido: ")
                celu    = input("Nueva Nro de Celular : ")
                mail    = input("Nuevo e-Mail : ")
                pwd     = pfxBoxTools.getpass("Nuevo Password : ")
                aa.modificarUnDocente(Docente(cod, nombre, mail, celu,pwd))
        elif opc == 4:
            cod = int(input("Codigo  de Docente a eliminar : "))
            aa.eliminarUnDocente(cod)
        elif opc == 5:
            aa.listarTodosDocentes()
        elif opc == 0:
            os.system('color 0f')
            break
        else:
            os.system('color 4f')
            print('Se introdujo un valor fuera de las opciones')

        os.system('pause')


def menuUsuarioDocente(cod):
    aa = ArchivoDocente()
    objOferta = pfxOfertaCurso.ArchivoOferta()
    objClases = pfxClasesProgramada.ArchivoClase()
    print("\n------------------------------ B I E N V E N I D O ------------------------------------------")
    aa.buscarMostrarUnDocente(cod)
    print("---------------------------------------------------------------------------------------------")
    while True:
        os.system('color 1f')
        print("\n\t-----------------------------------------------")
        print("\t\t<< ** MENU DE USUARIOS DOCENTES ** >>")
        print("\t-----------------------------------------------")
        print("\t1. Mi Perfil")
        print("\t2. Editar mi peril")
        print("\t3. Ver ofertas de cursos")
        print("\t4. Ver mis clases programadas")
        print("\t0. Salir")
        print("\t-----------------------------------------------")
        opc = int(input("\tSelecciona una opcion : "))
        os.system('cls')
        if opc == 1:
            aa.buscarMostrarUnDocente(cod)
        elif opc == 2:
            #cod = int(input("Codigo  del Docente a modificar sus datos? : "))
            if(aa.buscarMostrarUnDocente(cod) == True):
                nombre  = input("Nuevo Nombre y apellido: ")
                celu    = input("Nueva Nro de Celular : ")
                mail    = input("Nuevo e-Mail : ")
                pwd     = pfxBoxTools.getpass("Nuevo Password : ")
                aa.modificarUnDocente(Docente(cod, nombre, mail, celu,pwd))
        elif opc == 3:
            objOferta.listarTodosOfertas()
        elif opc == 4:
            objClases.listarTodosClases(-1)
        elif opc == 0:
            os.system('color 0f')
            break
        else:
            os.system('color 4f')
            print('Se introdujo un valor fuera de las opciones')

        os.system('pause')