import os 
import numpy
import lib
casa=numpy.empty([10,4],type(int))
lib.asignardepartamento(casa)
op=1
Rut=[]
aS=[]
while(op!=6):
    print("\n\tCASA FELIZ")
    print("***********************")
    print("1.   COMPRAR DEPARTAMENTO")
    print("2.   MOSTRA DEPARTAMENTOS DISPONIBLES") 
    print("3.   VER LISTADO DE COMPRADORES")
    print("4.   MOSTRA GANANCIAS TOTALES")
    print("5.   SALIR")
    op=lib.validaDatos("\nElija una opcion: ",1,6)
    if(op==1):
        print(casa)
        print("\tLos Departamento disponibles son:")
        lib.mostrardepartamento(casa)
        n=lib.validaDatos("\tIngrese N° de departamento: ",1,40)
        if(lib.estaDisponible(casa,n)==1):
            print("\nDebe cancelar: "+str(lib.precio(casa,n))+" UF")
            lib.rutcomprador(casa,n,aS,Rut)
            lib.vender(casa,n)
        else:
            print("\n\tEl departamento solicitado ya esta ocupado") 
    if(op==2):
        
        print("Departamentos disponibles: ")
        print(casa)
        input("<<Enter para continuar>>")
    if(op==3):
        if len(Rut)!=0:
            print("\nRut de los compradores: "+str(Rut))
    if(op==4):
        print("TIPO DEPARTAMENTO        CANTIDAD        TOTAL")
        print("tipo A 3800 UF            "+str(lib.cantA(casa))+"               "+str(lib.totalPagadoA(casa)))
        print("tipo A 3000 UF            "+str(lib.cantB(casa))+"               "+str(lib.totalPagadoB(casa)))
        print("tipo A 2000 UF            "+str(lib.cantC(casa))+"               "+str(lib.totalPagadoC(casa)))
        print("tipo A 3500 UF            "+str(lib.cantD(casa))+"               "+str(lib.totalPagadoD(casa)))  