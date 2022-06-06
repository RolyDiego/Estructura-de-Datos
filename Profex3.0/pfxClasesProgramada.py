#APROFEX
# Diego Martinez Garzon - 29/05/2022
import os
import pickle
import pfxAlumno
import pfxOfertaCurso

class Clase:
    def __init__(self, idDoc, idAlum, idOfer, canHra, fcha, hraIni, tPrecio, est):
        self.idClase        = idDoc
        self.fkIdAlumno     = idAlum
        self.fkIdOferta     = idOfer
        self.cantHoras      = canHra
        self.fecha          = fcha
        self.horaIni        = hraIni
        self.TotPrecio      = tPrecio
        self.estado         = est

    def obtIdClase(self):
        return (self.idClase)

    def obtFkIdAlumno(self):
        return (self.fkIdAlumno)

    def obtFkIdOferta(self):
        return (self.fkIdOferta)

    def obtCantHoras(self):
        return (self.cantHoras)

    def obtFecha(self):
        return (self.fecha)

    def obtHoraIni(self):
        return (self.horaIni)

    def obtTotPrecio(self):
        return (self.TotPrecio)

    def obtEstado(self):
        return (self.estado)

    def __str__(self):
        return '{:7} {:7} {:7} {:7} {:8}  {:8}  {:8}  {:8} '.format(self.idClase, self.fkIdAlumno, self.fkIdOferta, self.cantHoras,self.fecha,self.horaIni,self.TotPrecio,self.estado)


class ArchivoClase:
    Clases = []  # lista donde se gestionaran los datos de los Clases

    def __init__(self,):
        self.NomArchivo = 'pfxClase.pkl'
        self.cargaArchivoEnLista()
        self.objAlumno  = pfxAlumno.ArchivoAlumno()
        self.objOferta  = pfxOfertaCurso.ArchivoOferta()

    def cargaArchivoEnLista(self):
        fichero = open(self.NomArchivo, 'ab+')
        fichero.seek(0)
        try:
            self.Clases = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            #print("Se han cargado {} Clases..".format(len(self.Clases)))

    def adiconar(self, doc):  # recibo un objeto de la clase alumno con los datos ya cargados
        self.Clases.append(doc)  # adiciona en la lista
        self.almacenarEnArchivo()  # lo escribe en el archivo binario

    def almacenarEnArchivo(self):
        # crea de nuevo contenido de archivo
        fichero = open(self.NomArchivo, 'wb')
        pickle.dump(self.Clases, fichero)
        fichero.close()

    def buscarMostrarUnClase(self, cod):
        if len(self.Clases) == 0:
            print("No hay Clases...")
            return
        k = False
        for doc in self.Clases:
            if(doc.obtIdClase() == cod):
                print(doc)
                k = True
                break

        if(k == False):
            print("\nCodigo de Clase ", cod, " no existe !!!")
        return k

    def eliminarUnClase(self, cod):
        if len(self.Clases) == 0:
            print("No hay Clases...")
            return
        k = False
        listAux = []
        for doc in self.Clases:
            if(doc.obtIdClase() == cod):
                k = True
            else:
                listAux.append(doc)

        if(k == True):
            self.Clases = listAux
            self.almacenarEnArchivo()
            print("\nClase ", cod, " eliminado exinosamente ...")
        else:
            print("\nCodigo de Clase ", cod, " no existe !!!")

    def modificarUnClase(self, docModi):
        if len(self.Clases) == 0:
            print("No hay Clases...")
            return
        cod = docModi.obtIdClase()
        k = False
        listAux = []
        for doc in self.Clases:
            if(doc.obtIdClase() == cod):
                k = True
                listAux.append(docModi)
            else:
                listAux.append(doc)

        if(k == True):
            self.Clases = listAux
            self.almacenarEnArchivo()
            print("\nClase ", cod, " Modificado exinosamente ...")
        else:
            print("\nCodigo de Clase ", cod, " no existe !!!")

    def listarTodosClases(self,idAlum):
        if len(self.Clases) == 0:
            print("No hay Clases...")
            return
        print("----------------------------------------------------------------------------------------------")
        print("                      <<< ***   LISTA DE CLASES PROGRAMADAS    ****>>>")
        print("----------------------------------------------------------------------------------------------")
        print(" Codigo  CodAlumno   CodOferta   CantHoras   Fecha     HoraInicio    PrecioTotal   Estado")
        print("----------------------------------------------------------------------------------------------")
        for doc in self.Clases:
            if(idAlum == -1):
                print('{:7} {:7}    {:7}      {:7}     {:8}    {:8}  {:8}        {:8}'.format( doc.obtIdClase(), doc.obtFkIdAlumno(), doc.obtFkIdOferta(), doc.obtCantHoras(),doc.obtFecha(),doc.obtHoraIni(),doc.obtTotPrecio(),doc.obtEstado() ))
            elif(idAlum == doc.obtFkIdAlumno()):
                print('{:7} {:7}    {:7}      {:7}     {:8}    {:8}  {:8}        {:8}'.format( doc.obtIdClase(), doc.obtFkIdAlumno(), doc.obtFkIdOferta(), doc.obtCantHoras(),doc.obtFecha(),doc.obtHoraIni(),doc.obtTotPrecio(),doc.obtEstado() ))
                
        print("----------------------------------------------------------------------------------------------")

    def listarTodosClasesDocente(self,idAlum):
        if len(self.Clases) == 0:
            print("No hay Clases...")
            return
        print("----------------------------------------------------------------------------------------------")
        print("                      <<< ***   LISTA DE CLASES PROGRAMADAS    ****>>>")
        print("----------------------------------------------------------------------------------------------")
        print(" Codigo  CodAlumno   CodOferta   CantHoras   Fecha     HoraInicio    PrecioTotal   Estado")
        print("----------------------------------------------------------------------------------------------")
        for doc in self.Clases:
            if(idAlum == -1):
                print('{:7} {:7}    {:7}      {:7}     {:8}    {:8}  {:8}        {:8}'.format( doc.obtIdClase(), doc.obtFkIdAlumno(), doc.obtFkIdOferta(), doc.obtCantHoras(),doc.obtFecha(),doc.obtHoraIni(),doc.obtTotPrecio(),doc.obtEstado() ))
            elif(idAlum == doc.obtFkIdAlumno()):
                print('{:7} {:7}    {:7}      {:7}     {:8}    {:8}  {:8}        {:8}'.format( doc.obtIdClase(), doc.obtFkIdAlumno(), doc.obtFkIdOferta(), doc.obtCantHoras(),doc.obtFecha(),doc.obtHoraIni(),doc.obtTotPrecio(),doc.obtEstado() ))
                
        print("----------------------------------------------------------------------------------------------")



    # verifica si ya existe un registro con el mismo id, retorna TRUE si existe
    def verSiExisteClase(self, cod):
        existe = False
        if len(self.Clases) == 0:
            return(existe)

        for doc in self.Clases:
            if(doc.obtIdClase() == cod):
                existe = True
                break
        return (existe)

    def obtNombreClase(self, cod):#retorna el nombre de Clase desde archivo lista
        nombreDoc = ""
        for doc in self.Clases:
            if(doc.obtIdClase() == cod):
                existe = True
                nombreDoc = doc.obtNombre()
                break
        return (nombreDoc)

