#APROFEX
# Diego Martinez Garzon - 29/05/2022
import os
import pickle
import pfxDocente
import pfxCursos

class Oferta:
    def __init__(self, idOfer, idCur, idDoc, precio):
        self.idOferta       = idOfer
        self.fkIdCurso      = idCur
        self.fkIdDocente    = idDoc
        self.precioHora     = precio

    def obtIdOferta(self):
        return (self.idOferta)

    def obtFkIdCurso(self):
        return (self.fkIdCurso)

    def obtFkIdDocente(self):
        return (self.fkIdDocente)

    def obtPrecio(self):
        return (self.precioHora)

    def __str__(self):
        return '{:7} {:30} {:40} {:10}'.format(self.idOferta, self.fkIdCurso, self.fkIdDocente, self.precioHora)


class ArchivoOferta:
    Ofertas = []  # lista donde se gestionaran los datos de los Ofertas
    
    def __init__(self,):
        self.NomArchivo = 'pfxOferta.pkl'
        self.cargaArchivoEnLista()
        self.objDocente = pfxDocente.ArchivoDocente()
        self.objCurso   = pfxCursos.ArchivoCurso()

    def cargaArchivoEnLista(self):
        fichero = open(self.NomArchivo, 'ab+')
        fichero.seek(0)
        try:
            self.Ofertas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            #print("Se han cargado {} Ofertas..".format(len(self.Ofertas)))

    def adiconar(self, doc):  # recibo un objeto de la clase alumno con los datos ya cargados
        self.Ofertas.append(doc)  # adiciona en la lista
        self.almacenarEnArchivo()  # lo escribe en el archivo binario

    def almacenarEnArchivo(self):
        # crea de nuevo contenido de archivo
        fichero = open(self.NomArchivo, 'wb')
        pickle.dump(self.Ofertas, fichero)
        fichero.close()

    def buscarMostrarUnOferta(self, cod):
        if len(self.Ofertas) == 0:
            print("No hay Ofertas...")
            return
        k = False
        for doc in self.Ofertas:
            if(doc.obtIdOferta() == cod):
                print(doc)
                k = True
                break

        if(k == False):
            print("\nCodigo de Oferta ", cod, " no existe !!!")
        return k

    def eliminarUnOferta(self, cod):
        if len(self.Ofertas) == 0:
            print("No hay Ofertas...")
            return
        k = False
        listAux = []
        for doc in self.Ofertas:
            if(doc.obtIdOferta() == cod):
                k = True
            else:
                listAux.append(doc)

        if(k == True):
            self.Ofertas = listAux
            self.almacenarEnArchivo()
            print("\nOferta ", cod, " eliminado exinosamente ...")
        else:
            print("\nCodigo de Oferta ", cod, " no existe !!!")

    def modificarUnOferta(self, docModi):
        if len(self.Ofertas) == 0:
            print("No hay Ofertas...")
            return
        cod = docModi.obtIdOferta()
        k = False
        listAux = []
        for doc in self.Ofertas:
            if(doc.obtIdOferta() == cod):
                k = True
                listAux.append(docModi)
            else:
                listAux.append(doc)

        if(k == True):
            self.Ofertas = listAux
            self.almacenarEnArchivo()
            print("\nOferta ", cod, " Modificado exinosamente ...")
        else:
            print("\nCodigo de Oferta ", cod, " no existe !!!")

    def listarTodosOfertas(self):
        if len(self.Ofertas) == 0:
            print("No hay Ofertas...")
            return
        print("-----------------------------------------------------------------------------------------------------")
        print("                             <<< ***   LISTA DE OFERTAS DE CURSOS    ****>>>")
        print("-----------------------------------------------------------------------------------------------------")
        print(" Codigo  CodCurso  Nombre Curso                 CodDocente     Nombre Docente           Precio Hora")
        print("-----------------------------------------------------------------------------------------------------")
        for doc in self.Ofertas:
            print('{0:7}   {1:7}   {2:30} {3:7}  {4:30} {5:10}'.format(doc.obtIdOferta(), doc.obtFkIdCurso(), self.objCurso.obtNombreCurso(doc.obtFkIdCurso()),doc.obtFkIdDocente(), self.objDocente.obtNombreDocente(doc.obtFkIdDocente()), doc.obtPrecio()))
        print("-----------------------------------------------------------------------------------------------------")
        
    # verifica si ya existe un registro con el mismo id, retorna TRUE si existe
    def verSiExisteOferta(self, cod):
        existe = False
        if len(self.Ofertas) == 0:
            return(existe)

        for doc in self.Ofertas:
            if(doc.obtIdOferta() == cod):
                existe = True
                break
        return (existe)

    def obtPrecioOfertaCurso(self, cod):#retorna el nombre de docente desde archivo lista
        precio = 0
        for doc in self.Ofertas:
            if(doc.obtIdOferta() == cod):
                precio = doc.obtPrecio()
                break
        return (precio)

