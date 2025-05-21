from datetime import datetime
linea = 45

def recorrerFecha(listaGastos,rango):
    for i in range(len(listaGastos[rango]["fecha"])):
            print("Dia: ",listaGastos[rango]["fecha"][i]["dia"])
            print("Hora: ",listaGastos[rango]["fecha"][i]["hora"])
    return listaGastos[rango]["fecha"]

def mostrarTodos (listaGastos):
    for i in range (len(listaGastos)):
                print("=============================================")
                print(str("Gasto #"+str(i+1)+" ============").center(linea))
                print("=============================================")            
                print("Monto:", str(listaGastos[i]["monto"]))
                print("Categoria:",listaGastos[i]["categoria"])
                print("Descripción:",listaGastos[i]["descripcion"])           
                listaFecha = recorrerFecha (listaGastos,i)
                

def mostrarUna(listaGastos, categoriaMayus):
    cont = 1
    for i in range (len(listaGastos)):
                if(listaGastos[i]["categoria"] == categoriaMayus):
                    print("=============================================")
                    print(str("Gastos por categoría"+categoriaMayus+" " +str(cont)).center(linea))
                    print("=============================================")            
                    print("Monto:", str(listaGastos[i]["monto"]))
                    print("Categoria:",listaGastos[i]["categoria"])
                    print("Descripción:",listaGastos[i]["descripcion"])
                    listaFecha = recorrerFecha (listaGastos,i)

                    cont +=1
    if(cont == 1):
        print("La categoria: ",categoriaMayus.upper(),"  que ha ingresado no existe. Valide las opciones e intentelo nuevamente")


def mostrarConFechas(listaGastos,fechaInicial,fechaFinal):
        for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"],"%d-%m-%Y").date()
                if(fechaInicial <= convertirFecha <= fechaFinal):
                    print("=============================================")
                    print(str("Gastos por fecha").center(linea))
                    print("=============================================")            
                    print(f"Monto: {listaGastos[i]['monto']}".center(linea))
                    print(f"Categoria: {listaGastos[i]['categoria']}".center(linea))
                    print(f"Descripcion: {listaGastos[i]['descripcion']}".center(linea))
                    listaFecha = recorrerFecha (listaGastos,i)

def calcularDiario(listaGastos,diaFormat):
            totalDiario = 0
            for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"], "%d-%m-%Y").date()
                if(diaFormat == convertirFecha):
                    totalDiario = totalDiario + listaGastos[i]["monto"]
            #print("=============================================")
           # print(str("Gastos en el día de hoy").center(linea))
            print(str(str(diaFormat).center(linea)))
            print(str(str(totalDiario)).center(linea))
            print("=============================================")

def calcularSemanal(listaGastos,fechaLimite):
            totalSemanal = 0
            for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"], "%d-%m-%Y").date()
                if(fechaLimite <= convertirFecha):
                    totalSemanal = totalSemanal + listaGastos[i]["monto"]
            #print("=============================================")
            #print(str("Gastos Semanales").center(linea))
            print(str("Desde "+str(fechaLimite)).center(linea))
            print(str(str(totalSemanal)).center(linea))
            print("=============================================")

def calcularMes (listaGastos,mes):
            totalMes = 0
            for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"], "%d-%m-%Y").month
                if (convertirFecha == (mes-1)):
                    totalMes = totalMes + listaGastos[i]["monto"]
            #print("=============================================")
            #print(str("Gastos Mensuales").center(linea))
            print(str("Para el mes: "+str(mes-1)).center(linea))
            print(str(str(totalMes)+"").center(linea))
            print("=============================================")