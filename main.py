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

from datetime import datetime
from funciones.funcionesGGDD import *
from funciones.funcionesCode import *

print("=============================================")
print("¡BIENVENIDO AL PROGRAMA!")
print("=============================================\n")


listaGastos = abrirJSON() #guardamos los datos del archivo .json en una variable llamada listaGastos
ejecucionPrograma = True # variable para usar en el while que determina cuando termina el programa

while (ejecucionPrograma): 
    print("=============================================") #Lista de opciones que podrá realizar el usuario en el programa
    print("         Simulador de Gasto Diario")
    print("=============================================\n")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================\n")

    opcionUsuario = int(input(("Seleccione una opción:\n")))
    if(opcionUsuario == 1):
        print("=============================================")
        print("Registrar Nuevo Gasto")
        print("=============================================\n")
        print("Ingrese la información del gasto:\n")
        montoGasto = float(input("- Monto del gasto: "))
        categoriaGasto = input("- Categoría (ej. comida, transporte, entretenimiento, otros): ")
        descripcionGasto = input("- Descripción (opcional): ")
        print("\n=============================================")
        eleccionFecha = int(input("Digite 1. si el gasto se ha realizado el dia de hoy o 2 si el gasto se ha realizado en otra fecha: "))
        print("=============================================\n")
        if(eleccionFecha == 1):
            fechaActual = str(datetime.now()) #fecha del momento en que se ingresa el gasto
            dirGastos = {
            "monto":montoGasto,
            "categoria":categoriaGasto,
            "descripcion":descripcionGasto,
            "fecha":fechaActual
                        }
            
        elif(eleccionFecha == 2):
            fechaDiferente = datetime(input("Por favor digite la fecha y la hora del gasto: "))
            dirGastos = {
            "monto":montoGasto,
            "categoria":categoriaGasto,
            "descripcion":descripcionGasto,
            "fecha":fechaDiferente
                        }
        seleccion = input("Ingrese 'S' para guardar o 'C' para cancelar.")
        seleccion.capitalize

        if (seleccion == "S"):
            listaGastos.append(dirGastos)
            guardarJSON(listaGastos)
            print("¡DATOS GUARDADOS CON ÉXITO!")
            print("=============================================\n")

        elif (seleccion == "C"):
            listaGastos.append(dirGastos)
            print("¡LOS DATOS NO SE HAN ALMACENADO!")
            print("=============================================\n")

    elif(opcionUsuario == 5):
        print("Ejecución terminada. \n !Nos vemos pronto¡")
        ejecucionPrograma = False

