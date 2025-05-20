#PROGRAMA QUE PERMITE REGISTRAR Y MONITOREAR TUS GASTOS DIARIOS EN DIFERENTES CATEGORIAS
from datetime import datetime
from funciones.funcionesGGDD import *
from funciones.funcionesCode import *

print("=============================================")
print("         ¡BIENVENIDO AL PROGRAMA!")
print("=============================================\n")


listaGastos = abrirJSON() #guardamos los datos del archivo .json en una variable llamada listaGastos
ejecucionPrograma = True # variable para usar en el while que determina cuando termina el programa

while(ejecucionPrograma): 
    
    print("=============================================") #Lista de opciones que podrá realizar el usuario en el programa
    print("         Simulador de Gasto Diario")
    print("=============================================\n")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")

    opcionUsuario = int(input(("Seleccione una opción: ")))
    while(opcionUsuario <1 or opcionUsuario >5):
        opcionUsuario = int(input(("Opción incorrecta. Por favor valida las opciones y vuelve a intentarlo.\n")))


    if(opcionUsuario == 1):
        print("=============================================")
        print("Registrar Nuevo Gasto")
        print("=============================================\n")
        print("Ingrese la información del gasto:\n")
        montoGasto = float(input("- Monto del gasto: "))
        categoriaGasto = input("- Categoría (ej. comida, transporte, entretenimiento, otros): ")
        descripcionGasto = input("- Descripción (opcional): ")
        dirGastos = {
            "monto":montoGasto, 
            "categoria":categoriaGasto,
            "descripcion":descripcionGasto,
            "fecha":[]
                        }
        
        print("\n=============================================")
        eleccionFecha = int(input("Digite 1. si el gasto se ha realizado el dia de hoy o 2 si el gasto se ha realizado en otra fecha: "))
        print("=============================================\n")
        if(eleccionFecha == 1):
            fechaActual = (datetime.now()) #fecha del momento en que se ingresa el gasto
            diaAhora = str(fechaActual.day)
            mesAhora = str(fechaActual.month)
            anioAhora = str(fechaActual.year)
            horaAhora = str(fechaActual.hour)
            minutosAhora = str(fechaActual.minute)
            
            dirFecha = {"dia":diaAhora+"-"+mesAhora+"-"+anioAhora,
                        "hora": horaAhora+":"+minutosAhora}
            dirGastos["fecha"].append(dirFecha)
            #listaGastos.append(dirGastos)
            
        elif(eleccionFecha == 2):
            fecha2 = input("Por favor digite la fecha y la hora del gasto(año,mes,dia,hora,minutos)",)
            fechaDiferente = (datetime.strptime(fecha2,"%d,%m,%Y,%H,%M"))
            diaDif = str(fechaDiferente.day)
            mesDif = str(fechaDiferente.month)
            anioDif = str(fechaDiferente.year)
            horaDif = str(fechaDiferente.hour)
            minutos = str(fechaDiferente.minute)
            dirFecha = {"dia":diaDif+"-"+mesDif+"-"+anioDif,
                        "hora": horaDif+":"+mesDif}
            dirGastos["fecha"].append(dirFecha)
            #listaGastos.append(dirGastos)

            

        seleccion = input("Ingrese 'S' para guardar o 'C' para cancelar: ")
        seleccionMayus = seleccion.capitalize()

        if (seleccionMayus == "S"):
            listaGastos.append(dirGastos)
            guardarJSON(listaGastos)
            print("¡DATOS GUARDADOS CON ÉXITO!")
            print("=============================================\n")


        elif (seleccionMayus == "C"):
            
            print("¡LOS DATOS NO SE HAN ALMACENADO!")
            print("=============================================\n")
        
    elif(opcionUsuario == 2):
        print("=============================================")
        print("                Listar Gastos")
        print("=============================================")
        print("Seleccione una opción para filtrar los gastos: ")
        listarGasto = int(input("1. Ver todos los gastos \n2. Filtrar por categoría \n3. Filtrar por rango de fechas \n4. Regresar al menú principal\n"))
        #print("=============================================")
        
        if (listarGasto == 1):
            print("=============================================")
            print("                Todos los Gastos")
            print("=============================================")
            
            mostrarTodos(listaGastos)

        elif(listarGasto == 2):
            categoria = input("Por favor, digite la categoria que quieras consultar(ej. comida, transporte, entretenimiento, otros): \n")
            catergoriaMayus = categoria.lower()
            mostrarUna(listaGastos,categoria)

        elif(listarGasto == 3):
            print("=============================================")
            print("                Rango de fechas")
            print("=============================================")
            fechaInicialStr = input("Por favor, digite la fecha inicial(dd,mm,aaaa): ")
            fechaFinalStr  = input("Por favor, digite la fecha final(dd,mm,aaaa): ")
            fechaInicial =  datetime.strptime(fechaInicialStr,"%d-%m-%Y").date()
            fechaFinal = datetime.strptime(fechaFinalStr,"%d-%m-%Y").date()
            
            mostrarConFechas(listaGastos,fechaInicial,fechaFinal)
        elif(listarGasto == 4):
            print("=============================================")
            print("        Regresando al menú principal=========")
            print("=============================================")
            
    elif(opcionUsuario == 3):
        print("=============================================")
        print("               Calcular Gastos")
        print("=============================================")
        calcularGasto = int(input("Seleccione el periodo de cálculo: \n1. Calcular total diario \n2. Calcular total semanal \n3. Calcular total mensual \n4. Regresar al menú principal\n"))
        print("=============================================")
        
        if(calcularGasto == 1): #Total diario: Calcula y muestra el total de gastos del día actual.
            print("=============================================")
            print("               Total Gasto Diario")
            print("=============================================") 

        '''
=============================================
          Calcular Total de Gastos
=============================================
Seleccione el periodo de cálculo:

1. Calcular total diario
2. Calcular total semanal
3. Calcular total mensual
4. Regresar al menú principal
=============================================
'''


    elif(opcionUsuario == 5):
        print("Ejecución terminada. \n ¡Nos vemos pronto!")
        ejecucionPrograma = False