# --Main de Ofertas()
def menuOferta():
#k = True
#if k == True :
    aa = ArchivoOferta()
    while True:
        os.system('color 1f')
        print("\n\t-----------------------------------------------")
        print("\t\t<< ** MENU DE OFERTAS DE CURSOS ** >>")
        print("\t-----------------------------------------------")
        print("\t1. Adicionar nuevo Oferta")
        print("\t2. Buscar por codigo y mostrar un determinado Oferta")
        print("\t3. Modificar/Editar datos de un Oferta")
        print("\t4. Eliminar un Oferta")
        print("\t5. Listar todos los Ofertas")
        print("\t0. Salir")
        print("\t-----------------------------------------------")
        opc = int(input("\tSelecciona una opcion : "))
        os.system('cls')
        if opc == 1:
            while True:  # valida para no intorducir codigos duplicados
                cod = int(input("Codigo de oferta: "))
                if(aa.verSiExisteOferta(cod) == True):
                    print("\nCodigo ya existe..!!!, intente con otro codigo..")
                else:
                    break

            while True:  # valida que exista el codigo del curso 
                idCur = int(input("Codigo de Curso : "))
                if(aa.objCurso.verSiExisteCurso(idCur) == False):
                    print("\nCodigo de Curso NO existe..!!!, intente con otro codigo..")
                else: break
            
            while True:  # valida que exista el codigo del docente 
                idDoc = int(input("Codigo de Docente que dicta el curso : "))
                if(aa.objDocente.verSiExisteDocente(idDoc) == False):
                    print("\nCodigo de Docente NO existe..!!!, intente con otro codigo..")
                else: break

            idPre = float(input("Precio por hora : "))
            aa.adiconar(Oferta(cod,idCur,idDoc,idPre))
        elif opc == 2:
            cod = int(input("Codigo  de Oferta a buscar : "))
            aa.buscarMostrarUnOferta(cod)
        elif opc == 3:
            cod = int(input("Codigo  del Oferta a modificar sus datos? : "))
            if(aa.buscarMostrarUnOferta(cod) == True):
                while True:  # valida que exista el codigo del curso 
                    idCur = int(input("Codigo de Curso : "))
                    if(aa.objCurso.verSiExisteCurso(idCur) == False):
                        print("\nCodigo de Curso NO existe..!!!, intente con otro codigo..")
                    else: break

                while True:  # valida que exista el codigo del docente 
                    idDoc = int(input("Codigo de Docente que dicta el curso : "))
                    if(aa.objDocente.verSiExisteDocente(idDoc) == False):
                        print("\nCodigo de Docente NO existe..!!!, intente con otro codigo..")
                    else: break

                idPre = float(input("Precio por hora : "))
                aa.modificarUnOferta(Oferta(cod, idCur,idDoc,idPre))
        elif opc == 4:
            cod = int(input("Codigo  de Oferta a eliminar : "))
            aa.eliminarUnOferta(cod)
        elif opc == 5:
            aa.listarTodosOfertas()
        elif opc == 0:
            os.system('color 0f')
            break
        else:
            os.system('color 4f')
            print('Se introdujo un valor fuera de las opciones')

        os.system('pause')
