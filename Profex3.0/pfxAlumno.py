#APROFEX
# Diego Martinez Garzon - 29/05/2022
import os
import pickle
import pfxBoxTools
import pfxOfertaCurso
import pfxClasesProgramada

class Alumno:
    def __init__(self, idAlum,nomb,mail,celu,passw):
        self.idAlumno      = idAlum 
        self.nombre         = nomb
        self.email          = mail
        self.celular        = celu
        self.password       = passw

    def obtIdAlumno(self):
        return (self.idAlumno)

    def obtNombre(self):
        return (self.nombre)

    def obtEmail(self):
        return (self.email)

    def obtCelular(self):
        return (self.celular)

    def obtPassword(self):
        return (self.password)

    def __str__(self):
        return '{:7} {:30} {:40} {:10}'.format(self.idAlumno,self.nombre,self.email,self.celular)
       

class ArchivoAlumno:
    Alumnos = []  #lista donde se gestionaran los datos de los Alumnos

    def __init__(self,):
        self.NomArchivo  = 'pfxAlumno.pkl'
        self.cargaArchivoEnLista()

    def cargaArchivoEnLista(self):
        fichero = open(self.NomArchivo, 'ab+')
        fichero.seek(0)
        try:
            self.Alumnos = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            #print("Se han cargado {} Alumnos..".format(len(self.Alumnos)))

    def adiconar(self,doc): # recibo un objeto de la clase alumno con los datos ya cargados
        self.Alumnos.append(doc) #adiciona en la lista
        self.almacenarEnArchivo() #lo escribe en el archivo binario

    def almacenarEnArchivo(self):
        fichero = open(self.NomArchivo, 'wb') # crea de nuevo contenido de archivo
        pickle.dump(self.Alumnos, fichero)
        fichero.close()

    def buscarMostrarUnAlumno(self,cod):
        if len(self.Alumnos) == 0:
            print("No hay Alumnos...")
            return
        k = False
        for doc in self.Alumnos:
            if(doc.obtIdAlumno() == cod):
                print(doc)
                k = True
                break

        if(k == False): print("\nCodigo de Alumno ",cod," no existe !!!")
        return k


    def eliminarUnAlumno(self,cod):
        if len(self.Alumnos) == 0:
            print("No hay Alumnos...")
            return
        k = False
        listAux = []
        for doc in self.Alumnos:                
                if(doc.obtIdAlumno()== cod):
                    k = True
                else:
                    listAux.append(doc)
       
        if(k == True):
            self.Alumnos = listAux
            self.almacenarEnArchivo()
            print("\nAlumno ",cod," eliminado exinosamente ...")
        else:
            print("\nCodigo de Alumno ",cod," no existe !!!")

    def modificarUnAlumno(self,docModi):
        if len(self.Alumnos) == 0:
            print("No hay Alumnos...")
            return
        cod = docModi.obtIdAlumno()       
        k = False
        listAux = []
        for doc in self.Alumnos:                
                if(doc.obtIdAlumno()== cod):
                    k = True
                    listAux.append(docModi)
                else:
                    listAux.append(doc)
       
        if(k == True):
            self.Alumnos = listAux
            self.almacenarEnArchivo()
            print("\nAlumno ",cod," Modificado exinosamente ...")
        else:
            print("\nCodigo de Alumno ",cod," no existe !!!")

    def listarTodosAlumnos(self):
        if len(self.Alumnos) == 0:
            print("No hay Alumnos...")
            return
        print("------------------------------------------------------------------------------------")
        print("                   <<< ***   LISTA DE ALUMNOS    ****>>>")
        print("------------------------------------------------------------------------------------")
        print(" Codigo        Nombre  y Apellido             E-mail                    Celular")
        print("------------------------------------------------------------------------------------")
        for doc in self.Alumnos:
            #print(alum)
            print('{0:7}     {1:30} {2:30} {3:10}'.format(doc.obtIdAlumno(),doc.obtNombre(),doc.obtEmail(),doc.obtCelular()))
        print("------------------------------------------------------------------------------------")


    def verSiExisteAlumno(self,cod): #verifica si ya existe un registro con el mismo id, retorna TRUE si existe
        existe = False
        if len(self.Alumnos) == 0:
            return(existe)
        
        for doc in self.Alumnos:
            if(doc.obtIdAlumno() == cod):
                existe = True
                break
        return (existe)

    def validaUsrAlumno(self, mail,pwd):
        existe = False
        cod = 0
        if len(self.Alumnos) == 0:
            return(existe)

        for doc in self.Alumnos:
            if(doc.obtEmail() == mail):
                if(doc.obtPassword() == pwd):
                    cod = doc.obtIdAlumno()
                    existe = True
                    break
        return (cod)

