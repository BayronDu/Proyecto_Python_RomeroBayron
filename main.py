#PROGRAMA QUE PERMITE REGISTRAR Y MONITOREAR TUS GASTOS DIARIOS EN DIFERENTES CATEGORIAS
from datetime import *
from funciones.funcionesGGDD import *
from funciones.funcionesCode import *

print("=============================================")
print("         ¡BIENVENIDO AL PROGRAMA!")
print("=============================================\n")


listaGastos = abrirJSON() #guardamos los datos del archivo .json en una variable llamada listaGastos
ejecucionPrograma = True # variable para usar en el while que determina cuando termina el programa

while(ejecucionPrograma): 
    
    print("="*linea) #Lista de opciones que podrá realizar el usuario en el programa
    print(f"Simulador de Gasto Diario".center(linea))
    print("="*linea)
    print("\n1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("="*linea)

    opcionUsuario = int(input(("Seleccione una opción: ")))
    while(opcionUsuario <1 or opcionUsuario >5):
        opcionUsuario = int(input(("Opción incorrecta. Por favor valida las opciones y vuelve a intentarlo.\n")))


    if(opcionUsuario == 1):
        print("="*linea)
        print(f"Registrar Nuevo Gasto".center(linea))
        print("="*linea)
        print("Ingrese la información del gasto:\n")
        montoGasto = float(input("- Monto del gasto: "))
        categoriaGasto = input("- Categoría (ej. comida, transporte, entretenimiento, otros): ")
        categoriaFormat = categoriaGasto.lower()
        descripcionGasto = input("- Descripción (opcional): ")
        dirGastos = {
            "monto":montoGasto, 
            "categoria":categoriaFormat,
            "descripcion":descripcionGasto,
            "fecha":[]
                        }
        
        print("="*linea)
        eleccionFecha = int(input("Digite 1. si el gasto se ha realizado el dia de hoy o 2 si el gasto se ha realizado en otra fecha: "))
        print("="*linea)
        while(eleccionFecha != 1 and eleccionFecha != 2):
                eleccionFecha = int(input(("Opción incorrecta. Por favor valida las opciones y vuelve a intentarlo.\n")))
        if(eleccionFecha == 1):
            

            fechaActual = (datetime.now()) #fecha del momento en que se ingresa el gasto
            fechaAhora = fechaActual.strftime("%d-%m-%Y")
            horaAhora = fechaActual.strftime("%H-%M")          
            dirFecha = {"dia":fechaAhora,
                        "hora": horaAhora}
            dirGastos["fecha"].append(dirFecha)
            #listaGastos.append(dirGastos)
            
        elif(eleccionFecha == 2):
            fecha2 = input(f"Por favor digite la fecha y la hora del gasto(dd-mm-aaaa HH-MM): ")
            fechaDiferente = (datetime.strptime(fecha2,"%d-%m-%Y %H-%M"))
            diaDif = fechaDiferente.strftime("%d-%m-%Y")
            horaDif = fechaDiferente.strftime("%H-%M")
            
            dirFecha = {"dia":diaDif,
                        "hora": horaDif}
            dirGastos["fecha"].append(dirFecha)
        seleccion = input("Ingrese 'S' para guardar o 'C' para cancelar: ")
        seleccionMayus = seleccion.capitalize()

        if (seleccionMayus == "S"):
            listaGastos.append(dirGastos)
            guardarJSON(listaGastos)
            print("¡DATOS GUARDADOS CON ÉXITO!")
            print("="*linea)


        elif (seleccionMayus == "C"):
            
            print("¡LOS DATOS NO SE HAN ALMACENADO!")
            print("="*linea)
        
    elif(opcionUsuario == 2):
        opcion2 = True
        while(opcion2):
            print("="*linea)

            print(f"Listar Gastos".center(linea))
            print("="*linea)

            print("Seleccione una opción para filtrar los gastos: ")
            listarGasto = int(input("1. Ver todos los gastos \n2. Filtrar por categoría \n3. Filtrar por rango de fechas \n4. Regresar al menú principal\n"))
            
            if (listarGasto == 1):
                print("="*linea)
                print("                Todos los Gastos")
                print("="*linea)
                
                mostrarTodos(listaGastos)

            elif(listarGasto == 2):
                print(f"Categorias".center(linea))
                print(f"="*linea)
                categoria = obtenerCat(listaGastos)
                for cat in range(len(categoria)):
                    print(f"{categoria[cat]}")
                print(f"="*linea)
                categoria = input(f"Por favor, digite la categoria que quieras consultar(ej. comida, transporte, entretenimiento, otros): \n")
                categoriaMayus = categoria.lower()
                mostrarUna(listaGastos,categoriaMayus)

            elif(listarGasto == 3):
                print("="*linea)
                print(f"Rango de fechas".center(linea))
                print("="*linea)
                fechaInicialStr = input("Por favor, digite la fecha inicial(dd-mm-aaaa): ")
                fechaFinalStr  = input("Por favor, digite la fecha final(dd-mm-aaaa): ")
                fechaInicial =  datetime.strptime(fechaInicialStr,"%d-%m-%Y").date()
                fechaFinal = datetime.strptime(fechaFinalStr,"%d-%m-%Y").date()
                mostrarConFechas(listaGastos,fechaInicial,fechaFinal)

            elif(listarGasto == 4):
                print("="*linea)
                print(f"Regresando al menú principal".center(linea))
                print("="*linea)
                opcion2 = False

    elif(opcionUsuario == 3):
        opcion3 = True #Validar 
        while(opcion3):
            print("="*linea)
            print(str("Calcular Gastos").center(linea))
            print("="*linea)
            calcularGasto = int(input("Seleccione el periodo de cálculo: \n1. Calcular total diario \n2. Calcular total semanal \n3. Calcular total mensual \n4. Regresar al menú principal\n"))
            print("="*linea)
            diaActual = str(datetime.now().date())
            diaActualFormat = datetime.strptime(diaActual, "%Y-%m-%d").date()
       
        
            #calcularGasto = int(input("Opción incorrecta. Valida las opciones e intentalo nuevamente\n"))

            if(calcularGasto == 1): #Total diario: Calcula y muestra el total de gastos del día actual.
                print("="*linea)
                print(str("Total Gastos el dia de hoy").center(linea))
                totalDiario = calcularDiario(listaGastos,diaActualFormat)
                print(str(str(diaActualFormat).center(linea)))
                print(str(str(totalDiario)).center(linea))
                print("="*linea)

            elif(calcularGasto == 2): #Total semanal: Calcula y muestra el total de gastos de los últimos siete días.
                print("="*linea)
                print(f"Total Gastos Semanales".center(linea))
                fechaLimite = diaActualFormat - timedelta(days=7)
                totalSemanal = calcularSemanal(listaGastos,fechaLimite)
                print(f"Desde {fechaLimite}".center(linea))
                print(f"{totalSemanal}".center(linea))
                print("="*linea)

            elif(calcularGasto == 3):
                print("="*linea)
                print(f"Total Gasto Mensual".center(linea))
                mesFormat = datetime.strptime(diaActual, "%Y-%m-%d").month
                totalMes = calcularMes(listaGastos,mesFormat)
                print(f"Para el mes: {mesFormat-1}".center(linea))
                print(str(str(totalMes)+"").center(linea))
                print(f"="*linea)

            elif(calcularGasto == 4):
                print("="*linea)

                print(str("Volviendo al menú anterior").center(linea))
                print("="*linea)
                opcion3 = False

    elif(opcionUsuario == 4):
        diaActual = datetime.now()
        diaActualFormat = diaActual.strftime(" %A, %d de %B de %Y")
        diaActual1 = datetime.now()
        diaActual2 = diaActual1.strftime("%d-%m-%Y")
        diaSuma = datetime.strptime(diaActual2,"%d-%m-%Y").date()
        opcion4 = True
        while(opcion4):
            print(f"="*linea)
            print(f"Generar Reporte de Gastos".center(linea))
            print(f"="*linea)
            generarReporte= int(input(f"Seleccione el tipo de reporte:\n 1. Reporte Diario\n 2. Reporte Semanal\n 3. Reporte Mensual\n 4. Regresar al menú principal\n"))
            print(f"="*linea)
    
            if generarReporte == 1:
                totalDiario = calcularDiario(listaGastos,diaSuma)
                print(diaSuma)
                verGuardar = int(input(f"¿Desea ver el reporte en pantalla o desea guardalo en un archivo .JSON?\n Presione 1 para ver en pantalla o 2 para guardar: \n"))

                if(verGuardar == 1):
                    print("="*linea)
                    print(f'Reporte de Gastos del Día:{diaActualFormat}')
                    print("="*linea)
                    print(f"Total de Gastos: ${totalDiario}\n")
                    print(f"Por categorías: \n")
                    sumarCatDiario(listaGastos,diaActual2)

                elif(verGuardar == 2):
                    guardarReporteEnJSON(listaGastos,"reporte_gastos_diario.json")   
            
            elif generarReporte == 2:
                diaSuma = datetime.strptime(diaActual2,"%d-%m-%Y").date()
                fechaLimite = diaSuma - timedelta(days=7)
                totalSemanal = calcularSemanal(listaGastos,fechaLimite)
                print("="*linea)
                print(f"Reporte de Gastos Semanales Desde: {fechaLimite}")
                print(f"Total de Gastos: ${totalSemanal}\n")
                sumarCatSemanal(listaGastos,fechaLimite)

            elif generarReporte == 3:
                print("="*linea)
                print(f"Reporte Gasto Mensual".center(linea))
                diaActualOpc3 = str(datetime.now().date())
                mesFormat = datetime.strptime(diaActualOpc3, "%Y-%m-%d").month
                totalMes = calcularMes(listaGastos,mesFormat)
                print("="*linea)
                print(f"Reporte de Gastos Semanales Desde: {mesFormat}")
                print(f"Total de Gastos: ${totalMes}\n")
                sumarCatMensual(listaGastos,mesFormat)

            elif generarReporte ==4:
                print("="*linea)
                print(f'Volviendo al menú principal')
                print("="*linea)
                opcion4 = False

    elif(opcionUsuario == 5):
        print(f"Ejecución terminada. \n ¡Nos vemos pronto!")
        ejecucionPrograma = False
