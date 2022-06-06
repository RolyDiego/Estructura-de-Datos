#APROFEX
# Diego Martinez Garzon - 29/05/2022
import os
import pfxDocente
import pfxAlumno
import pfxOfertaCurso
import pfxCursos
import pfxBoxTools
import pfxClasesProgramada

def iniciaSesionUsuario(codigo):
        print("\n\t----------------- Inicio de Sesion -----------")
        logEmial = input("\t\tLogin : ")
        pwd     = pfxBoxTools.getpass("\t\tPassword : ")
        print("\t-----------------------------------------------")
        tipoUsr = "Z"  
        cod = 0
        if(tipoUsr == "Z"):
                objDoc = pfxAlumno.ArchivoAlumno()
                cod = objDoc.validaUsrAlumno(logEmial,pwd)
                if( cod != 0):
                        codigo[0] = cod
                        tipoUsr = "A"
        if(tipoUsr == "Z"):
                objDoc = pfxDocente.ArchivoDocente()
                cod = objDoc.validaUsrDocente(logEmial,pwd)
                if( cod != 0):
                        codigo[0] = cod
                        tipoUsr = "D"
        if(tipoUsr == "Z"):
                if(pfxBoxTools.verifAdmin(logEmial,pwd) == True):
                        tipoUsr = "X"
                        codigo[0] = 777

        return(tipoUsr)


def menuPrincipal():
        codigo = [-1]
        while True:
                os.system('color 1f')
                print ("\n\t========================================================")
                print("\t\t<< ** BIENVENIDO A PROFEX ** >>")
                print ("\t--------------------------------------------------------")
                print ("\tBy team ->")
                print ("\t\tDiego Martinez ")
                print ("\t\tJorge Saucedo ")
                print ("\t\tAugusto Carrizales ")
                print ("\t\tJulian Gomez ")
                print ("\t========================================================")
                tipoUsr = iniciaSesionUsuario(codigo)
                cod = codigo[0]
                if tipoUsr == "D":
                        pfxDocente.menuUsuarioDocente(cod)
                elif tipoUsr == "A":
                        pfxAlumno.menuUsuarioAlumno(cod)
                elif tipoUsr == "X":
                        menuAdmin()
                elif tipoUsr == "Z":
                        print("\n\tUsario no existe  o email/password es incorrecto.....")
                        op = input("\n\tDseas registrarte como un nuevo usuario <S/N> ? :")
                        if(op == "S" or op == "s"):
                                oppp = int(input("\n\t1.- Como Alumno \n\t2.- Como Docente \n\tSelecciones Opcion : "))
                                if(oppp == 2): #como docente
                                        aa = pfxDocente.ArchivoDocente()
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
                                        aa.adiconar(pfxDocente.Docente(cod, nombre, mail, celu,pwd))       
                                        
                                        pfxDocente.menuUsuarioDocente(cod)   
                                if(oppp == 1): 
                                        aa = pfxAlumno.ArchivoAlumno()
                                        while True:  # valida para no intorducir codigos duplicados
                                                cod = int(input("Codigo : "))
                                                if(aa.verSiExisteAlumno(cod) == True):
                                                        print("\nCodigo ya existe..!!!, intente con otro codigo..")
                                                else: break

                                        nombre = input("Nombre y apellido : ")
                                        celu = input("Nro de Celular : ")
                                        mail = input("e-Mail : ")
                                        pwd     = pfxBoxTools.getpass("Password : ")
                                        aa.adiconar(pfxAlumno.Alumno(cod, nombre, mail, celu,pwd))

                                        pfxAlumno.menuUsuarioAlumno(cod)       
                print("\n\n\tProFex te dice: Hasta la proxima ...!!!")
                os.system('pause')
                os.system('color 0f')
                break
                

def menuAdmin():
        print("\n------------------------------ B I E N V E N I D O ------------------------------------------")
        print("\t\t\t Aministrador del sistema ProFex")
        print("---------------------------------------------------------------------------------------------")
        while True:
                os.system('color 1f')
                print ("\n\t===============================================")
                print("\t\t<< ** PROFEX MENU ADMIN ** >>")
                print ("\t===============================================")
                print("\t1. Gestionar Docentes")
                print("\t2. Gestionar Alumnos")
                print("\t3. Gestionar Curso")
                print("\t4. Gestionar Ofertas de Cursos")
                print("\t5. Gestionar Solicitar clases a programar")
                print("\t0. Salir")
                print ("\t===============================================")
                opc = int(input("\tSelecciona una opcion : "))
                os.system('cls')
                if opc == 1:
                        pfxDocente.menuDocente()
                elif opc == 2:
                        pfxAlumno.menuAlumno()
                elif opc == 3:
                        pfxCursos.menuCurso()
                elif opc == 4:
                        pfxOfertaCurso.menuOferta()
                elif opc == 5:
                        pfxClasesProgramada.menuClase()
                elif opc == 0:
                        os.system('color 0f')
                        break        
                else:
                        os.system('color 4f')
                        print('Se introdujo un valor fuera de las opciones')

                # os.system('pause')
                
#main
menuPrincipal()