# --Main de Alumno()
def menuAlumno():
    aa = ArchivoAlumno()
    while True:
        os.system('color 1f')
        print("\n\t-----------------------------------------------")
        print("\t\t<< ** MENU DE ALUMNOS ** >>")
        print("\t-----------------------------------------------")
        print("\t1. Adicionar nuevo Alumno")
        print("\t2. Buscar por codigo y mostrar un determinado Alumno")
        print("\t3. Modificar/Editar datos de un Alumno")
        print("\t4. Eliminar un Alumno")
        print("\t5. Listar todos los Alumnos")
        print("\t0. Salir")
        print("\t-----------------------------------------------")
        opc = int(input("\tSelecciona una opcion : "))
        os.system('cls')
        if opc == 1:
            while True:  # valida para no intorducir codigos duplicados
                cod = int(input("Codigo : "))
                if(aa.verSiExisteAlumno(cod) == True):
                    print("\nCodigo ya existe..!!!, intente con otro codigo..")
                else:
                    break

            nombre = input("Nombre y apellido : ")
            celu = input("Nro de Celular : ")
            mail = input("e-Mail : ")
            pwd     = pfxBoxTools.getpass("Password : ")
            aa.adiconar(Alumno(cod, nombre, mail, celu,pwd))
        elif opc == 2:
            cod = int(input("Codigo  de Alumno a buscar : "))
            aa.buscarMostrarUnAlumno(cod)
        elif opc == 3:
            cod = int(input("Codigo  del Alumno a modificar sus datos? : "))
            if(aa.buscarMostrarUnAlumno(cod) == True):
                nombre  = input("Nuevo Nombre y apellido: ")
                celu    = input("Nueva Nro de Celular : ")
                mail    = input("Nueva e-Mail : ")
                pwd     = pfxBoxTools.getpass("Nuevo Password : ")
                aa.modificarUnAlumno(Alumno(cod, nombre, mail, celu,pwd))
        elif opc == 4:
            cod = int(input("Codigo  de Alumno a eliminar : "))
            aa.eliminarUnAlumno(cod)
        elif opc == 5:
            aa.listarTodosAlumnos()
        elif opc == 0:
            os.system('color 0f')
            break
        else:
            os.system('color 4f')
            print('Se introdujo un valor fuera de las opciones')

        os.system('pause')



def menuUsuarioAlumno(cod):
    aa = ArchivoAlumno()
    objOferta = pfxOfertaCurso.ArchivoOferta()
    objClases = pfxClasesProgramada.ArchivoClase()
    print("\n------------------------------ B I E N V E N I D O ------------------------------------------")
    aa.buscarMostrarUnAlumno(cod)
    print("---------------------------------------------------------------------------------------------")
    while True:
        os.system('color 1f')
        print("\n\t-----------------------------------------------")
        print("\t\t<< ** MENU DE USUARIO DE ALUMNOS ** >>")
        print("\t-----------------------------------------------")
        print("\t1. Mi Perfil")
        print("\t2. Editar mi peril")
        print("\t3. Ver ofertas de cursos")
        print("\t4. Programar una clase")
        print("\t5. Ver mis clases programadas")
        print("\t0. Salir")
        print("\t-----------------------------------------------")
        opc = int(input("\tSelecciona una opcion : "))
        os.system('cls')
        if opc == 1:
            aa.buscarMostrarUnAlumno(cod)
        elif opc == 2:
            if(aa.buscarMostrarUnAlumno(cod) == True):
                nombre  = input("Nuevo Nombre y apellido: ")
                celu    = input("Nueva Nro de Celular : ")
                mail    = input("Nueva e-Mail : ")
                pwd     = pfxBoxTools.getpass("Nuevo Password : ")
                aa.modificarUnAlumno(Alumno(cod, nombre, mail, celu,pwd))
        elif opc == 3:
            objOferta.listarTodosOfertas()
        elif opc == 4:
            objOferta.listarTodosOfertas()
            print("\n\n*****************************************************************************")
            print("---->> Introducir los siguientes datos para programar una nueva clase --->>")
            
            pfxClasesProgramada.entradaParaAdicionar(objClases,cod)
        elif opc == 5:
            objClases.listarTodosClases(cod)
        elif opc == 0:
            os.system('color 0f')
            break
        else:
            os.system('color 4f')
            print('Se introdujo un valor fuera de las opciones')

        os.system('pause')