#FIN ArchivoClase

def entradaParaAdicionar(aa,idAlum):
        while True:  # valida para no intorducir codigos duplicados
            cod = int(input("Codigo de nueva clase a programar : "))
            if(aa.verSiExisteClase(cod) == True):
                print("\nCodigo ya existe..!!!, intente con otro codigo..")
            else:
                break

        while True:  # valida que exista el codigo del curso 
            if(idAlum == -1):
                idAlum      = int(input("Codigo de Alumno : "))
            if(aa.objAlumno.verSiExisteAlumno(idAlum) == False):
                print("\nCodigo de Alumno NO existe..!!!, intente con otro codigo..")
            else: break

        while True:  # valida que exista el codigo del curso 
            idOfer      = int(input("Codigo de la OFERTA seleccionada : "))
            if(aa.objOferta.verSiExisteOferta(idOfer) == False):
                print("\nCodigo de oferta de cursos NO existe..!!!, intente con otro codigo..")
            else: break

        canHra      = int(input("Cantidad de horas a contratar: "))
        precioHora  = aa.objOferta.obtPrecioOfertaCurso(idOfer)
        tPrecio     = precioHora * canHra
        print("\nTotal precios a Pagar es --->> ",tPrecio)
        fcha        = input("\nFecha de la clase a realiar : ")
        hraIni      = input("Hora de la clase : ")            
        est         = input("Estado : ")
        aa.adiconar(Clase(cod, idAlum,idOfer,canHra,fcha,hraIni,tPrecio,est))



# --Main de Clases()
#k = True
#if k == True :
def menuClase():
    aa = ArchivoClase()
    while True:
        os.system('color 1f')
        print("\n\t-----------------------------------------------")
        print("\t\t<< ** MENU DE PROGRAMAR CLASES ** >>")
        print("\t-----------------------------------------------")
        print("\t1. Adicionar nueva Clase progamada")
        print("\t2. Buscar por codigo y mostrar un determinado Clase")
        print("\t3. Modificar/Editar datos de un Clase")
        print("\t4. Eliminar un Clase")
        print("\t5. Listar todos los Clases")
        print("\t0. Salir")
        print("\t-----------------------------------------------")
        opc = int(input("\tSelecciona una opcion : "))
        os.system('cls')
        if opc == 1:
            entradaParaAdicionar(aa,-1)
        elif opc == 2:
            cod = int(input("Codigo  de Clase a buscar : "))
            aa.buscarMostrarUnClase(cod)
        elif opc == 3:
            cod = int(input("Codigo  del Clase a modificar sus datos? : "))
            if(aa.buscarMostrarUnClase(cod) == True):
                while True:  # valida que exista el codigo del curso 
                    idAlum      = int(input("Codigo de Alumno : "))
                    if(aa.objAlumno.verSiExisteAlumno(idAlum) == False):
                        print("\nCodigo de Alumno NO existe..!!!, intente con otro codigo..")
                    else: break
            
                while True:  # valida que exista el codigo del curso 
                    idOfer      = int(input("Codigo de la OFERTA seleccionada : "))
                    if(aa.objOferta.verSiExisteOferta(idOfer) == False):
                        print("\nCodigo de oferta de cursos NO existe..!!!, intente con otro codigo..")
                    else: break

                canHra      = int(input("Cantidad de horas a contratar: "))
                precioHora  = aa.objOferta.obtPrecioOfertaCurso(idOfer)
                tPrecio     = precioHora * canHra
                print("\nTotal precios a Pagar es --->> ",tPrecio)
                fcha        = input("\nFecha de la clase a realiar : ")
                hraIni      = input("Hora de la clase : ")            
                est         = input("Estado : ")
                     
                aa.modificarUnClase(Clase(cod, idAlum,idOfer,canHra,fcha,hraIni,tPrecio,est))

        elif opc == 4:
            cod = int(input("Codigo  de Clase a eliminar : "))
            aa.eliminarUnClase(cod)
        elif opc == 5:
            aa.listarTodosClases(-1)
        elif opc == 0:
            os.system('color 0f')
            break
        else:
            os.system('color 4f')
            print('Se introdujo un valor fuera de las opciones')

        os.system('pause')
