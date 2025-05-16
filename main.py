#PROGRAMA QUE PERMITE REGISTRAR Y MONITOREAR TUS GASTOS DIARIOS EN DIFERENTES CATEGORIAS

'''
=============================================
         Simulador de Gasto Diario
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Salir
=============================================

'''

from funciones.funcionesGGDD import *
from funciones.funcionesCode import *

listaGastos = abrirJSON() #guardamos los datos del archivo .json en una variable llamada listaGastos
ejecucionPrograma = True # variable para usar en el while que determina cuando termina el programa

while (ejecucionPrograma): 
    print("=============================================") #Lista de opciones que podrá realizar el usuario en el programa
    print("         Simulador de Gasto Diario")
    print("=============================================")
    opcionUsuario = int(input(("Seleccione una opción:")))
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")

    if(opcionUsuario == 1):
        print("=============================================")
        print("Registrar Nuevo Gasto")
        print("=============================================")
        print("Ingrese la información del gasto:\n")
        montoGasto = float(input("- Monto del gasto: "))
        categoriaGasto = input("- Categoría (ej. comida, transporte, entretenimiento, otros):")
        descripcionGasto = input("- Descripción (opcional):")

        dirGastos = {
            "monto":montoGasto,
            "categoria":categoriaGasto,
            "descripcion":descripcionGasto
        }

        seleccion = input("Ingrese 'S' para guardar o 'C' para cancelar.")

        if (seleccion == "S"):
            listaGastos.append(dirGastos)
            guardarJSON(listaGastos)
        print("=============================================")


    elif(opcionUsuario == 4):
        print("Ejecución terminada. \n !Nos vemos pronto¡")
        ejecucionPrograma = False

